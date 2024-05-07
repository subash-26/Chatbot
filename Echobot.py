import streamlit as st
import random
import time


#with st.chat_message(name = "user", avatar="💕"):
#   st.write("Hello 😍")


st.title("Chatbot")


#Initialize a chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat message from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("Whats Up ?"):
    # Display a user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role" : "user", "content" : prompt })

    response = f"Echo: {prompt}"
    #Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)

    # Add assistant response to chat history

    st.session_state.messages.append({"role" : "assistant", "content" : prompt })