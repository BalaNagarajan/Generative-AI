import pandas as pd
import streamlit as st
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import google.generativeai as genai
from langchain.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()
os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def process_data(df):
    """Process data and return processed DataFrame"""
    #Convert the data frame to text and split it into chunks
    text = df.to_string()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=1000)
    chunks = text_splitter.split_text(text)
    #Get the vector store
    embeddings = GoogleGenerativeAIEmbeddings(model = "models/embedding-001")
    vector_store = FAISS.from_texts(chunks, embedding=embeddings)
    vector_store.save_local("faiss_index")
    st.subheader("Vector store created successfully!")

def get_conversational_chain():

    prompt_template = """
    Answer the question in detail based on the provided context, the response should be detailed and try to perform any analytical operations based on the request, if the answer is not in
    if the question is out of provided context then respond, "Answer is related to context", don't provide the wrong answer\n\n
    Context:\n {context}?\n
    Question: \n{question}\n

    Answer:
    """

    model = ChatGoogleGenerativeAI(model="gemini-pro",
                             temperature=0.5)

    prompt = PromptTemplate(template = prompt_template, input_variables = ["context", "question"])
    chain = load_qa_chain(model, chain_type="stuff", prompt=prompt)

    return chain

def user_input(user_question):
    embeddings = GoogleGenerativeAIEmbeddings(model = "models/embedding-001")
    new_db = FAISS.load_local("faiss_index", embeddings,allow_dangerous_deserialization=True)
    docs = new_db.similarity_search(user_question)
    chain = get_conversational_chain()
    response = chain(
        {"input_documents":docs, "question": user_question}
        , return_only_outputs=True)

    print(response)
    st.write("Reply: ", response["output_text"])

def main():
    
    st.set_page_config("Workorder Chat Bot")
    st.title("Work Order Chatbot")
    user_question = st.text_input("Enter your work order questions")
    if user_question:
        user_input(user_question)



    with st.sidebar:
        st.title("Work Order Processing")
        st.write("Upload a CSV file to begin")   
        uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
        if uploaded_file is not None:
            df = pd.read_csv(uploaded_file)
            st.success("File uploaded successfully!")

            process_button = st.button("Process Data")
            if process_button:
                process_data(df.copy())  # Avoid modifying original data
                
        else:
           st.info("Upload a CSV file to begin.")

if __name__ == "__main__":
  main()
