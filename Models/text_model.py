from transformers import pipeline

class ClaimTextAnalyzer:
    def __init__(self):
        self.analyzer = pipeline("text-classification", model="distilbert-base-uncased")

    def analyze_claim(self, text):
        result = self.analyzer(text[:512])[0]
        return {"intent": "Vehicle Damage Claim", "confidence": round(result['score'], 2)}
