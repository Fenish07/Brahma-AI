"""Brahma entry point (Phase 1: text mode)."""
import os
import sys

from dotenv import load_dotenv

import config

load_dotenv()


def main() -> None:
    if not os.getenv("ANTHROPIC_API_KEY"):
        sys.exit("Set ANTHROPIC_API_KEY in a .env file (see .env.example).")

    from brain import Brain  # imported after env is loaded

    brain = Brain()
    print(f"{config.ASSISTANT_NAME} online. Type 'quit' to exit.\n")
    while True:
        try:
            text = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break
        if not text:
            continue
        if text.lower() in {"quit", "exit"}:
            break
        print(f"{config.ASSISTANT_NAME}: {brain.ask(text)}\n")


if __name__ == "__main__":
    main()
