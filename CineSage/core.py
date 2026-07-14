 # from dotenv import load_dotenv
# from langchain_core.prompts import ChatPromptTemplate
# load_dotenv()

# from langchain_mistralai import ChatMistralAI

# model = ChatMistralAI(model = "mistral-small-2603")

# prompt = ChatPromptTemplate.from_messages([
#     (
# "system",

# """
# You are a professional Movie Information Extraction Assistant.

# Your responsibility is to extract useful structured information from a movie description accurately.

# Rules:
# - Extract only the information explicitly mentioned.
# - Never guess or hallucinate missing details.
# - If a field is missing, return "NULL".
# - Keep the summary within 2-3 sentences.
# - Return the output in a clean and readable format.
# - Do not add explanations or extra commentary.

# Extract the following information:

# 🎬 Movie Information
# - Movie Title
# - Release Year
# - Genre
# - Director
# - Runtime
# - Language
# - Country
# - IMDb Rating
# - Awards

# 🎭 Cast
# - Lead Cast
# - Supporting Cast

# 📖 Story
# - Plot
# - Main Goal
# - Conflict
# - Setting

# 🎵 Technical Details
# - Music Composer
# - Production Company
# - Cinematographer

# ⭐ Highlights
# - Major Themes
# - Notable Features
# - Critical Reception
# - Audience Reception
# - Interesting Facts

# 📝 Quick Summary
# Generate a concise summary in 2-3 sentences.

# Return the output exactly in this format:

# Movie Title:
# Release Year:
# Genre:
# Director:
# Runtime:
# Language:
# Country:
# IMDb Rating:
# Awards:

# Lead Cast:
# Supporting Cast:

# Plot:
# Main Goal:
# Conflict:
# Setting:

# Music Composer:
# Production Company:
# Cinematographer:

# Major Themes:
# Notable Features:
# Critical Reception:
# Audience Reception:
# Interesting Facts:

# Summary:
# """

# ),
# (
# "human",

# """
# Extract the useful information from the following movie description.

# Movie Description:

# {paragraph}
# """)
# ]) 

# para = input("Give your paragraph :")

# final_prompt = prompt.invoke(
#     {"paragraph" : para}
# )
# response = model.invoke(final_prompt)

# print(response.content)






# ---------Structured Prompt or Structured output using pydentic (Output gets stored in json)--------------------


from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel
from typing import List,Optional
from langchain_core.output_parsers import PydanticOutputParser
load_dotenv()
from langchain_mistralai import ChatMistralAI
model = ChatMistralAI(model = "mistral-small-2603")




# step1 - create a schema
class Movie(BaseModel):   #it is schema
    title: str
    relese_year: Optional[int]
    genre : List[str]
    director:Optional[str]
    caste: List[str]
    rating: Optional[float]
    summary: str

#step2 :- Create Parser
parser = PydanticOutputParser(pydantic_object= Movie) #checks all info. is correct or not 

prompt = ChatPromptTemplate.from_messages([
    ('system',"""
Extract movei information from the paragraph
     {format_instructions} """),
     ('human',"{paragraph}")
]) 


para = input("Give your paragraph :")

final_prompt = prompt.invoke(
    {"paragraph" : para,
     'format_instructions': parser.get_format_instructions}
)

response = model.invoke(final_prompt)

print(response.content)
