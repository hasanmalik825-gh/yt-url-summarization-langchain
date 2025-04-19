from fastapi import FastAPI
import uvicorn
from app.routes import index_router, summarization_router
from app.middleware.middleware import add_middleware

app = FastAPI()

app.middleware("http")(add_middleware)
app.include_router(index_router)
app.include_router(summarization_router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)