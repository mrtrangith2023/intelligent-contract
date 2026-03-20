from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# ---- Fake DB ----
history_db = []

# ---- Model ----
class ContractRequest(BaseModel):
    contract: str

# ---- Routes ----
@app.get("/")
def root():
    return {"status": "ok", "message": "Intelligent Contract API 🚀"}

@app.post("/submit")
def submit(data: ContractRequest):
    result = {
        "action": "submit",
        "contract": data.contract,
        "status": "received"
    }
    history_db.append(result)
    return result

@app.post("/verify")
def verify(data: ContractRequest):
    result = {
        "action": "verify",
        "contract": data.contract,
        "verified": True,
        "risk": "Low",
        "details": "No major vulnerabilities found"
    }
    history_db.append(result)
    return result

@app.get("/history")
def history():
    return {"history": history_db}