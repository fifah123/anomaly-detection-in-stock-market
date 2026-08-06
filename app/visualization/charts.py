import plotly.graph_objects as go


def candlestick_chart(df):

    fig = go.Figure()

    fig.add_trace(
        go.Candlestick(
            x=df["Date"],
            open=df["Open"],
            high=df["High"],
            low=df["Low"],
            close=df["Close"],
            name="Price"
        )
    )

    fig.update_layout(
        height=600,
        template="plotly_dark",
        xaxis_title="Date",
        yaxis_title="Price",
        xaxis_rangeslider_visible=False
    )

    return fig


def volume_chart(df):

    fig = go.Figure()

    fig.add_bar(
        x=df["Date"],
        y=df["Volume"],
        name="Volume"
    )

    fig.update_layout(
        height=300,
        template="plotly_dark",
        xaxis_title="Date",
        yaxis_title="Volume"
    )

    return fig

def moving_average_chart(df):

    fig = go.Figure()

    fig.add_scatter(
        x=df["Date"],
        y=df["Close"],
        name="Close"
    )

    fig.add_scatter(
        x=df["Date"],
        y=df["MA20"],
        name="MA20"
    )

    fig.add_scatter(
        x=df["Date"],
        y=df["MA50"],
        name="MA50"
    )

    fig.add_scatter(
        x=df["Date"],
        y=df["MA200"],
        name="MA200"
    )

    fig.update_layout(
        template="plotly_dark",
        height=500
    )

    return fig

def rsi_chart(df):

    fig = go.Figure()

    fig.add_scatter(
        x=df["Date"],
        y=df["RSI"],
        name="RSI"
    )

    fig.add_hline(y=70)

    fig.add_hline(y=30)

    fig.update_layout(
        template="plotly_dark",
        height=300
    )

    return fig

def macd_chart(df):

    fig = go.Figure()

    fig.add_scatter(
        x=df["Date"],
        y=df["MACD"],
        name="MACD"
    )

    fig.add_scatter(
        x=df["Date"],
        y=df["MACD Signal"],
        name="Signal"
    )

    fig.update_layout(
        template="plotly_dark",
        height=300
    )

    return fig

def bollinger_chart(df):

    fig = go.Figure()

    fig.add_scatter(
        x=df["Date"],
        y=df["Close"],
        name="Close"
    )

    fig.add_scatter(
        x=df["Date"],
        y=df["BB Upper"],
        name="Upper"
    )

    fig.add_scatter(
        x=df["Date"],
        y=df["BB Middle"],
        name="Middle"
    )

    fig.add_scatter(
        x=df["Date"],
        y=df["BB Lower"],
        name="Lower"
    )

    fig.update_layout(
        template="plotly_dark",
        height=500
    )

    return fig

def cci_chart(df):

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=df["Date"],
            y=df["CCI"],
            mode="lines",
            name="CCI",
            line=dict(width=2)
        )
    )

    # Overbought / Oversold Levels
    fig.add_hline(
        y=100,
        line_dash="dash",
        line_color="green",
        annotation_text="+100"
    )

    fig.add_hline(
        y=-100,
        line_dash="dash",
        line_color="red",
        annotation_text="-100"
    )

    fig.update_layout(
        title="Commodity Channel Index (CCI)",
        template="plotly_dark",
        height=300,
        hovermode="x unified",
        xaxis_title="Date",
        yaxis_title="CCI"
    )

    return fig

def adx_chart(df):

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=df["Date"],
            y=df["ADX"],
            mode="lines",
            name="ADX",
            line=dict(width=2)
        )
    )

    if "DMP" in df.columns:
        fig.add_trace(
            go.Scatter(
                x=df["Date"],
                y=df["DMP"],
                mode="lines",
                name="+DI"
            )
        )

    if "DMN" in df.columns:
        fig.add_trace(
            go.Scatter(
                x=df["Date"],
                y=df["DMN"],
                mode="lines",
                name="-DI"
            )
        )

    fig.add_hline(
        y=25,
        line_dash="dash",
        annotation_text="Strong Trend"
    )

    fig.update_layout(
        title="Average Directional Index (ADX)",
        template="plotly_dark",
        height=350,
        hovermode="x unified",
        xaxis_title="Date",
        yaxis_title="ADX"
    )

    return fig

def volatility_chart(df):

    fig = go.Figure()

    fig.add_scatter(
        x=df["Date"],
        y=df["Volatility"],
        name="Volatility"
    )

    fig.update_layout(
        template="plotly_dark",
        height=300,
        yaxis_title="Annualized Volatility"
    )

    return fig