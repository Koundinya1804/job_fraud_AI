# 🕵️ AI Job Fraud Detection System

> An intelligent, multi-layer system that analyzes job postings and flags fraudulent listings using machine learning, semantic similarity, rule-based reasoning, and scam network detection.

---

## 📌 Overview

Fake job listings are a growing threat — designed to steal money or personal data from unsuspecting job seekers. This project combines a trained ML classifier, semantic NLP analysis, rule-based fraud indicators, and a company credibility checker into a single Streamlit web app that gives every job posting a **real-time fraud risk score**.

You can paste a job description directly or provide a URL, and the system returns a color-coded risk meter along with a human-readable explanation of every red flag it found.

---

## ✨ Features

| Feature | Description |
|---|---|
| 🤖 ML Classifier | TF-IDF + Random Forest model trained on real fraud/genuine job data |
| 🧠 Semantic Detector | Sentence-BERT embeddings compared against known scam phrases |
| 📋 Rule Engine | Keyword + pattern matching for payment demands, urgency tactics, and suspicious contact channels |
| 🏢 Company Checker | Flags free-email domains and missing company website references |
| 🌐 Scam Network | SQLite-backed tracker that surfaces patterns appearing across multiple posts |
| 📊 Analytics Dashboard | Bar chart and pie chart showing fraud indicator frequency and prediction distribution |
| 🔗 URL Scraping | Automatically fetches and parses job descriptions from a given URL |

---

## 🏗️ Project Structure

```
job_fraud_ai_project/
│
├── streamlit_app.py          # Main UI — risk meter, input handling, result display
│
├── ml_engine/
│   ├── predictor.py          # Loads trained model, cleans text, runs TF-IDF + extra features
│   └── semantic_detector.py  # Sentence-BERT cosine similarity against fraud phrase bank
│
├── rules/
│   ├── fraud_rules.py        # Indicator detection, pattern matching, natural-language reasoning
│   ├── company_check.py      # Email domain and website credibility checks
│   └── scam_network.py       # Pattern frequency tracker (wraps db_manager)
│
├── dashboard/
│   └── analytics.py          # Matplotlib charts rendered inside Streamlit
│
├── database/
│   └── db_manager.py         # SQLite init, update, and alert query functions
│
├── scraper/
│   └── job_scraper.py        # BeautifulSoup URL scraper
│
├── models/
│   ├── fraud_model.pkl        # Pre-trained Random Forest classifier
│   └── tfidf_vectorizer.pkl   # Fitted TF-IDF vectorizer
│
├── fraud_patterns.db          # SQLite database (auto-created on first run)
├── requirements.txt
└── LICENSE
```

---

## ⚙️ How It Works

### Risk Score Pipeline

```
Job Text Input
      │
      ├──▶ ML Predictor (TF-IDF + keyword flags)  ──▶ base probability
      ├──▶ Semantic Detector (SBERT cosine sim)    ──▶ +0.30 if flagged
      ├──▶ Rule Engine (pattern combos)            ──▶ +0.55 if flagged
      └──▶ Company Checker (email / website)       ──▶ +0.20 if flagged
                                                          │
                                              Final Risk Score (capped at 1.0)
```

### Risk Thresholds

| Score | Label |
|---|---|
| > 0.60 | ⚠️ High Fraud Risk |
| 0.35 – 0.60 | ⚠️ Suspicious |
| < 0.35 | ✅ Likely Genuine |

### Fraud Indicators Detected

- **Payment requests** — registration fee, training fee, security deposit, activation fee, and 15+ variants
- **External contact** — WhatsApp, Telegram, "DM HR", "send your details to"
- **Urgency tactics** — "limited seats", "immediate joining", "hurry up", "last few openings"
- **No interview** — explicit claims of hiring without any interview process

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Koundinya1804/job_fraud_ai_project.git
cd job_fraud_ai_project
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the app

```bash
streamlit run streamlit_app.py
```

The app will open in your browser at `http://localhost:8501`.

---

## 📦 Dependencies

```
streamlit
scikit-learn
joblib
scipy
numpy
sentence-transformers
plotly
matplotlib
pandas
requests
beautifulsoup4
```

> The pre-trained models (`fraud_model.pkl` and `tfidf_vectorizer.pkl`) are included in the `models/` directory. No training step is required to run the app.

---

## 🗄️ Database

The app uses a local SQLite database (`fraud_patterns.db`) to track how often each fraud pattern appears across analyzed job posts. When any single pattern has been seen **3 or more times**, it triggers a **Scam Network Alert** in the UI.

The database is initialized automatically on first run — no setup needed.

---

## 📸 App Preview

### Input Options
- **Paste Job Description** — directly enter text for analysis
- **Paste Job URL** — the scraper fetches and parses the page for you

### Output Sections
- 🎯 **Risk Meter** — animated gauge from 0–100
- ⚠️ **Fraud Patterns** — matched rule combinations
- 💬 **AI Fraud Reasoning** — plain-English explanations for each flag
- 🧠 **Context-Aware Detection** — semantic similarity result
- 🏢 **Company Credibility Warning** — email / website checks
- 🌐 **Scam Network Detection** — cross-post pattern frequency alerts
- 📊 **Analytics Dashboard** — fraud indicator bar chart + prediction pie chart

---

## 🛡️ Disclaimer

This tool is designed to assist job seekers in identifying potentially fraudulent listings. It is not a guarantee — always verify job offers independently before sharing personal information or making any payment.

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

## 👤 Author

**Koundinya1804**  
Built with Python, Streamlit, scikit-learn, and Sentence Transformers.

---

*If this project helped you, consider giving it a ⭐ on GitHub!*
