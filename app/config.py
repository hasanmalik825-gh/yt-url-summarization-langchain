import os

IP_WHITELIST = os.environ.get("IP_WHITELIST") or ["127.0.0.1", "172.17.0.1"]

GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
GROQ_MODEL_NAME = os.environ.get("GROQ_MODEL_NAME")


OPENAI_MODEL_NAME = os.environ.get("OPENAI_MODEL_NAME")
AZURE_OPENAI_API_KEY = os.environ.get("AZURE_OPENAI_API_KEY")
API_VERSION = os.environ.get("API_VERSION")
AZURE_OPENAI_ENDPOINT = os.environ.get("AZURE_OPENAI_ENDPOINT")

