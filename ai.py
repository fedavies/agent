import os
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv

load_dotenv(".env")

print( os.getenv("AZURE_OPENAI_API_KEY"))
print( os.getenv("AZURE_OPENAI_ENDPOINT"))
print( os.getenv("OPENAI_API_VERSION"))

llm = init_chat_model(
    "azure_openai:gpt-4o-mini",
    azure_deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
)