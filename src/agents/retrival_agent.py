from langchain.agents import create_agent #, AgentState
# from langchain.messages import RemoveMessage
from src.tools.retrieval_tool import retrieve_context
from src.llm_config.chat_model import response_model as llm
from src.prompts.prompt_loader import load_system_prompt
from src.middleware.tool_error_handling import handle_tool_errors

from src.tools.quality_of_life_tools import (
    clarify,
    confirm_action,
    flag_content,
    suggest_alternative,
    request_context,
)
from dotenv import load_dotenv
load_dotenv()

tools = [
    retrieve_context,
    clarify,
    confirm_action,
    flag_content,
    suggest_alternative,
    request_context,
]

prompt = load_system_prompt("response_prompt")

agent = create_agent(
    llm, 
    tools, 
    system_prompt=prompt,
    middleware=[handle_tool_errors]
)