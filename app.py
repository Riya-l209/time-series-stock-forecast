# app.py
import streamlit as st
from PIL import Image

st.set_page_config(page_title="Stock Forecasting", layout="centered")

st.title("📈 Time Series Stock Forecasting – AAPL")
st.markdown("This project forecasts AAPL stock prices using ARIMA, Prophet, and LSTM models.")

st.subheader("🔮 Prophet Forecast")
prophet_img = Image.open("reports/prophet_forecast.png")
st.image(prophet_img, caption="Prophet Forecast for AAPL", use_column_width=True)

st.subheader("🧠 LSTM Forecast")
lstm_img = Image.open("reports/lstm_forecast.png")
st.image(lstm_img, caption="LSTM Forecast for AAPL", use_column_width=True)

st.markdown("---")
st.write("Developed by [Riya Bhardwaj] · July 2025")
