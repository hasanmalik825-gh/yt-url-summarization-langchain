from enum import Enum
from typing import Optional
from fastapi import APIRouter, Query
from app.summarizer import summarize_documents
from app.utils.web_scrapper import get_web_text, get_youtube_text
import logging

summarization_router = APIRouter()

class SummarizationType(str, Enum):
    stuff = "stuff"
    map_reduce = "map_reduce"
    refine = "refine"

class ModelType(str, Enum):
    groq = "groq"
    openai = "openai"

@summarization_router.post("/summarize")
async def summarize_endpoint(
    summarization_type: SummarizationType,
    model_type: ModelType,
    url: str = Query(..., description="The URL of the content to summarize"),
):
    
    if "youtube.com" in url:
        docs = await get_youtube_text(url)
    else:
        docs = await get_web_text(url)
    
    try:
        summary = summarize_documents(docs, model_type, summarization_type)
        return {
        "summary": summary,
        "source_url": url,
        "summarization_type": summarization_type,
        "model_type": model_type
    }
    except Exception as e:
        logging.error(f"Error summarizing content: {e}")
        return {
            "error": "Failed to summarize content"
        }