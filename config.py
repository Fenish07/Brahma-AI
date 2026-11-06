"""Central settings for Brahma."""
from pathlib import Path

ASSISTANT_NAME = "Brahma"
MODEL = "claude-sonnet-5-5"
MAX_TOKENS = 600
MAX_HISTORY = 20  # messages kept in memory

DATA_DIR = Path(__file__).parent / "data"
DATA_DIR.mkdir(exist_ok=True)

# File tools (added in later phases) may only touch these folders.
ALLOWED_FOLDERS = [Path.home() / "Documents", Path.home() / "Downloads"]

SYSTEM_PROMPT = (
    f"You are {ASSISTANT_NAME}, a concise voice assistant running on the user's laptop. "
    "Your replies are spoken aloud, so speak naturally: short sentences, no markdown, "
    "no bullet lists. Use your tools to take actions instead of describing how to do them. "
    "If a request is destructive or ambiguous, ask for confirmation first."
)
