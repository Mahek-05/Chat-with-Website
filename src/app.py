import streamlit as st
from langchain_core.messages import AIMessage, HumanMessage

def get_response(user_input):
    return "I dont Know"

# app configuration
st.set_page_config(page_title="Chat-with-Websites", page_icon="🤖")
st.title("Chat with Websites")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        AIMessage(content="Hello, I am a website chat-bot. How can i help you ?"),
    ]

# sidebar
with st.sidebar:
    st.header("Settings")
    websit_url = st.text_input("Enter the URL of the website you want to chat with")

# user input  
user_query = st.chat_input("Type your message here...")

if user_query is not None and user_query != "":
    
    response = get_response(user_query)
    st.session_state.chat_history.append(HumanMessage(content=user_query))
    st.session_state.chat_history.append(AIMessage(content=response))

    # with st.sidebar:
    #     st.write(st.session_state.chat_history)
        
# conversation
for message in st.session_state.chat_history:
    if isinstance(message, AIMessage):
        with st.chat_message("AI"):
            st.write(message.content)
    elif isinstance(message, HumanMessage):
        with st.chat_message("Human"):
            st.write(message.content)