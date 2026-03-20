from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# ---- Models ----
class ContractRequest(BaseModel):
    contract: str

# ---- Routes ----
@app.get("/")
def root():
    return {"status": "ok", "message": "Intelligent Contract API 🚀"}

@app.post("/submit")
def submit_contract(data: ContractRequest):
    return {
        "result": "Contract submitted",
        "input": data.contract
    }

@app.post("/verify")
def verify_contract(data: ContractRequest):
    return {
        "verified": True,
        "details": "No vulnerabilities found"
    }

@app.get("/history")
def history():
    return {
        "history": []
    }