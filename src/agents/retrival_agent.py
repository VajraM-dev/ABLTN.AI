from langchain.agents import create_agent #, AgentState
# from langchain.messages import RemoveMessage
from src.tools.retrieval_tool import retrieve_context
from src.llm_config.chat_model import response_model as llm
from src.prompts.prompt_loader import load_system_prompt
from src.middleware.tool_error_handling import handle_tool_errors
from langgraph.checkpoint.postgres import PostgresSaver  
# from langgraph.graph.message import REMOVE_ALL_MESSAGES
# from langgraph.runtime import Runtime
from langchain.agents.middleware import SummarizationMiddleware
# from langchain.agents.middleware import after_model
from langgraph.checkpoint.memory import InMemorySaver
from src.tools.quality_of_life_tools import (
    clarify,
    confirm_action,
    flag_content,
    suggest_alternative,
    request_context,
)
from dotenv import load_dotenv
import os
load_dotenv()

tools = [
    retrieve_context,
    clarify,
    confirm_action,
    flag_content,
    suggest_alternative,
    request_context,
]

# @after_model
# def delete_old_messages(state: AgentState, runtime: Runtime) -> dict | None:
#     """Remove old messages to keep conversation manageable."""
#     messages = state["messages"]

#     if len(messages) > 6:
#         new_msgs = messages[-6:]
#         return {
#             "messages": [
#                 RemoveMessage(id=REMOVE_ALL_MESSAGES),
#                 *new_msgs
#             ]
#         }

summary_generator = SummarizationMiddleware(
            model="openai:gpt-4o-mini",
            # max_tokens_before_summary=4000,  # Trigger summarization at 4000 tokens
            messages_to_keep=10,  # Keep last 20 messages after summary
        )

# If desired, specify custom instructions
prompt = load_system_prompt("response_prompt")

environment = os.environ.get("ENVRIONMENT", "development")

if environment == "development":
    checkpointer = InMemorySaver()
else:
    DB_URI = os.environ.get("CHAT_HISTORY_DB_URL")
    # with PostgresSaver.from_conn_string(DB_URI) as checkpointer:
    _checkpointer_cm = PostgresSaver.from_conn_string(DB_URI)
    checkpointer = _checkpointer_cm.__enter__()
    checkpointer.setup() # auto create tables in PostgresSql

agent = create_agent(
    llm, 
    tools, 
    system_prompt=prompt,
    middleware=[handle_tool_errors, summary_generator],
    checkpointer=checkpointer
)