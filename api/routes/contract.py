from fastapi import APIRouter
from app.contract import IntelligentContract

router = APIRouter()

contract = IntelligentContract(owner="0xADMIN")

@router.get("/")
def root():
    return {"message": "Intelligent Contract API running"}

@router.post("/submit")
def submit(data: dict):
    return contract.submit_request("user", data)

@router.get("/verify/{request_id}")
def verify(request_id: str):
    return contract.verify(request_id)

@router.get("/history")
def history():
    return contract.history

@router.get("/state/{request_id}")
def state(request_id: str):
    return contract.state.get(request_id)