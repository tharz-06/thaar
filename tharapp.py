import streamlit as st
import google.generativeai as genai


st.title("welcome")

genai.configure(api_key="AIzaSyCI8tx92q_i_0p5TF8N7Qo1m7yAnsmvUDQ")
text =st.text_input("enter your question")

model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])



if st.button("Click me"):
 response = chat.send_message(text)
 st.write(response.text)