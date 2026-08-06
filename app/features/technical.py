import numpy as np
import pandas as pd

from ta.trend import (
    SMAIndicator,
    MACD,
)

from ta.momentum import RSIIndicator

from ta.volatility import (
    BollingerBands,
)
from ta.trend import EMAIndicator
from ta.trend import ADXIndicator
from ta.trend import CCIIndicator

from ta.momentum import StochasticOscillator

from ta.volume import OnBalanceVolumeIndicator

from ta.volatility import AverageTrueRange

def generate_features(df: pd.DataFrame):

    df = df.copy()

    # ==========================
    # Returns
    # ==========================

    df["Daily Return"] = df["Close"].pct_change()

    df["Log Return"] = np.log(
        df["Close"] / df["Close"].shift(1)
    )

    # ==========================
    # Moving Average
    # ==========================

    df["MA20"] = SMAIndicator(
        close=df["Close"],
        window=20
    ).sma_indicator()

    df["MA50"] = SMAIndicator(
        close=df["Close"],
        window=50
    ).sma_indicator()

    df["MA200"] = SMAIndicator(
        close=df["Close"],
        window=200
    ).sma_indicator()

    # ==========================
    # RSI
    # ==========================

    df["RSI"] = RSIIndicator(
        close=df["Close"],
        window=14
    ).rsi()

    # ==========================
    # MACD
    # ==========================

    macd = MACD(
        close=df["Close"]
    )

    df["MACD"] = macd.macd()

    df["MACD Signal"] = macd.macd_signal()

    df["MACD Histogram"] = macd.macd_diff()

    # ==========================
    # Bollinger Bands
    # ==========================

    bb = BollingerBands(
        close=df["Close"],
        window=20,
        window_dev=2
    )

    df["BB Upper"] = bb.bollinger_hband()

    df["BB Middle"] = bb.bollinger_mavg()

    df["BB Lower"] = bb.bollinger_lband()

    df["BB Width"] = bb.bollinger_wband()

    # ==========================
    # Rolling Volatility
    # ==========================

    df["Volatility"] = (
        df["Daily Return"]
        .rolling(20)
        .std()
    )

    # EMA

    df["EMA20"] = EMAIndicator(
        close=df["Close"],
        window=20
    ).ema_indicator()

    # ATR

    df["ATR"] = AverageTrueRange(
        high=df["High"],
        low=df["Low"],
        close=df["Close"]
    ).average_true_range()

    # ADX

    adx = ADXIndicator(
        high=df["High"],
        low=df["Low"],
        close=df["Close"]
    )

    df["ADX"] = adx.adx()

    # CCI

    cci = CCIIndicator(
        high=df["High"],
        low=df["Low"],
        close=df["Close"]
    )

    df["CCI"] = cci.cci()

    # OBV

    obv = OnBalanceVolumeIndicator(
        close=df["Close"],
        volume=df["Volume"]
    )

    df["OBV"] = obv.on_balance_volume()

    # Stochastic

    stoch = StochasticOscillator(
        high=df["High"],
        low=df["Low"],
        close=df["Close"]
    )

    df["Stochastic"] = stoch.stoch()

    return df