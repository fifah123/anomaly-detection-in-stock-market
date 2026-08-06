import streamlit as st

from app.data.downloader import load_stock_data
from app.features.technical import generate_features

from app.models.isolation_forest import run_isolation_forest
from app.models.lof import run_lof

from app.visualization.anomaly import anomaly_price_chart

st.title("🚨 Stock Market Anomaly Detection")

ticker = st.text_input(
    "Ticker",
    "AAPL"
)

model_name = st.selectbox(
    "Detection Model",
    [
        "Isolation Forest",
        "Local Outlier Factor"
    ]
)

contamination = st.slider(
    "Contamination",
    0.01,
    0.20,
    0.03,
    0.01
)

if st.button("Run Detection", use_container_width=True):

    df = load_stock_data(
        ticker,
        "2023-01-01",
        None
    )

    df = generate_features(df)

    features = [
        "Daily Return",
        "Volatility",
        "RSI",
        "MACD",
        "CCI",
        "ADX",
        "Volume"
    ]

    if model_name == "Isolation Forest":

        result = run_isolation_forest(
            df,
            features,
            contamination
        )

    else:

        result = run_lof(
            df,
            features,
            contamination
        )

    anomalies = result[result["Anomaly"] == -1]

    normal = result[result["Anomaly"] == 1]

    st.subheader("Detection Summary")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Total Records", len(result))

    c2.metric("Normal", len(normal))

    c3.metric("Anomalies", len(anomalies))

    c4.metric(
        "Anomaly %",
        f"{len(anomalies)/len(result)*100:.2f}%"
    )

    st.divider()

    st.plotly_chart(
        anomaly_price_chart(result),
        use_container_width=True
    )

    st.divider()

    st.subheader("Detected Anomalies")

    st.dataframe(
        anomalies,
        use_container_width=True
    )

    st.download_button(
        "Download Result",
        result.to_csv(index=False),
        "anomaly_result.csv",
        "text/csv"
    )