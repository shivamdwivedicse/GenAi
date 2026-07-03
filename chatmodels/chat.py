from dotenv import load_dotenv

load_dotenv()

# from langchain.chat_models import init_chat_model

# model = init_chat_model("google_genai:gemini-2.5-flash-lite")

# model = init_chat_model("meta-llama/llama-4-scout-17b-16e-instruct" , model_provider="groq")

# model = init_chat_model("groq:openai/gpt-oss-120b")

# insted of chat init let use this 
from langchain_mistralai import ChatMistralAI

model = ChatMistralAI(model= "mistral-small-2603")

response = model.invoke("give me a paragraph on machine learning")
print(response.content)
