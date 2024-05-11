import openai 
import streamlit as st
import pydantic


st.title("Chat-GPT like clone")

#openai.api_key = st.secrets["OPENAI_API_KEY"] 

#client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

api_key=st.secrets["OPENAI_API_KEY"]
#client = OpenAI.api_key = api_key

openai.api_key = api_key

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"


#Initialize a chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat message from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("Whats Up ?"):

    # Add user message to chat history
    st.session_state.messages.append({"role" : "user", "content" : prompt })

    # Display a user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        stream = openai.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        )
        response = st.write_stream(stream)
    
    st.session_state.messages.append({"role": "assistant", "content": response})


    #Response Message
#   with st.chat_message("assistant"):
#        message_placeholder = st.empty()
#        full_response = ""
#        for response in openai.chat.completions.create(
#            model=st.session_state["openai_model"],
#            messages=[
#                {"role": m["role"], "content": m["content"]}
#                for m in st.session_state.messages
#            ],
#            stream = True,
#        ):
            #full_response += response.choices[0].delta.get("content", "")
#            full_response += response.choices[0].
#            message_placeholder.markdown(full_response + " ")
#       message_placeholder.markdown(full_response) 
    

#    st.session_state.messages.append({"role" : "assistant", "content" : response})'''
                                     
                    