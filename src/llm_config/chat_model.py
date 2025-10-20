from langchain.chat_models import init_chat_model
from dotenv import load_dotenv

load_dotenv()

response_model = init_chat_model("openai:gpt-5-nano-2025-08-07", temperature=0)