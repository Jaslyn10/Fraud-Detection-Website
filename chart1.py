import pickle as pkl

import streamlit as st

with open("./graphs/chart1.pkl", "rb") as file:
    fig = pkl.load(file)

st.write("## Fraud vs Non Fraud Distribution")
st.text(" ")
st.text(" ")
st.text(" ")
st.plotly_chart(fig)
