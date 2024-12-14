import uvicorn

from fastapi import FastAPI
from src.api import seo_route

app = FastAPI()

app.include_router(seo_route.router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
