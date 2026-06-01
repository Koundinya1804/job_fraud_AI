import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


def show_dashboard():

    st.subheader("Fraud Analytics Dashboard")

    # Example fraud indicator data
    data = {
        "Indicator": [
            "Registration Fee",
            "WhatsApp Contact",
            "Telegram Contact",
            "Urgent Hiring",
            "No Interview"
        ],
        "Frequency": [45, 32, 10, 20, 15]
    }

    df = pd.DataFrame(data)

    st.write("### Fraud Indicator Frequency")

    fig, ax = plt.subplots()

    ax.bar(df["Indicator"], df["Frequency"])

    ax.set_xlabel("Fraud Indicator")
    ax.set_ylabel("Frequency")
    ax.set_title("Common Fraud Indicators")

    plt.xticks(rotation=45)

    st.pyplot(fig)

    # Prediction distribution
    st.write("### Prediction Distribution")

    pred_data = {
        "Category": ["Genuine Jobs", "Fraud Jobs"],
        "Count": [80, 20]
    }

    pred_df = pd.DataFrame(pred_data)

    fig2, ax2 = plt.subplots()

    ax2.pie(
        pred_df["Count"],
        labels=pred_df["Category"],
        autopct="%1.1f%%"
    )

    ax2.set_title("Fraud vs Genuine Jobs")

    st.pyplot(fig2)