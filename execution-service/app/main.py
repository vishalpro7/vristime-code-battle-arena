from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title = "Vristime Execution Engine"
)

class CodeSubmission(BaseModel):
    language : str
    code : str
    test_case : list[dict]

@app.get("/health")
def health_check():
    return {
        "status" : "Execution Service is running"
    }

@app.post("/execute")
def execute_code(
    submission : CodeSubmission
):
    return {
        "message" : "Received submission successfully!", 
        "language" : submission.language, 
        "code_length" : len(submission.code)
    }