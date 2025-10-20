from langchain_community.tools import YouTubeSearchTool
from langchain.tools import tool
import ast

search_tool = YouTubeSearchTool()

@tool
def search_videos(query: str):
    """
    This function searches for YouTube videos based on the provided query
    and returns a list of video URLs.
    Args:
        query (str): The search query string.
    Returns:
        List[str]: A list of YouTube video URLs matching the search query.
    """
    results = search_tool.run(query)

    final_result = ast.literal_eval(results)
    return final_result