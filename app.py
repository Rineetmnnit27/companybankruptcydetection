import streamlit as st
import pandas as pd
import numpy as np
import joblib
import plotly.express as px

# =====================================================
# Page Configuration
# =====================================================

st.set_page_config(
    page_title="FinTech AI-First Dashboard",
    page_icon="💳",
    layout="wide"
)

# =====================================================
# Load Model
# =====================================================

model = joblib.load("bankruptcy_prediction_model.pkl")

# =====================================================
# Sidebar
# =====================================================

st.sidebar.title("💳 FinTech AI Dashboard")

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Home",
        "📈 Revenue Forecast",
        "⚠ Bankruptcy Prediction",
        "🏢 Company Risk Segmentation"
    ]
)

# =====================================================
# HOME PAGE
# =====================================================

if page == "🏠 Home":

    st.title("💳 FinTech AI-First Strategy Dashboard")

    st.markdown("""
This dashboard demonstrates an AI-first strategy using multiple Machine Learning approaches.

### Implemented Models

- Revenue Forecasting (ARIMA)
- Bankruptcy Prediction (XGBoost)
- Company Risk Segmentation (K-Means)

The goal is to support better financial decision-making, credit risk assessment, and strategic planning.
""")

    st.divider()

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Companies", "6819")
    c2.metric("Financial Features", "95")
    c3.metric("Forecast Horizon", "12 Months")
    c4.metric("ML Models", "3")

# =====================================================
# FORECAST
# =====================================================

elif page == "📈 Revenue Forecast":

    st.title("📈 Revenue Forecast")

    forecast = pd.read_csv("forecasted_revenue.csv")

    st.dataframe(forecast, use_container_width=True)

    fig = px.line(
        forecast,
        x="Date",
        y="Forecasted_Revenue",
        markers=True,
        title="Next 12 Months Revenue Forecast"
    )

    st.plotly_chart(fig, use_container_width=True)

# =====================================================
# BANKRUPTCY
# =====================================================

elif page == "⚠ Bankruptcy Prediction":

    st.title("⚠ Bankruptcy Prediction")

    st.write(
        "Upload a CSV file containing the engineered financial features used during model training."
    )

    uploaded_file = st.file_uploader(
        "Upload CSV",
        type="csv"
    )

    if uploaded_file is not None:

        df = pd.read_csv(uploaded_file)

        predictions = model.predict(df)

        probabilities = model.predict_proba(df)

        result = df.copy()

        result["Prediction"] = np.where(
            predictions == 1,
            "Bankrupt",
            "Healthy"
        )

        result["Bankruptcy Probability"] = (
            probabilities[:, 1] * 100
        ).round(2)

        st.success("Prediction Completed")

        st.dataframe(result, use_container_width=True)

        csv = result.to_csv(index=False)

        st.download_button(
            "⬇ Download Prediction",
            csv,
            file_name="bankruptcy_predictions.csv",
            mime="text/csv"
        )

# =====================================================
# SEGMENTATION
# =====================================================

elif page == "🏢 Company Risk Segmentation":

    st.title("🏢 Company Risk Segmentation")

    segment = pd.read_csv("company_risk_segments.csv")

    st.dataframe(segment.head(20), use_container_width=True)

    st.subheader("Risk Distribution")

    fig = px.histogram(
        segment,
        x="Risk Segment",
        color="Risk Segment",
        title="Company Risk Segments"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Cluster Distribution")

    fig2 = px.pie(
        segment,
        names="Risk Segment",
        title="Risk Segment Share"
    )

    st.plotly_chart(fig2, use_container_width=True)

    csv = segment.to_csv(index=False)

    st.download_button(
        "⬇ Download Segmentation",
        csv,
        file_name="company_segments.csv",
        mime="text/csv"
    )