from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from src.tools.retreival_as_agent import ableton_retrieval_tool
from src.tools.youtube_agent_as_tool import ask_youtube_agent
from src.prompts.main_agent_prompt import MAIN_AGENT_SYSTEM_PROMPT
from langchain.agents.middleware import SummarizationMiddleware
from src.middleware.tool_error_handling import handle_tool_errors
import os
from langgraph.checkpoint.postgres import PostgresSaver  
from langgraph.checkpoint.memory import InMemorySaver
from langchain_core.runnables import RunnableConfig
from dotenv import load_dotenv
load_dotenv()

model = ChatOpenAI(
    model="gpt-5-nano-2025-08-07",
    temperature=0.1,
)

tools = [ableton_retrieval_tool, ask_youtube_agent]

summary_generator = SummarizationMiddleware(
            model="openai:gpt-4o-mini",
            # max_tokens_before_summary=4000,  # Trigger summarization at 4000 tokens
            messages_to_keep=10,  # Keep last 20 messages after summary
        )

environment = os.environ.get("ENVRIONMENT", "development")

if environment == "development":
    checkpointer = InMemorySaver()
else:
    DB_URI = os.environ.get("CHAT_HISTORY_DB_URL")
    # with PostgresSaver.from_conn_string(DB_URI) as checkpointer:
    _checkpointer_cm = PostgresSaver.from_conn_string(DB_URI)
    checkpointer = _checkpointer_cm.__enter__()
    checkpointer.setup() # auto create tables in PostgresSql

agent = create_agent(model, tools=tools, system_prompt=MAIN_AGENT_SYSTEM_PROMPT, middleware=[handle_tool_errors, summary_generator], checkpointer=checkpointer)

def resond_to_user(question: str, config: str = "default") -> str:
    config: RunnableConfig = {"configurable": {"thread_id": config}}
    for chunk in agent.stream({
        "messages": [{"role": "user", "content": question}]
    }, stream_mode="values", config=config):
        # Each chunk contains the full state at that point
        latest_message = chunk["messages"][-1]
        if latest_message.content:
            print(f"Agent: {latest_message.content}")
        elif latest_message.tool_calls:
            print(f"Calling tools: {[tc['name'] for tc in latest_message.tool_calls]}")