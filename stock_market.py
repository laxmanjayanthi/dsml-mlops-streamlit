import yfinance as yf
import pandas as pd 
import streamlit as st  

msft = yf.Ticker('MSFT')

st.title('Stock Market App')
st.write("This is stock market pagesfdsd")
st.write(msft.history(period="1mo"))
