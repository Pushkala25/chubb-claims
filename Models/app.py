import streamlit as st
from models.image_model import DamageClassifier
from models.text_model import ClaimTextAnalyzer
from models.fraud_detector import FraudDetector
from models.claim_confidence import calculate_claim_confidence
from PIL import Image

st.set_page_config(page_title="AI Claims Assessment", page_icon="🤖")

st.title("🤖 AI-Powered Claims Assessment & Fraud Detection System")
st.write("Upload an image and description to generate automated claim analysis.")

img_model = DamageClassifier()
text_model = ClaimTextAnalyzer()
fraud_model = FraudDetector()

uploaded_image = st.file_uploader("Upload Damage Image", type=["jpg", "png", "jpeg"])
claim_text = st.text_area("Enter Claim Description")

if uploaded_image and claim_text:
    with open("temp_img.jpg", "wb") as f:
        f.write(uploaded_image.getbuffer())

    st.image(Image.open("temp_img.jpg"), caption="Uploaded Image", use_column_width=True)

    with st.spinner("Analyzing claim..."):
        damage_type, severity = img_model.predict_damage("temp_img.jpg")
        text_info = text_model.analyze_claim(claim_text)
        fraud_flag, fraud_msg = fraud_model.check_fraud("temp_img.jpg")
        confidence = calculate_claim_confidence(severity, text_info["confidence"], fraud_flag)

    st.success("✅ Analysis Complete")
    st.subheader("Results")
    st.write(f"**Damage Type:** {damage_type}")
    st.write(f"**Severity:** {severity}")
    st.write(f"**Claim Intent:** {text_info['intent']} (Confidence: {text_info['confidence']})")
    st.write(f"**Fraud Check:** {fraud_msg}")
    st.write(f"**Claim Confidence Score:** {confidence}")
