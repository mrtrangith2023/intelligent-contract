from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

# 1️⃣ Khởi tạo app trước
app = FastAPI(title="Intelligent Contract API Demo")

# 2️⃣ Thêm CORS middleware
origins = ["http://localhost:5174"]  # frontend local URL

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 3️⃣ In-memory storage
tokens = []
token_counter = 1

# 4️⃣ Model dữ liệu
class Token(BaseModel):
    owner: str
    token_id: int = None

# 5️⃣ Endpoints
@app.post("/mint", response_model=Token)
def mint_token(token: Token):
    global token_counter
    token.token_id = token_counter
    tokens.append(token.dict())
    token_counter += 1
    return token

@app.get("/tokens", response_model=List[Token])
def get_tokens():
    return tokens

@app.get("/")
def read_root():
    return {"message": "Backend is live!"}