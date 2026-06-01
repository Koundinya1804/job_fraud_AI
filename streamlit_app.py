import streamlit as st
import plotly.graph_objects as go

from ml_engine.predictor import predict_job
from ml_engine.semantic_detector import semantic_fraud_check

from rules.fraud_rules import detect_indicators, detect_patterns, generate_reasoning
from rules.company_check import analyze_company
from rules.scam_network import update_pattern_database, detect_scam_network

from scraper.job_scraper import scrape_job_description
from dashboard.analytics import show_dashboard
from database.db_manager import init_db


init_db()

st.set_page_config(page_title="AI Job Fraud Detection System", layout="centered")


# ---------------- RISK METER ---------------- #

def show_risk_meter(prob):

    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=prob * 100,
        title={'text': "Fraud Risk Score"},
        gauge={
            'axis': {'range': [0, 100]},
            'bar': {'color': "red"},
            'steps': [
                {'range': [0, 30], 'color': "green"},
                {'range': [30, 70], 'color': "yellow"},
                {'range': [70, 100], 'color': "red"}
            ]
        }
    ))

    st.plotly_chart(fig)


# ---------------- HYBRID RISK SCORE ---------------- #

def compute_risk_score(prob, patterns, semantic_flag, company_warnings):

    risk = prob

    if patterns:
        risk += 0.55

    if semantic_flag:
        risk += 0.30

    if company_warnings:
        risk += 0.20

    return min(risk, 1.0)


# ---------------- UI ---------------- #

st.title("AI Job Fraud Detection System")

option = st.radio(
    "Select Input Type",
    ["Paste Job Description", "Paste Job URL"]
)


# ================= DESCRIPTION INPUT ================= #

if option == "Paste Job Description":

    text = st.text_area("Enter Job Description")

    if st.button("Analyze Job"):

        if text.strip() == "":
            st.warning("Please enter a job description")

        else:

            pred, prob = predict_job(text)

            indicators = detect_indicators(text)

            patterns = detect_patterns(indicators)

            explanations = generate_reasoning(indicators, patterns)

            semantic_flag, _ = semantic_fraud_check(text)

            company_warnings = analyze_company(text)

            update_pattern_database(patterns)

            network_alerts = detect_scam_network()


            final_risk = compute_risk_score(
                prob,
                patterns,
                semantic_flag,
                company_warnings
            )

            show_risk_meter(final_risk)


            if final_risk > 0.6:
                st.error(f"⚠ High Fraud Risk ({final_risk:.2f})")

            elif final_risk > 0.35:
                st.warning(f"⚠ Suspicious Job ({final_risk:.2f})")

            else:
                st.success(f"✅ Likely Genuine Job ({final_risk:.2f})")


            if patterns:
                st.subheader("Fraud Patterns Detected")
                for p in patterns:
                    st.write("⚠", p)


            if explanations:
                st.subheader("AI Fraud Reasoning")
                for e in explanations:
                    st.write("•", e)


            if semantic_flag:
                st.subheader("Context-Aware Detection")
                st.write(
                    "The system detected language similar to known job scams."
                )


            if company_warnings:
                st.subheader("🏢 Company Credibility Warning")
                for w in company_warnings:
                    st.write("⚠", w)


            if network_alerts and patterns:
                st.subheader("🌐 Scam Network Detection")
                for alert in network_alerts:
                    st.write("⚠", alert)


# ================= URL INPUT ================= #

else:

    url = st.text_input("Enter Job URL")

    if st.button("Scan Job"):

        if url.strip() == "":
            st.warning("Please enter a URL")

        else:

            job_text = scrape_job_description(url)

            if job_text == "":
                st.error("Could not extract job description")

            else:

                pred, prob = predict_job(job_text)

                indicators = detect_indicators(job_text)

                patterns = detect_patterns(indicators)

                explanations = generate_reasoning(indicators, patterns)

                semantic_flag, _ = semantic_fraud_check(job_text)

                company_warnings = analyze_company(job_text)

                update_pattern_database(patterns)

                network_alerts = detect_scam_network()


                final_risk = compute_risk_score(
                    prob,
                    patterns,
                    semantic_flag,
                    company_warnings
                )

                show_risk_meter(final_risk)


                if final_risk > 0.6:
                    st.error(f"⚠ High Fraud Risk ({final_risk:.2f})")

                elif final_risk > 0.35:
                    st.warning(f"⚠ Suspicious Job ({final_risk:.2f})")

                else:
                    st.success(f"✅ Likely Genuine Job ({final_risk:.2f})")


                if patterns:
                    st.subheader("Fraud Patterns Detected")
                    for p in patterns:
                        st.write("⚠", p)


                if explanations:
                    st.subheader("AI Fraud Reasoning")
                    for e in explanations:
                        st.write("•", e)


                if semantic_flag:
                    st.subheader("Context-Aware Detection")
                    st.write(
                        "The system detected language similar to known job scams."
                    )


                if company_warnings:
                    st.subheader("🏢 Company Credibility Warning")
                    for w in company_warnings:
                        st.write("⚠", w)


                if network_alerts and patterns:
                    st.subheader("🌐 Scam Network Detection")
                    for alert in network_alerts:
                        st.write("⚠", alert)


st.divider()

if st.button("Show Fraud Analytics Dashboard"):
    show_dashboard()
    