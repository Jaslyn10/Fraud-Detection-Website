import pickle as pkl

import streamlit as st

with open("./graphs/chart2.pkl", "rb") as file:
    fig = pkl.load(file)

st.write("## Gender Distribution of Fraud Transactions")
st.text(" ")
st.text(" ")
st.text(" ")
st.plotly_chart(fig)
