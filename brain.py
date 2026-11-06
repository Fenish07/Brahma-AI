"""The LLM brain: Claude with a tool-calling loop and short-term memory."""
import anthropic

import config
import tools


class Brain:
    def __init__(self) -> None:
        self.client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY
        self.history: list[dict] = []

    def _trim_history(self) -> None:
        """Keep recent messages, always starting on a plain user message
        so tool_use / tool_result pairs are never split."""
        if len(self.history) <= config.MAX_HISTORY:
            return
        self.history = self.history[-config.MAX_HISTORY:]
        while self.history and not (
            self.history[0]["role"] == "user" and isinstance(self.history[0]["content"], str)
        ):
            self.history.pop(0)

    def ask(self, user_text: str) -> str:
        """Send user text, run any tool calls, return the final spoken reply."""
        self.history.append({"role": "user", "content": user_text})
        try:
            while True:
                resp = self.client.messages.create(
                    model=config.MODEL,
                    max_tokens=config.MAX_TOKENS,
                    system=config.SYSTEM_PROMPT,
                    tools=tools.get_schemas(),
                    messages=self.history,
                )
                self.history.append({"role": "assistant", "content": resp.content})
                if resp.stop_reason != "tool_use":
                    reply = "".join(b.text for b in resp.content if b.type == "text")
                    self._trim_history()
                    return reply
                results = [
                    {
                        "type": "tool_result",
                        "tool_use_id": b.id,
                        "content": tools.run_tool(b.name, b.input),
                    }
                    for b in resp.content
                    if b.type == "tool_use"
                ]
                self.history.append({"role": "user", "content": results})
        except anthropic.APIConnectionError:
            self.history.pop()
            return "I can't reach the internet right now."
        except anthropic.APIStatusError as e:
            self.history.pop()
            return f"The API returned an error: {e.status_code}."
