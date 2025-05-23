from google.adk.agents import Agent
from google.adk.tools import google_search


# Default properties doesn't work.
def get_current_time() -> dict:  # ? Must specify return type
    # ? Provide a detailed explanation in the Dock String to assist the agent in understanding the purpose of this function.
    """
    Get the current time in the format YYYY-MM-DD HH:MM:SS.
    """
    from datetime import datetime

    return {
        "current_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }


root_agent = Agent(
    name="tool_agent",
    model="gemini-2.0-flash",
    description="Tool agent",
    instruction="""
    You are a helpful assistant that can use the following tools:
    - get_current_time
    """,
    # tools=[google_search],
    tools=[get_current_time],
    # tools=[google_search, get_current_time], # <--- Doesn't work
)
