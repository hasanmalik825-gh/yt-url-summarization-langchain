FROM python:3.11-slim

# 1) set working dir early
WORKDIR /app

# 2) install deps
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 3) copy *everything* (including your app/ folder)
COPY . .

# 4) ensure Python will look in /app for modules
ENV PYTHONPATH=/app

EXPOSE 8001

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]
