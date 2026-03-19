# 🚀 Intelligent Contract API (GenLayer Testnet)
![Python](https://img.shields.io/badge/python-3.12-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-ready-green)

## 📌 Overview

This project implements an **Intelligent Contract System** using FastAPI, designed for the GenLayer ecosystem.

It demonstrates how smart contracts can leverage **AI-based evaluation and verifiable execution** to process user requests in a deterministic and auditable way.

---

## 🧠 Key Features

* 🤖 AI-powered evaluation (`ai.py`)
* ✅ Deterministic verification layer (`verifier.py`)
* 🧾 State management (pending → verified / rejected)
* 📜 Execution history tracking (audit log)
* 🔐 SHA-256 hashing for integrity
* ⚡ Modular FastAPI architecture
* 🧪 Unit testing included

---

## 🏗️ Project Structure

```
intelligent-contract/
│
├── app/
│   ├── __init__.py
│   ├── contract.py        # Core intelligent contract logic
│   ├── ai.py              # AI evaluation logic
│   ├── verifier.py        # Verification logic
│   ├── models.py          # Data models (Pydantic)
│   ├── config.py          # Environment config
│
├── api/
│   ├── main.py            # FastAPI entry point
│   ├── routes/
│   │   └── contract.py    # API routes
│
├── tests/
│   ├── test_contract.py   # Unit tests
│
├── .env.example
├── requirements.txt
├── README.md
└── run.py
```

---

## ⚙️ Installation & Run

### 1. Clone repository

```
git clone https://github.com/mrtrangith2023/intelligent-contract.git
cd intelligent-contract
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

### 3. Run server

```
uvicorn api.main:app --reload
```

---

## 🌐 API Endpoints

Base URL:

```
http://localhost:8000/api
```

### 🔹 POST /submit

Submit request for AI evaluation

**Request**

```json
{
  "user": "alice",
  "amount": 100
}
```

**Response**

```json
{
  "request_id": "uuid",
  "result": {
    "score": 0.9,
    "decision": "approved"
  },
  "status": "pending"
}
```

---

### 🔹 GET /verify/{request_id}

Verify result deterministically

**Response**

```json
{
  "valid": true,
  "status": "verified"
}
```

---

### 🔹 GET /history

View execution logs (audit trail)

---

### 🔹 GET /state/{request_id}

Get stored contract state

---

## 🧠 Intelligent Logic

* AI evaluates input data (e.g., scoring logic)
* Decision is generated (`approved` / `rejected`)
* Verification recomputes result to ensure correctness

👉 This simulates **verifiable computation in smart contracts**

---

## 🔐 Security & Integrity

* SHA-256 hashing ensures data integrity
* Every action is logged with hash + timestamp
* History acts like a blockchain audit log

---

## 🧪 Testing

Run tests:

```
pytest
```

Example:

```python
def test_submit_and_verify():
    contract = IntelligentContract("0xADMIN")
    res = contract.submit_request("user", {"amount": 100})
    assert contract.verify(res["request_id"])["valid"] is True
```

---

## 📸 Demo

Swagger UI:

```
http://localhost:8000/docs
```

---

## 🚀 Future Improvements

* Database persistence (PostgreSQL / Redis)
* Authentication (JWT)
* Advanced AI models
* On-chain integration (GenLayer L1)

---

## 🏆 Why This Project?

This project demonstrates:

* AI + Smart Contract integration
* Verifiable execution model
* Modular backend architecture
* Real-world scalable design

👉 Aligned with GenLayer vision of **intelligent, verifiable computation**

---

## 👤 Author

**TAM**
Web3 Builder | Exploring AI x Blockchain 🚀

---

## 📎 Submission

* GitHub Repo: https://github.com/mrtrangith2023/intelligent-contract
* Demo: Swagger UI (`/docs`)

---

🔥 Built for GenLayer Testnet Mission
