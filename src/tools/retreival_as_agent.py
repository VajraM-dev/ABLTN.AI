from langchain.tools import tool
from src.agents.retrival_agent import agent

@tool
def ableton_retrieval_tool(query: str) -> str:
    """
    This function retrieves information from Ableton-related resources based on the provided query from the official Ableton documentation.
    Args:
        query (str): The search query string.
    Returns:
        str: Retrieved information relevant to the query.
    """
    result = agent.invoke(
        {"messages": [{"role": "user", "content": query}]}
    )

    return result