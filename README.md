# 📈 Time Series Stock Forecasting – AAPL

> **Project Type**: Data Science | Time Series Forecasting | Deep Learning  
> **Tools Used**: Python · ARIMA · Prophet · LSTM · TensorFlow · Matplotlib · Streamlit  
> **Deployed App**: 👉 [Click here to view live demo](https://time-series-stock-forecast-d5nxqfrbgyvxuzenhnaqyb.streamlit.app/)

---

## 📌 Project Objective

The objective of this project is to forecast the **AAPL (Apple Inc.) stock prices** using various **time series forecasting techniques**, including classical statistical models and modern deep learning models.  
This project demonstrates hands-on skills in working with real stock market data, preprocessing, model training, evaluation, and deployment of results through a live web application.

---

## 🧠 Models Used

| Model   | Description                                                                 |
|---------|-----------------------------------------------------------------------------|
| **ARIMA**  | Autoregressive Integrated Moving Average – good for linear patterns     |
| **Prophet** | Developed by Facebook – excellent for handling seasonality and holidays |
| **LSTM**   | Recurrent Neural Network – captures long-term dependencies in sequences |

---

## 📊 Results (Visual Forecasts)

- **Prophet** captured trend + seasonality effectively
- **LSTM** modeled non-linear and volatile behavior more dynamically
- Forecast charts are available in the [Streamlit app](https://time-series-stock-forecast-d5nxqfrbgyvxuzenhnaqyb.streamlit.app/)
  
---

## 🗂️ Project Structure

```bash
time-series-stock-forecast/
├── app.py                    # Streamlit web app
├── data/
│   └── stock_data.csv        # Raw historical stock prices
├── reports/
│   ├── prophet_forecast.png  # Prophet forecast chart
│   └── lstm_forecast.png     # LSTM forecast chart
├── notebooks/
│   └── Time_Series_Stock_Forecasting.ipynb  # Full working notebook
├── README.md                 # This file
```
📚 Topics Covered

-Time Series Analysis
-Stock Market Data Processing
-ARIMA and SARIMA Modeling
-Facebook Prophet Forecasting
-LSTM with TensorFlow/Keras
-Data Normalization and Scaling
-Model Evaluation and Comparison
-Deployment with Streamlit Cloud

⚙️ Tech Stack

-Languages & Libraries: Python, Pandas, NumPy, Matplotlib, Seaborn, Plotly
-Modeling: Statsmodels, Prophet, TensorFlow/Keras
-Visualization & Deployment: Streamlit, PIL

🚀 How to Run This Project
Option 1: View the live demo
👉 Streamlit App

Option 2: Run locally
```
git clone https://github.com/your-username/time-series-stock-forecast.git
cd time-series-stock-forecast
pip install -r requirements.txt
streamlit run app.py
```

👩‍💻 Developed By
Riya Bhardwaj
Data Science & AI Enthusiast 
