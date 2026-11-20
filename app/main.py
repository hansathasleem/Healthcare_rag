from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from app.services.rag_service import (
    build_knowledge_base,
    answer_question
)

app = FastAPI(
    title="Healthcare RAG API",
    description="Healthcare Policy Question Answering API",
    version="1.0.0"
)

class QuestionRequest(BaseModel):
    question: str = Field(min_length=1)

# Global variables
index = None
chunks = None

@app.on_event("startup")
def startup_event():
    global index, chunks

    index, chunks = build_knowledge_base()

    print("Healthcare RAG is ready!")

@app.get("/")
def home():
    return {
        "message": "Healthcare RAG API is running"
    }

@app.post("/ask")
def ask_question(request: QuestionRequest):

    if index is None or chunks is None:
        raise HTTPException(
            status_code=503,
            detail="Knowledge base is not available"
        )

    result = answer_question(
        request.question,
        index,
        chunks
    )

    return result