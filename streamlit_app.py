import streamlit as st
import asyncio
from utils.web_scrapper import get_web_text, get_youtube_text
from summarizer import summarize_documents

st.title("Summarizer of the web and YT videos")
st.sidebar.title("Summarization Type")
summarization_type = st.sidebar.selectbox("Select Summarization Type", ["stuff", "map_reduce", "refine"])
groq_api_key = st.sidebar.text_input("Enter your Groq API Key", type="password")

url = st.text_input("Enter the URL of the content to summarize")

async def summarize():
    if "youtube.com" in url:
        docs = await get_youtube_text(url)
    else:
        docs = await get_web_text(url)
    return summarize_documents(docs, summarization_type, groq_api_key)

if st.button("Summarize"):
    if not url or not groq_api_key:
        st.error("Please enter both URL and Groq API Key")
    else:
        try:
            st.info("Summarizing...")
            summary = asyncio.run(summarize())
            st.success('Summarization completed')
            with st.expander("Summary Result", expanded=True):
                st.write(summary)
        except Exception as e:
            st.error(f"An error occurred: {e}")

