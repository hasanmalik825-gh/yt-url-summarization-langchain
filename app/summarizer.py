from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain.chains.summarize import load_summarize_chain
from langchain_core.runnables.base import Runnable
from langchain_core.documents import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import AzureChatOpenAI
from app.config import AZURE_OPENAI_ENDPOINT, API_VERSION, OPENAI_MODEL_NAME, GROQ_MODEL_NAME, GROQ_API_KEY, AZURE_OPENAI_API_KEY
from typing import List

def summarize_documents(
        docs: List[Document],
        model_type: str,
        summarization_type: str,
        api_key: str = GROQ_API_KEY or AZURE_OPENAI_API_KEY
    ) -> Runnable:

    if model_type == "openai":
        llm = AzureChatOpenAI(
            deployment_name=OPENAI_MODEL_NAME,
            api_key=api_key,
            api_version=API_VERSION,
            azure_endpoint=AZURE_OPENAI_ENDPOINT,
            streaming=True,
        )
    elif model_type == "groq":
        llm = ChatGroq(model=GROQ_MODEL_NAME, api_key=api_key, streaming=True)
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)

    if summarization_type == "stuff":
        return _stuff_summarizer(docs, llm)
    elif summarization_type == "map_reduce":
        split_docs = text_splitter.split_documents(documents=docs)
        return _map_reduce_summarizer(split_docs, llm)
    elif summarization_type == "refine":
        #split_docs = text_splitter.split_documents(documents=docs)
        return _refine_chain_summarizer(docs, llm)

def _stuff_summarizer(docs: List[Document], llm: ChatGroq | AzureChatOpenAI):
    prompt=PromptTemplate(template=""" Write a concise and short summary of the following document,
    Document :{text}
    """
    )
    chain = load_summarize_chain(
        llm=llm,
        chain_type="stuff",
        prompt=prompt,
        verbose=True
    )
    return chain.run(docs)

def _map_reduce_summarizer(docs: List[Document], llm: ChatGroq):
    chunk_prompt = PromptTemplate(
        template=""" Write a concise and short summary of the following document,
        Document :{text}
        Summary :
        """
    )
    combine_prompt = PromptTemplate(
        template=""" Provide the final summary of the entire document with the following format,
        Format : Title, Genre, Summary.
        Documents :{text}
        """
    )
    chain = load_summarize_chain(
        llm=llm,
        chain_type="map_reduce",
        map_prompt=chunk_prompt,
        combine_prompt=combine_prompt,
        verbose=True
    )
    return chain.run(docs)

def _refine_chain_summarizer(docs: List[Document], llm: ChatGroq):
    prompt = PromptTemplate(
        template=""" Write a concise and short summary.
        """
    )
    chain = load_summarize_chain(
        llm=llm,
        #prompt=prompt,
        chain_type="refine",
        verbose=True,
    )
    return chain.run(docs)

