# from src.agents.retrival_agent import agent
# from langchain_core.runnables import RunnableConfig

from src.agents.main_agent import resond_to_user

# def get_response(query: str, config: str = "default"):
#     config: RunnableConfig = {"configurable": {"thread_id": config}}

#     query = (
#         """System Instructions: You must use retrieve_context tool for ANY question about:
#         - Ableton Live features, settings, or workflows
#         - Technical issues, troubleshooting, or errors
#         - How to do something in Ableton Live
#         - Specific Ableton functions, devices, or instruments

#         Do NOT use retrieve_context for:
#         - Greetings (hi, hello, how are you)
#         - General conversation unrelated to Ableton

#         Remember user specific information like name, preferences, and past interactions to provide personalized responses.
        
#         \n\n
#         """

#         f"User Query: {query}"
#     )

#     for event in agent.stream(
#         {"messages": [{"role": "user", "content": query}]},
#         config,
#         stream_mode="values",
#     ):

#         # Each chunk contains the full state at that point
#         latest_message = event["messages"][-1]
#         if latest_message.content:
#             print(f"Agent: {latest_message.content}")
#         elif latest_message.tool_calls:
#             print(f"Calling tools: {[tc['name'] for tc in latest_message.tool_calls]}")

def main():

    while True:
        query = input("You: ")
        if query.lower() in ["exit", "quit"]:
            break
        else:
            resond_to_user(
                query,
                config="1",
            )

    # return True

if __name__ == "__main__":
    main()
