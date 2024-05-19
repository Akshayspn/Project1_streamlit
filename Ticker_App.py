import yfinance as yf
import streamlit as st
import pandas as pd

st.write("My streamlit app to show TICKR history")
ts=str(input("Enter ticker symbol"))

td=yf.Ticker(ts)

tdf=td.history(period='1d', start='2010-01-01', end='2020-01-01')

st.line_chart(tdf.Close)
st.line_chart(tdf.Volume)