from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain.chains.summarize import load_summarize_chain
from langchain_core.runnables.base import Runnable
from langchain_core.documents import Document
from constants import GROQ_API_KEY
from typing import List

def summarize_documents(
        docs: List[Document], 
        summarization_type: str,
        groq_api_key: str = GROQ_API_KEY
    ) -> Runnable:
    prompt_template = PromptTemplate(
        template="""
        Summarize the following content in 100 words:
        Content: {text}
        """,
    )
    llm = ChatGroq(model="llama3-8b-8192",api_key=groq_api_key, streaming=True)
    chain = load_summarize_chain(
        llm=llm, 
        prompt=prompt_template, 
        chain_type=summarization_type,
        verbose=True
    )
    summary = chain.run(docs)
    return summary

