from app.contract import IntelligentContract

def test_submit_and_verify():
    contract = IntelligentContract("admin")

    data = {
        "reputation": 80,
        "stake": 150,
        "activity": True
    }

    res = contract.submit_request("user1", data)
    assert res["result"]["decision"] == "approve"

    assert contract.verify(res["request_id"]) == True