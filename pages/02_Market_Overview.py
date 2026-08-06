import streamlit as st
from datetime import date

from app.data.downloader import load_stock_data
from app.features.technical import generate_features

from app.visualization.charts import (
    moving_average_chart,
    bollinger_chart,
    rsi_chart,
    macd_chart,
    cci_chart,
    adx_chart,
    volatility_chart,
)

st.title("📈 Market Overview & Technical Indicators")

ticker = st.text_input("Ticker", "AAPL")

col1, col2 = st.columns(2)

with col1:
    start = st.date_input("Start Date", date(2023, 1, 1))

with col2:
    end = st.date_input("End Date", date.today())

if st.button("Analyze", use_container_width=True):

    df = load_stock_data(ticker, start, end)

    if df.empty:
        st.error("No data found.")
        st.stop()

    df = generate_features(df)

    latest = df.iloc[-1]

    # ======================================================
    # Market Summary
    # ======================================================

    st.subheader("📊 Market Summary")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Close", f"{latest['Close']:.2f}")
    c2.metric("Daily Return", f"{latest['Daily Return']:.2%}")
    c3.metric("RSI", f"{latest['RSI']:.2f}")
    c4.metric("Volatility", f"{latest['Volatility']:.2%}")

    st.divider()

    # ======================================================
    # Price Analysis
    # ======================================================

    st.header("📈 Price Analysis")

    st.markdown("### Stock Price with Moving Averages (20, 50, 200)")
    st.plotly_chart(
        moving_average_chart(df),
        use_container_width=True
    )

    st.markdown("### Bollinger Bands")
    st.plotly_chart(
        bollinger_chart(df),
        use_container_width=True
    )

    st.divider()

    # ======================================================
    # Momentum Indicators
    # ======================================================

    st.header("📊 Momentum Indicators")

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("#### Relative Strength Index (RSI)")
        st.plotly_chart(
            rsi_chart(df),
            use_container_width=True
        )

        st.markdown("#### Commodity Channel Index (CCI)")
        st.plotly_chart(
            cci_chart(df),
            use_container_width=True
        )

        st.markdown("#### Rolling 20-Day Volatility")
        st.plotly_chart(
            volatility_chart(df),
            use_container_width=True
        )

    with col2:

        st.markdown("#### Moving Average Convergence Divergence (MACD)")
        st.plotly_chart(
            macd_chart(df),
            use_container_width=True
        )

        st.markdown("#### Average Directional Index (ADX)")
        st.plotly_chart(
            adx_chart(df),
            use_container_width=True
        )

    st.divider()

    # ======================================================
    # Feature Dataset
    # ======================================================

    st.header("📋 Engineered Feature Dataset")

    st.dataframe(
        df,
        use_container_width=True
    )