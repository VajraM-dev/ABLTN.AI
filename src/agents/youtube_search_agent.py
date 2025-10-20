from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from src.tools.video_search_tool import search_videos
from src.tools.video_retreival_tool import retrieve_transcripts
from src.prompts.youtube_parsing_prompt import SYSTEM_PROMPT
from src.middleware.tool_error_handling import handle_tool_errors
from dotenv import load_dotenv
load_dotenv()

model = ChatOpenAI(
    model="gpt-5-nano-2025-08-07",
    temperature=0.1,
)

tools = [search_videos, retrieve_transcripts]

agent = create_agent(model, tools=tools, system_prompt=SYSTEM_PROMPT, middleware=[handle_tool_errors])

# for chunk in agent.stream({
#     "messages": [{"role": "user", "content": "How to make tight techno basslines, my current kick and bass sound muddy?"}]
# }, stream_mode="values"):
#     # Each chunk contains the full state at that point
#     latest_message = chunk["messages"][-1]
#     if latest_message.content:
#         print(f"Agent: {latest_message.content}")
#     elif latest_message.tool_calls:
#         print(f"Calling tools: {[tc['name'] for tc in latest_message.tool_calls]}")