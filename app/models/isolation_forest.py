from sklearn.ensemble import IsolationForest


def run_isolation_forest(
    df,
    features,
    contamination=0.03,
    random_state=42,
):

    model = IsolationForest(
        contamination=contamination,
        random_state=random_state
    )

    X = df[features].dropna()

    prediction = model.fit_predict(X)

    score = model.decision_function(X)

    result = df.loc[X.index].copy()

    result["Anomaly"] = prediction

    result["Anomaly Score"] = score

    return result