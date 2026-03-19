from typing import Dict, Any
from app.ai import ai_evaluate
from app.verifier import verify_result
import hashlib
import json
import uuid
import time


class IntelligentContract:
    def __init__(self, owner: str):
        self.owner = owner
        self.state: Dict[str, Any] = {}
        self.history = []

    def _hash(self, data: Any) -> str:
        return hashlib.sha256(
            json.dumps(data, sort_keys=True).encode()
        ).hexdigest()

    def _log(self, action: str, data: Any, request_id: str = None):
        self.history.append({
            "timestamp": time.time(),
            "action": action,
            "request_id": request_id,
            "data": data,
            "hash": self._hash(data)
        })

    def submit_request(self, user: str, data: Dict[str, Any]):
        result = ai_evaluate(data)

        # 🔥 FIX: unique ID
        request_id = str(uuid.uuid4())

        self.state[request_id] = {
            "user": user,
            "data": data,
            "result": result,
            "status": "pending",
            "created_at": time.time()
        }

        self._log("submit_request", result, request_id)

        return {
            "request_id": request_id,
            "result": result,
            "status": "pending"
        }

    def verify(self, request_id: str):
        record = self.state.get(request_id)

        if not record:
            return {"valid": False, "error": "Not found"}

        is_valid = verify_result(record["data"], record["result"])

        # 🔥 FIX: update state
        record["status"] = "verified" if is_valid else "rejected"
        record["verified_at"] = time.time()

        self._log("verify", {"valid": is_valid}, request_id)

        return {
            "valid": is_valid,
            "status": record["status"]
        }