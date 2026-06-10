import os 
from dotenv import load_dotenv
from langchain_ollama import OllamaLLM
load_dotenv()

print("API KEY:", os.getenv("LANGCHAIN_API_KEY"))
print("PROJECT:", os.getenv("LANGCHAIN_PROJECT"))
print("Current Directory:", os.getcwd())







import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT")

###Prompt Template

prompt  = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant that helps answer questions about the world."),
        ("user", "Question: {question}")
    ]
)


###Streamlit App
st.title("Ollama LLM with Langchain")
input_text = st.text_input("What is your question?")


###Ollama Llama2 model
llm = OllamaLLM(model="gemma:2b")
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

if input_text:
    st.write(chain.invoke({"question": input_text}))

     


