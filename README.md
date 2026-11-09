Customer Churn Prediction

A machine learning project that predicts whether a customer is likely to leave a subscription service using Python and Logistic Regression.

Features

- Customer churn prediction
- Customer data preprocessing
- Logistic Regression classification
- Churn probability calculation
- Interactive Streamlit dashboard
- Automated testing

Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Joblib
- Pytest

Project Structure

customer-churn-prediction-ml/
├── app.py
├── data/
│   └── customer_churn.csv
├── models/
│   └── .gitkeep
├── src/
│   ├── __init__.py
│   ├── preprocess.py
│   ├── train.py
│   └── predict.py
├── tests/
│   ├── __init__.py
│   └── test_model.py
├── .github/workflows/
│   └── tests.yml
├── requirements.txt
├── Dockerfile
├── runtime.txt
├── .gitignore
└── LICENSE

Installation

Clone the repository:

git clone https://github.com/Xhkbasharat/customer-churn-prediction-ml.git
cd customer-churn-prediction-ml

Install the dependencies:

pip install -r requirements.txt

Train the Model

python -m src.train

Run the Application

streamlit run app.py

Run Tests

python -m pytest

Dataset

The project uses customer information such as:

- Gender
- Senior citizen status
- Contract type
- Internet service
- Monthly charges
- Customer tenure

The current sample dataset is for demonstration only. A larger, representative dataset is needed for reliable evaluation.

Future Improvements

- Use a larger dataset
- Compare multiple machine learning algorithms
- Improve prediction performance
- Add customer analytics charts
- Deploy the application online

Disclaimer

This project is for educational purposes. Predictions are estimates and should not be treated as definitive business decisions.

Author

Xhkbasharat

GitHub: https://github.com/Xhkbasharat

License

MIT License
