import plotly.graph_objects as go


def anomaly_price_chart(df):

    fig = go.Figure()

    normal = df[df["Anomaly"] == 1]

    anomaly = df[df["Anomaly"] == -1]

    fig.add_scatter(
        x=normal["Date"],
        y=normal["Close"],
        mode="lines",
        name="Close Price"
    )

    fig.add_scatter(
        x=anomaly["Date"],
        y=anomaly["Close"],
        mode="markers",
        marker=dict(
            size=10,
            color="red"
        ),
        name="Anomaly"
    )

    fig.update_layout(
        title="Detected Price Anomalies",
        template="plotly_dark",
        height=550,
        xaxis_title="Date",
        yaxis_title="Price"
    )

    return fig