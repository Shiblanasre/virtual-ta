from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class QuestionRequest(BaseModel):
    question: str
    image: Optional[str] = None

@app.post("/api/")
async def get_answer(req: QuestionRequest):
    # Replace this with your real answer logic
    return {
        "answer": f"You asked: {req.question}",
        "links": ["https://example.com/discussion"]
    }
