from dotenv import load_dotenv
load_dotenv() ## loading all the environment variables
from tools import ImageGenerationTool
import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

## function to load Gemini Pro model and get repsonses
model=genai.GenerativeModel("gemini-pro") 
chat = model.start_chat(history=[])
def get_gemini_response(question):
    
    response=chat.send_message(question,stream=True)
    return response

##initialize our streamlit app

st.set_page_config(page_title="GenerativeAI - GeminiPro")

st.header("Fashion Recommendation ChatBot :sunglasses:", divider='rainbow')

st.text(":red[Note] :- Include #generate in input to generate an Image")

# Initialize session state for chat history if it doesn't exist
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

input=st.text_input("Input: ",key="input")
submit=st.button("Send")

if submit and input:
    img_path = ""
    if '#generate' in input:
        API_TOKEN = st.secrets['HUGGINGFACE_API_TOKEN']
        API_URL = st.secrets['HUGGINGFACE_API_URL']
        img_path = ImageGenerationTool().run(input,API_TOKEN,API_URL)
        input = input.replace("#generate","write a short note on ")
        print(img_path)
        st.image(img_path, use_column_width=True)
    response=get_gemini_response(input)
    # Add user query and response to session state chat history
    st.session_state['chat_history'].append(("You", input,''))
    st.subheader("The Response is")
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(("Bot", chunk.text,img_path))
    
st.subheader("The Chat History is")

with st.expander("View History  :point_down:"):
    for role, text, img_path in st.session_state['chat_history']:
        if role=='You':
            st.write(f":blue[{role}]: {text}")
        elif role == prev:
            st.write(f"{text}")
        else:
            st.write(f":green[{role}]: ")
            try:
                st.image(img_path)
            except Exception as e:
                print(e)
            st.write(f"{text}")
        prev = role
    



    

