def ai_evaluate(input_data):
    score = 0

    if input_data.get("reputation", 0) > 70:
        score += 1
    if input_data.get("stake", 0) > 100:
        score += 1
    if input_data.get("activity"):
        score += 1

    decision = "approve" if score >= 2 else "reject"

    return {
        "score": score,
        "decision": decision
    }