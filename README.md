# Web & YouTube Content Summarizer

A FastAPI and Streamlit-based application that summarizes web content and YouTube videos using LangChain with support for multiple LLM providers (Groq and Azure OpenAI).

## Features

- Summarize content from:
  - Web pages
  - YouTube videos
- Multiple summarization strategies:
  - Stuff (for shorter content)
  - Map-reduce (for longer content with chunking)
  - Refine (iterative refinement)
- Support for different LLM providers:
  - Groq
  - Azure OpenAI
- Dual interfaces:
  - REST API (FastAPI)
  - Web UI (Streamlit)
- IP whitelisting for API security

## Prerequisites

- Python 3.11
- Groq API key and/or Azure OpenAI access
- Docker (optional)

## Installation

1. Clone the repository
2. Create and activate a virtual environment (recommended)
3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Configuration

1. Copy `.env.example` to `.env`
2. Configure the following environment variables:
```
# if using GROQ model only specify it's model name and api key.
GROQ_API_KEY=your-groq-api-key
GROQ_MODEL_NAME=your-groq-model-name
# if using Azure OpenAI model specify it's model name, api key, api version and endpoint.
AZURE_OPENAI_API_KEY=your-azure-openai-api-key
OPENAI_MODEL_NAME=your-model-deployment-name
API_VERSION=your-azure-api-version
AZURE_OPENAI_ENDPOINT=your-azure-endpoint
```

## Running the Application

### FastAPI Server

```bash
uvicorn main:app --host 0.0.0.0 --port 8001
```

### Streamlit Interface

```bash
streamlit run streamlit_app.py
```

### Using Docker

```bash
docker build -t content-summarizer .
docker run -p 8001:8001 content-summarizer
```

## API Endpoints

- `GET /` - Health check endpoint
- `POST /summarize` - Summarization endpoint
  - Parameters:
    - `summarization_type`: stuff/map_reduce/refine
    - `model_type`: groq/openai
    - `url`: Content URL to summarize

## Security

- API endpoints are protected with IP whitelisting
- Default whitelist: `127.0.0.1`, `172.17.0.1`
- Configure `IP_WHITELIST` in environment variables to modify


## Technologies Used

- FastAPI
- Streamlit
- LangChain
- Groq
- Azure OpenAI
- YouTube Transcript API
- Unstructured (for content parsing)