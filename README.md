# 🏡 Smart Real Estate Price Predictor

A Machine Learning web application that predicts Bengaluru
property prices based on location, area, number of bedrooms,
and bathrooms.

## 🚀 Features

- Predict property prices using Machine Learning.
- Enter property location and area in square feet.
- Specify BHK and number of bathrooms.
- Display estimated prices in Indian lakhs.
- Simple and user-friendly web interface.

## 🛠️ Technologies Used

- Python
- Flask
- Pandas
- NumPy
- Scikit-learn
- HTML
- CSS
- Jupyter Notebook

## 🤖 Machine Learning

- Dataset: Bengaluru House Price Data
- Models evaluated: Linear Regression and Random Forest
- Selected model: Random Forest Regressor
- Evaluation metrics: MAE and R² Score

Model performance on the test set:
- MAE: 36.75 lakhs
- R² Score: 0.5044

These metrics indicate that predictions have limitations
and should not be treated as guaranteed market prices.

## 📂 Project Structure

Smart-Real-Estate-Price-Predictor/
├── app/
│   ├── app.py
│   ├── templates/
│   │   └── index.html
│   └── static/
├── data/
├── model/
│   └── house_price_model.pkl
├── notebooks/
│   └── 01_data_analysis.ipynb
├── src/
├── .gitignore
├── README.md
└── requirements.txt

## ⚙️ Installation

1. Clone this repository.
2. Install the required packages:

   pip install -r requirements.txt

3. Run the application:

   python app/app.py

4. Open http://127.0.0.1:5000 in your browser.

## ⚠️ Disclaimer

This application provides experimental price estimates
based on historical Bengaluru housing data. Predictions
may differ significantly from actual market prices.