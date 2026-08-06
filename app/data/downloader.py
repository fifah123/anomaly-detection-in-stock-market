import yfinance as yf
import streamlit as st


@st.cache_data(show_spinner=False)
def load_stock_data(
    ticker: str,
    start_date,
    end_date
):
    df = yf.download(
        ticker,
        start=start_date,
        end=end_date,
        progress=False,
        auto_adjust=True
    )

    # Flatten MultiIndex columns if present
    if hasattr(df.columns, "nlevels") and df.columns.nlevels > 1:
        df.columns = df.columns.get_level_values(0)

    df.reset_index(inplace=True)

    return df