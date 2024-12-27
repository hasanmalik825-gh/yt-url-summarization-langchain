from enum import Enum
from typing import Optional
from fastapi import APIRouter, Query
from summarizer import summarize_documents
from utils.web_scrapper import get_web_text, get_youtube_text

summarization_router = APIRouter()

class SummarizationType(str, Enum):
    stuff = "stuff"
    map_reduce = "map_reduce"
    refine_chain = "refine"

@summarization_router.post("/summarize")
async def summarize_endpoint(
    summarization_type: SummarizationType,
    url: str = Query(..., description="The URL of the content to summarize"),
):
    
    if "youtube.com" in url:
        docs = await get_youtube_text(url)
    else:
        docs = await get_web_text(url)
    summary = summarize_documents(docs, summarization_type)
    return {
            "summary": summary,
            "source_url": url,
            "summarization_type": summarization_type
        }