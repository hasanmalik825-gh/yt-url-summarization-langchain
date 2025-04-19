import streamlit as st
import asyncio
from app.utils.web_scrapper import get_web_text, get_youtube_text
from app.summarizer import summarize_documents

st.title("Summarizer of the web and YT videos")
st.sidebar.title("Select Model and Summarization Type")
model_type = st.sidebar.selectbox("Model Type", ["groq", "openai"])
summarization_type = st.sidebar.selectbox("Summarization Type", ["stuff", "map_reduce", "refine"])
api_key = st.sidebar.text_input("Enter your Groq or OpenAI API Key", type="password")

url = st.text_input("Enter the URL of the content to summarize")

async def summarize():
    if "youtube.com" in url:
        docs = await get_youtube_text(url)
    else:
        docs = await get_web_text(url)
    return summarize_documents(docs, model_type, summarization_type, api_key)

if st.button("Summarize"):
    if not url or not api_key:
        st.error("Please enter both URL and API Key")
    else:
        try:
            st.info("Summarizing...")
            summary = asyncio.run(summarize())
            st.success('Summarization completed')
            with st.expander("Summary Result", expanded=True):
                st.write(summary)
        except Exception as e:
            st.error(f"An error occurred: {e}")

