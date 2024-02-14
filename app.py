from dotenv import load_dotenv
load_dotenv() 

import streamlit as st
import  os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

#FUNCTION LOAD IN GEMINI

model=genai.GenerativeModel("gemini-pro")
def get_gemini_response(question):
    response=model.generate_content(question)
    return response.text

#initialize our streamlit app

st.set_page_config(page_title="our first project")
st.header("FIRST GENAI LLM APP")
input=st.text_input("Input: ",key="input")
submit=st.button("click")

#when its clicked
if submit:
    response=get_gemini_response(input)
    st.subheader("The Response is ")
    st.write(response)