import pickle as pkl

import streamlit as st

with open("./graphs/chart4.pkl", "rb") as file:
    fig = pkl.load(file)

st.write("## Hourly Distribution of Fraud Transactions")
st.text(" ")
st.text(" ")
st.plotly_chart(fig)
