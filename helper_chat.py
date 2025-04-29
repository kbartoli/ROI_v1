from langchain_aws import ChatBedrock
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
import streamlit as st

# reading secrets from the secrets file:
aws_access_key = st.secrets["aws"]["aws_access_key_id"]
aws_secret_key = st.secrets["aws"]["aws_secret_access_key"]
region = st.secrets["aws"]["region_name"]

def get_llm():
    llm = ChatBedrock(
        model = "amazon.titan-text-premier-v1:0",
        region= region,
        aws_access_key_id=aws_access_key,
        aws_secret_access_key=aws_secret_key
    )
    return llm

def chat(model, messages):
    response = model.invoke(messages)
    return response.content
