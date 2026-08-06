import streamlit as st

from datetime import date

from app.data.downloader import load_stock_data
from app.visualization.charts import (
    candlestick_chart,
    volume_chart
)

st.title("📊 Asset Explorer")

st.markdown(
    """
Explore historical stock prices before running anomaly detection.
"""
)

market = st.selectbox(
    "Market",
    [
        "US",
        "Indonesia"
    ]
)

if market == "US":

    ticker = st.selectbox(
        "Ticker",
        [
            "AAPL",
            "MSFT",
            "NVDA",
            "GOOGL",
            "AMZN",
            "META",
            "TSLA"
        ]
    )

else:

    ticker = st.selectbox(
        "Ticker",
        [
            "BBCA.JK",
            "BBRI.JK",
            "BMRI.JK",
            "TLKM.JK",
            "ASII.JK"
        ]
    )

col1, col2 = st.columns(2)

with col1:

    start_date = st.date_input(
        "Start Date",
        date(2023, 1, 1)
    )

with col2:

    end_date = st.date_input(
        "End Date",
        date.today()
    )

if st.button("Load Data", use_container_width=True):

    with st.spinner("Downloading market data..."):

        df = load_stock_data(
            ticker,
            start_date,
            end_date
        )

    if df.empty:

        st.error("No data found.")

    else:

        st.success(f"{len(df)} records loaded.")

        latest = df.iloc[-1]

        c1, c2, c3, c4 = st.columns(4)

        c1.metric(
            "Latest Close",
            f"${latest['Close']:.2f}" if market == "US" else f"Rp {latest['Close']:,.0f}"
        )

        c2.metric(
            "Open",
            f"{latest['Open']:.2f}"
        )

        c3.metric(
            "High",
            f"{latest['High']:.2f}"
        )

        c4.metric(
            "Low",
            f"{latest['Low']:.2f}"
        )

        st.plotly_chart(
            candlestick_chart(df),
            use_container_width=True
        )

        st.plotly_chart(
            volume_chart(df),
            use_container_width=True
        )

        st.subheader("Historical Data")

        st.dataframe(
            df,
            use_container_width=True
        )