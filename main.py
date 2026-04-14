from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from router import router

app = FastAPI(
    title="Streaming LLM Applications with FastAPI",
    description="Learn to stream LLM responses in real-time with Server-Sent Events",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)


@app.get("/")
async def root():
    return {
        "service": "streaming-llm-fastapi",
        "docs": "/docs",
        "health": "/bedtime-story/health",
    }
