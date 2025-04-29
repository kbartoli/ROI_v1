import streamlit as st
from helper_chat import chat, get_llm

#making sure user is logged in
if not st.experimental_user.is_logged_in:
    st.write("Please log in to use the chat!")
    st.stop()

# initializing and storing the llm is session state so I do not need to reinitialize every run
if "llm" not in st.session_state:
    st.session_state.llm = get_llm()

if "messages" not in st.session_state:
    st.session_state["messages"] = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])




#user_query = st.chat_input("Ask something:")
if user_query:= st.chat_input("Ask somthing: "):
    st.chat_message("user").write(user_query)
    st.session_state.messages.append({"role":"user", "content":user_query})
    response = chat(st.session_state.llm, st.session_state.messages)
    st.session_state.messages.append({"role":"assistant", "content":response})
    st.chat_message("assistant").write(response)

if st.button("Clear chat"):
    st.session_state.messages.clear()
    st.rerun()