import pandas as pd


def preprocess_data(df):
    """Clean customer churn dataset."""

    df = df.copy()

    # Remove customer ID if present
    if "customerID" in df.columns:
        df = df.drop(columns=["customerID"])

    # Convert TotalCharges to numeric
    if "TotalCharges" in df.columns:
        df["TotalCharges"] = pd.to_numeric(
            df["TotalCharges"], errors="coerce"
        )

    # Remove rows with missing values
    df = df.dropna()

    # Convert target labels
    if "Churn" in df.columns:
        df["Churn"] = df["Churn"].map({
            "Yes": 1,
            "No": 0
        })

    return df
