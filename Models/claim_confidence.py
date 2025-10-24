def calculate_claim_confidence(damage_severity, text_confidence, fraud_flag):
    severity_score = {"Low": 0.9, "Medium": 0.7, "High": 0.5}.get(damage_severity, 0.6)
    fraud_score = 0.2 if fraud_flag else 1.0
    combined = severity_score * text_confidence * fraud_score
    return round(combined, 2)
