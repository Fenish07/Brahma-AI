# Brahma

A Jarvis-style desktop assistant powered by Claude. Phase 1: text mode with tool calling.

## Setup
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate    macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env     # then paste your API key into .env
python main.py
```

## Try
- "What time is it?"
- "Open YouTube"
- "Open notepad"

## Add a tool
Create a function in `tools/` with the `@tool(...)` decorator. It is picked up automatically.

## Roadmap
1. Text brain with tools (done)
2. Voice: TTS, push-to-talk, "Brahma" wake word
3. More tools: volume, screenshot, notes/todos, web search, file search
4. Polish: logging, config, docs
