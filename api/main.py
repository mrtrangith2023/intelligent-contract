from fastapi import FastAPI
from app.contract import IntelligentContract
from api.routes.contract import router as contract_router

app = FastAPI()

app.include_router(contract_router, prefix="/api")

contract = IntelligentContract(owner="0xADMIN")


def root():
    return {"message": "Intelligent Contract API running"}


def submit(data: dict):
    return contract.submit_request("user", data)


def verify(request_id: str):
    return contract.verify(request_id)

# 🔥 NEW ENDPOINTS


def history():
    return contract.history

    
def state(request_id: str):
    return contract.state.get(request_id)