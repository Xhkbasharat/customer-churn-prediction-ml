import pandas as pd

from src.preprocess import preprocess_data


def test_removes_customer_id():
    df = pd.DataFrame({
        "customerID": ["C001"],
        "tenure": [12],
        "Churn": ["Yes"]
    })

    result = preprocess_data(df)

    assert "customerID" not in result.columns


def test_converts_churn_labels():
    df = pd.DataFrame({
        "tenure": [12, 24],
        "Churn": ["Yes", "No"]
    })

    result = preprocess_data(df)

    assert result["Churn"].tolist() == [1, 0]


def test_converts_total_charges():
    df = pd.DataFrame({
        "TotalCharges": ["100.5", "200.0"],
        "Churn": ["Yes", "No"]
    })

    result = preprocess_data(df)

    assert result["TotalCharges"].dtype != object


def test_returns_dataframe():
    df = pd.DataFrame({
        "tenure": [12],
        "Churn": ["Yes"]
    })

    result = preprocess_data(df)

    assert isinstance(result, pd.DataFrame)
