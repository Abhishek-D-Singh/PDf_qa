#!/usr/bin/env python
# coding: utf-8

# In[1]:


#pip install streamlit pypdf openai faiss-cpu langchain==0.0.77


# In[9]:


import os


# In[10]:


#os.environ["OPENAI_API_KEY"] = "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"

  

# In[3]:


from pypdf import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain import OpenAI
from langchain.chains.question_answering import load_qa_chain
from langchain.embeddings import OpenAIEmbeddings
from langchain.llms import OpenAI
from langchain.vectorstores.faiss import FAISS
from pypdf import PdfReader
import streamlit as st


# In[4]:


@st.cache
def parse_pdf(file):
    pdf = PdfReader(file)
    output = []
    for page in pdf.pages:
        text = page.extract_text()
        output.append(text)

    return "\n\n".join(output)


# In[5]:


@st.cache
def embed_text(text):
    """Split the text and embed it in a FAISS vector store"""
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=800, chunk_overlap=0, separators=["\n\n", ".", "?", "!", " ", ""]
    )
    texts = text_splitter.split_text(text)

    embeddings = OpenAIEmbeddings()
    index = FAISS.from_texts(texts, embeddings)

    return index


# In[14]:


def get_answer(index, query):
    """Returns answer to a query using langchain QA chain"""

    docs = index.similarity_search(query)

    chain = load_qa_chain(OpenAI(temperature=0))
    answer = chain.run(input_documents=docs, question=query)

    return answer


# In[ ]:




