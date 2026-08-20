import os
from pathlib import Path
from dotenv import load_dotenv
from google.adk import Agent

# Load environment variables
ENV_PATH = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=ENV_PATH)

# Plain Python dictionary for session state
MEMORY = {}

def save_user_preference(key: str, value: str) -> str:
    """Saves a user preference key and value into memory.

    Args:
        key: The preference name, like 'favorite_team' or 'language'.
        value: The preference value, like 'Arsenal' or 'Python'.
    """
    MEMORY[key] = value
    return f"Successfully saved {key} = {value}"

def get_user_preferences() -> dict:
    """Retrieves all saved user preferences from memory."""
    return MEMORY

root_agent = Agent(
    name="personal_assistant",
    model="gemini-2.5-flash",
    description="A technical assistant with memory.",
    instruction="You are a helpful assistant. Use your tools to save and read user preferences.",
    tools=[save_user_preference, get_user_preferences],
)