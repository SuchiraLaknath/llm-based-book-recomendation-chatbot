from frontend_files.read_config import Configurations
import streamlit as st
import requests
import time

configs = Configurations().get_config()

backend_url = configs['backend']['url']

st.title("Book recomending chatbot")

def response_generator(prompt):
    
    # response = asnswer_the_question(prompt)
    url = f"{backend_url}/chat"
    response = requests.post(url=url, json ={'user_input': prompt}, 
                             headers={"Content-Type": "application/json"})
    
    response = response.json()
    answer = response["result"]
    
    for word in answer.split("\n"):
        yield f'''{word}  \n'''
        time.sleep(0.05)
  
def load_messages():
    url = f"{backend_url}/get_conversation_history"
    msgs = requests.get(url=url).json()["chat_memory"]["messages"]
    messages = []
    role = None
    for message in msgs:
        if message["type"] == "human":
            role = "user"
        elif message["type"] == "ai":
            role = "assistant"
        else:
            pass
        if role != None:
            translated_msg = {"role":role , "content":message["content"]}
            messages.append(translated_msg)
    return messages

def clear_memory():
    requests.post(
        url=f"{backend_url}/clear_conversation_history"
    )
    time.sleep(0.05)
    st.session_state.messages = load_messages()

if "messages" not in st.session_state:
    st.session_state.messages = load_messages()

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Hi, What can I do for you?"):
    
    if prompt:
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        # Display user message in chat message container
        with st.chat_message("user"):
            st.markdown(prompt)

        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            response = st.write_stream(response_generator(prompt))
            # Add assistant response to chat history
            st.session_state.messages.append({"role": "assistant", "content": response})

with st.sidebar:
    with st.container():
        st.button("Clear Chat",
                  type="primary",
                  on_click=clear_memory
                  )