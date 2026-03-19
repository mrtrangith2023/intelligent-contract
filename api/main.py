from fastapi import FastAPI
import uuid

app = FastAPI()

# memory storage
requests_db = {}

@app.get("/")
def root():
    return {"message": "Intelligent Contract API running"}

@app.post("/submit")
def submit(data: dict):
    request_id = str(uuid.uuid4())
    
    requests_db[request_id] = {
        "data": data,
        "status": "pending"
    }

    return {
        "request_id": request_id,
        "status": "pending"
    }

@app.get("/verify/{request_id}")
def verify(request_id: str):
    if request_id not in requests_db:
        return {"valid": False, "error": "Not found"}

    return {
        "valid": True,
        "data": requests_db[request_id]
    }