# from dotenv import load_dotenv

# load_dotenv()

# from langchain_mistralai import ChatMistralAI

# from langchain_core.messages import AIMessage , SystemMessage ,HumanMessage

# model = ChatMistralAI(model = "mistral-small-2603" , temperature=0.9)

# messages = [
#     SystemMessage(content ="you are a sad AI agent ") #role of the ai system 

# ]

# print("---------------Welcome to the CHATBOT Type 0 to exit the application-----------------------")
# while True:

#     prompt = input("You : ")
#     messages.append(HumanMessage(content = prompt))  #append(prompt) to HumanMessage
#     if prompt == "0":
#         break

#     response = model.invoke(messages)
#     messages.append(AIMessage(content = response.content))
#     print("Bot :", response.content)
# print(messages)





# -------------Prompt Templates---------------

from dotenv import load_dotenv

load_dotenv()

from langchain_mistralai import ChatMistralAI

from langchain_core.messages import AIMessage , SystemMessage ,HumanMessage

model = ChatMistralAI(model = "mistral-small-2603" , temperature=0.9)

print("Choose your AI Mode")
print("Press 1 for Angry mode")
print("Press 2 for funny mode")
print("Press 3 for sad Mode")

choice = int(input("Tell your response :-"))

if choice ==1:
    mode = "You are an angry ai agent. You respond agressively and impatiently"
elif choice ==2:
    mode = "You are a very funny ai agent. You respond with humor and jokes"
elif choice == 3:
    mode = "You are a very sad ai agent. You respond in depressed and emotional tone."

messages = [
    SystemMessage(content =mode) #role of the ai system 

]

print("---------------Welcome to the CHATBOT Type 0 to exit the application-----------------------")
while True:

    prompt = input("You : ")
    messages.append(HumanMessage(content = prompt))  #append(prompt) to HumanMessage
    if prompt == "0":
        break

    response = model.invoke(messages)
    messages.append(AIMessage(content = response.content))
    print("Bot :", response.content)
print(messages)