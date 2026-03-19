from app.ai import ai_evaluate

def verify_result(data, result):
    recalculated = ai_evaluate(data)
    return recalculated["decision"] == result["decision"]