#!/usr/bin/env python
# coding: utf-8

# In[1]:



import streamlit as st
#import ipynb.fs
from main import parse_pdf, embed_text, get_answer


# In[21]:
st.header("Doc QA")
uploaded_file = st.file_uploader("Upload a pdf", type=["pdf"])
#api = st.text_input("**Enter OpenAI API Key**",type="password",placeholder="sk-")
#st.write("api:", st.secrets["api"])

#if api:
if uploaded_file is not None:
    index = embed_text(parse_pdf(uploaded_file))
    query = st.text_area("Ask a question about the document")
    button = st.button("Submit")
    if button:
        st.write(get_answer(index, query))







