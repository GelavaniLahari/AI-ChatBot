'''import streamlit as st
import requests

BACKEND_url="http://127.0.0.1:8000/chat"

st.set_page_config(
    page_title="ChatBot",
    layout="centered"
)

st.title="AI-ChatBot"

if "messages" not in st.session_state:
    st.session_state.messages=[]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
          st.write(message["content"])  

user_input=st.chat_input("How may i help you!!....")

if user_input:
     st.session_state.messages.append(
          {
               "role":"user",
               "content":user_input
          }
     )
     with st.chat_message("user"):
        st.write(user_input)

     try:
       response=requests.post(
        BACKEND_url,
        Json={
             "question":user_input}
       )  
       bot_response=response.json()["response"]

     except Exception as e:
       bot_response =f"error:{str(e)}"

     st.session_state.messages.append(
         {
             "role":"assistant",
             "content":bot_response
         }
     )  
     with st.chat_messagee("assistant"):
         st.write(bot_response)
               '''