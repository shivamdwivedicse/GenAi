from dotenv import load_dotenv
load_dotenv()

from langchain_mistralai import ChatMistralAI

model = ChatMistralAI(model = "mistral-small-2603" , temperature=0 , max_tokens=20)
#Temprature is a parameter:-
#If you want some creative task set temprature to high(0.8,0.9) and if you want to do any logical task then put temprature a little bit lower.

# max_tokens is also a parameter:-
# used for putting limits in our output

response = model.invoke("Write a poerm on AI")
print(response.content)