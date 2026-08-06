from sklearn.neighbors import LocalOutlierFactor


def run_lof(
    df,
    features,
    contamination=0.03,
    n_neighbors=20,
):

    model = LocalOutlierFactor(
        contamination=contamination,
        n_neighbors=n_neighbors
    )

    X = df[features].dropna()

    prediction = model.fit_predict(X)

    result = df.loc[X.index].copy()

    result["Anomaly"] = prediction

    result["Anomaly Score"] = model.negative_outlier_factor_

    return result