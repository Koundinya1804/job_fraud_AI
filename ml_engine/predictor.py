import joblib
import re
import numpy as np
from scipy.sparse import hstack

# Load model and vectorizer
model = joblib.load("models/fraud_model.pkl")
vectorizer = joblib.load("models/tfidf_vectorizer.pkl")


def clean_text(text):

    text = text.lower()
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"[^a-z\s]", " ", text)
    text = re.sub(r"\s+", " ", text)

    return text.strip()


def detect_keyword(text, keywords):
    return int(any(word in text for word in keywords))


def predict_job(description):

    clean = clean_text(description)

    # TF-IDF features
    vec = vectorizer.transform([clean])

    # Fraud indicators
    fee_keywords = ["registration fee", "training fee", "processing fee"]
    whatsapp_keywords = ["whatsapp"]
    telegram_keywords = ["telegram"]
    urgent_keywords = ["urgent hiring", "immediate joining"]

    fee_flag = detect_keyword(clean, fee_keywords)
    whatsapp_flag = detect_keyword(clean, whatsapp_keywords)
    telegram_flag = detect_keyword(clean, telegram_keywords)
    urgent_flag = detect_keyword(clean, urgent_keywords)

    extra_features = np.array([[fee_flag, whatsapp_flag, telegram_flag, urgent_flag]])

    X = hstack([vec, extra_features])

    prediction = model.predict(X)[0]
    probability = model.predict_proba(X)[0][1]

    return prediction, probability