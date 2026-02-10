from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.chains.artifact_chain import generate_all_artifacts

app = FastAPI(title="TestCraft AI (Groq)")


class RequirementRequest(BaseModel):
    requirement: str


@app.get("/")
def home():
    return {"message": "TestCraft AI Backend Running (Groq)"}


@app.post("/generate")
def generate(req: RequirementRequest):
    try:
        return generate_all_artifacts(req.requirement)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
