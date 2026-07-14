# from dotenv import load_dotenv
# load_dotenv()

# import streamlit as st
# from langchain_core.prompts import ChatPromptTemplate
# from langchain_mistralai import ChatMistralAI

# # -----------------------------
# # PAGE CONFIG
# # -----------------------------

# st.set_page_config(
#     page_title="Movei Information Extractor",
#     page_icon="🎞️",
#     layout="wide"
# )

# # -----------------------------
# # CUSTOM CSS
# # -----------------------------

# st.markdown("""
# <style>

# .stApp{
#     background:linear-gradient(135deg,#0B0B14,#131325,#18182F);
# }

# .block-container{
#     max-width:1000px;
#     padding-top:2rem;
# }

# .title{
#     font-size:58px;
#     font-weight:800;
#     text-align:center;
#     color:white;
#     margin-bottom:5px;
# }

# .subtitle{
#     text-align:center;
#     color:#B7BDD6;
#     font-size:18px;
#     margin-bottom:35px;
# }

# textarea{
#     font-size:17px !important;
#     border-radius:18px !important;
# }

# .stTextArea textarea{
#     border-radius:18px !important;
# }

# .stButton>button{
#     width:100%;
#     height:55px;
#     border:none;
#     border-radius:15px;
#     font-size:18px;
#     font-weight:bold;
#     color:white;
#     background:linear-gradient(90deg,#7F5AF0,#2CB67D);
#     transition:0.3s;
# }

# .stButton>button:hover{
#     transform:scale(1.02);
#     box-shadow:0 0 18px rgba(127,90,240,.5);
# }

# .result-card{
#     background:#111827;
#     border-radius:18px;
#     padding:25px;
#     border-left:5px solid #7F5AF0;
#     margin-top:20px;
# }

# hr{
#     border:none;
#     height:1px;
#     background:#2C2F45;
# }

# </style>
# """, unsafe_allow_html=True)

# # -----------------------------
# # TITLE
# # -----------------------------

# st.markdown(
# """
# <div class='title'>🎞️ Movei Information Extractor</div>
# <div class='subtitle'>
# Transform movie descriptions into structured insights in seconds.
# </div>
# """,
# unsafe_allow_html=True
# )

# # -----------------------------
# # MODEL
# # -----------------------------

# model = ChatMistralAI(
#     model="mistral-small-2603",
#     temperature=0
# )

# # -----------------------------
# # PROMPT
# # -----------------------------

# prompt = ChatPromptTemplate.from_messages([

# ("system",

# """
# You are a professional Movie Information Extraction Assistant.

# Your responsibility is to extract useful structured information from a movie description accurately.

# Rules:

# - Extract only explicitly mentioned information.
# - Never guess missing information.
# - If unavailable, write NULL.
# - Keep summary within 2-3 sentences.
# - Return clean Markdown.
# - No explanations.

# Return output like:

# # 🎬 Movie Information

# **Movie Title:** ...

# **Release Year:** ...

# **Genre:** ...

# **Director:** ...

# **Runtime:** ...

# **Language:** ...

# **Country:** ...

# **IMDb Rating:** ...

# **Awards:** ...

# # 🎭 Cast

# **Lead Cast:**

# - Person 1
# - Person 2

# **Supporting Cast:**

# ...

# # 📖 Story

# **Plot:**

# ...

# **Main Goal:**

# ...

# **Conflict:**

# ...

# **Setting:**

# ...

# # 🎼 Technical Details

# **Music Composer:**

# ...

# **Production Company:**

# ...

# **Cinematographer:**

# ...

# # ✨ Highlights

# **Major Themes:**

# ...

# **Notable Features:**

# ...

# **Critical Reception:**

# ...

# **Audience Reception:**

# ...

# **Interesting Facts:**

# ...

# # 📝 Summary

# ...
# """

# ),

# ("human",

# """
# Movie Description:

# {paragraph}
# """

# )

# ])

# # -----------------------------
# # INPUT
# # -----------------------------

# paragraph = st.text_area(
#     "🪄 Paste your movie paragraph",
#     height=260,
#     placeholder="Example: Interstellar is a visually stunning science fiction film..."
# )

# # -----------------------------
# # BUTTON
# # -----------------------------

# if st.button("⚡ Extract Information"):

#     if paragraph.strip() == "":

#         st.warning("Please enter a movie description.")

#     else:

#         with st.spinner("🔮 Extracting information..."):

#             final_prompt = prompt.invoke(
#                 {
#                     "paragraph": paragraph
#                 }
#             )

#             response = model.invoke(final_prompt)

#         st.markdown("---")

#         st.markdown("## 📋 Extracted Information")

#         with st.container(border=True):
#             st.markdown(response.content)





# -------structured prompt or output in json (machine friendly output UI)


from dotenv import load_dotenv
load_dotenv()

import streamlit as st

from pydantic import BaseModel
from typing import List, Optional

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain_mistralai import ChatMistralAI


# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="🎬 Movie Information Extractor",
    page_icon="🎬",
    layout="centered"
)

st.title("🎬 Movie Information Extractor")
st.write("Extract structured movie information from any paragraph using LangChain + Mistral AI.")

# -----------------------------
# Load Model
# -----------------------------
model = ChatMistralAI(
    model="mistral-small-2603"
)


# -----------------------------
# Schema
# -----------------------------
class Movie(BaseModel):
    title: str
    release_year: Optional[int]
    genre: List[str]
    director: Optional[str]
    cast: List[str]
    rating: Optional[float]
    summary: str


# -----------------------------
# Output Parser
# -----------------------------
parser = PydanticOutputParser(pydantic_object=Movie)


# -----------------------------
# Prompt
# -----------------------------
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
Extract movie information from the paragraph.

{format_instructions}
"""
        ),
        (
            "human",
            "{paragraph}"
        ),
    ]
)


# -----------------------------
# UI
# -----------------------------
paragraph = st.text_area(
    "Enter Movie Paragraph",
    height=220,
    placeholder="Example: Interstellar is a 2014 science fiction film directed by Christopher Nolan..."
)

if st.button("Extract Information", use_container_width=True):

    if paragraph.strip() == "":
        st.warning("Please enter a paragraph.")
        st.stop()

    with st.spinner("Extracting..."):

        final_prompt = prompt.invoke(
            {
                "paragraph": paragraph,
                "format_instructions": parser.get_format_instructions()
            }
        )

        response = model.invoke(final_prompt)

        movie = parser.parse(response.content)

    st.success("Information Extracted Successfully!")

    st.subheader("🎬 Movie Details")

    st.json(movie.model_dump())