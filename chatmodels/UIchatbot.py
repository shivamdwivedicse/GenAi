# import streamlit as st
# from dotenv import load_dotenv

# load_dotenv()

# from langchain_mistralai import ChatMistralAI
# from langchain_core.messages import AIMessage, SystemMessage, HumanMessage

# st.title("🥲Welcome to the Sad CHATBOT")

# model = ChatMistralAI(model="mistral-small-2603", temperature=0.9)

# # Initialize chat history in session state
# if "messages" not in st.session_state:
#     st.session_state.messages = [
#         SystemMessage(content="you are a Sad ai agent ")  # role of the ai system
#     ]

# # Display previous messages (skip system message)
# for message in st.session_state.messages:
#     if isinstance(message, HumanMessage):
#         with st.chat_message("user"):
#             st.write(message.content)
#     elif isinstance(message, AIMessage):
#         with st.chat_message("assistant"):
#             st.write(message.content)

# prompt = st.chat_input("You : ")

# if prompt:
#     st.session_state.messages.append(HumanMessage(content=prompt))  # append(prompt) to HumanMessage
#     with st.chat_message("user"):
#         st.write(prompt)

#     response = model.invoke(st.session_state.messages)
#     st.session_state.messages.append(AIMessage(content=response.content))

#     with st.chat_message("assistant"):
#         st.write(response.content)







#------FUNNY AI CHATBOT 👇👇👇👇uncomment and use------




# import streamlit as st
# from dotenv import load_dotenv

# load_dotenv()

# from langchain_mistralai import ChatMistralAI
# from langchain_core.messages import AIMessage, SystemMessage, HumanMessage

# st.title("😂Welcome to the funny CHATBOT")

# model = ChatMistralAI(model="mistral-small-2603", temperature=0.9)

# # Initialize chat history in session state
# if "messages" not in st.session_state:
#     st.session_state.messages = [
#         SystemMessage(content="you are a funny ai agent ")  # role of the ai system
#     ]

# # Display previous messages (skip system message)
# for message in st.session_state.messages:
#     if isinstance(message, HumanMessage):
#         with st.chat_message("user"):
#             st.write(message.content)
#     elif isinstance(message, AIMessage):
#         with st.chat_message("assistant"):
#             st.write(message.content)

# prompt = st.chat_input("You : ")

# if prompt:
#     st.session_state.messages.append(HumanMessage(content=prompt))  # append(prompt) to HumanMessage
#     with st.chat_message("user"):
#         st.write(prompt)

#     response = model.invoke(st.session_state.messages)
#     st.session_state.messages.append(AIMessage(content=response.content))

#     with st.chat_message("assistant"):
#         st.write(response.content)












# ----------Manually created Prompt template chatbot UI--------------

# from dotenv import load_dotenv
# load_dotenv()

# import streamlit as st

# from langchain_mistralai import ChatMistralAI
# from langchain_core.messages import (
#     HumanMessage,
#     AIMessage,
#     SystemMessage
# )

# # ----------------------------
# # Page Configuration
# # ----------------------------

# st.set_page_config(
#     page_title="Mood AI Chatbot",
#     page_icon="🤖",
#     layout="wide"
# )

# # ----------------------------
# # Custom CSS
# # ----------------------------

# st.markdown("""
# <style>

# .main{
#     background-color:#0E1117;
# }

# .stChatMessage{
#     border-radius:15px;
#     padding:10px;
# }

# h1{
#     text-align:center;
#     color:#00FFD1;
# }

# </style>
# """, unsafe_allow_html=True)

# # ----------------------------
# # Title
# # ----------------------------

# st.title("🤖 Mood AI Chatbot")

# st.caption("Chat with AI in different moods")

# # ----------------------------
# # Sidebar
# # ----------------------------

# with st.sidebar:

#     st.header("⚙️ Settings")

#     mode = st.selectbox(
#         "Choose AI Mode",
#         [
#             "😡 Angry",
#             "😂 Funny",
#             "😢 Sad"
#         ]
#     )

#     temperature = st.slider(
#         "Temperature",
#         0.0,
#         1.0,
#         0.9
#     )

#     if st.button("🗑️ Clear Chat"):
#         st.session_state.messages = []
#         st.rerun()

# # ----------------------------
# # System Prompt
# # ----------------------------

# if mode == "😡 Angry":
#     system_prompt = (
#         "You are an angry AI assistant. "
#         "Reply aggressively, impatiently and rudely."
#     )

# elif mode == "😂 Funny":
#     system_prompt = (
#         "You are a funny AI assistant. "
#         "Always reply with humor and jokes."
#     )

# else:
#     system_prompt = (
#         "You are a sad AI assistant. "
#         "Reply in an emotional and depressed tone."
#     )

# # ----------------------------
# # Model
# # ----------------------------

# model = ChatMistralAI(
#     model="mistral-small-2603",
#     temperature=temperature
# )

# # ----------------------------
# # Session State
# # ----------------------------

# if "messages" not in st.session_state:
#     st.session_state.messages = [
#         SystemMessage(content=system_prompt)
#     ]

# # Update system prompt if mode changes

# st.session_state.messages[0] = SystemMessage(content=system_prompt)

# # ----------------------------
# # Display Chat
# # ----------------------------

# for msg in st.session_state.messages[1:]:

#     if isinstance(msg, HumanMessage):
#         with st.chat_message("user"):
#             st.write(msg.content)

#     elif isinstance(msg, AIMessage):
#         with st.chat_message("assistant"):
#             st.write(msg.content)

# # ----------------------------
# # User Input
# # ----------------------------

# prompt = st.chat_input("Type your message...")

# if prompt:

#     st.session_state.messages.append(
#         HumanMessage(content=prompt)
#     )

#     with st.chat_message("user"):
#         st.write(prompt)

#     response = model.invoke(st.session_state.messages)

#     st.session_state.messages.append(
#         AIMessage(content=response.content)
#     )

#     with st.chat_message("assistant"):
#         st.write(response.content)










