from src.agents.youtube_search_agent import agent
from langchain.tools import tool

@tool
def ask_youtube_agent(question: str) -> str:
    """
    This function takes a user question as input, invokes the YouTube search agent,
    and returns the agent's response.
    Args:
        question (str): The user's question to the YouTube search agent.
    Returns:
        str: The response from the YouTube search agent.
    """

    result = agent.invoke(
        {"messages": [{"role": "user", "content": question}]}
    )

    return result