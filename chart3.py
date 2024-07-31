import pickle as pkl

import streamlit as st

with open("./graphs/chart3.pkl", "rb") as file:
    fig = pkl.load(file)

st.write("## Categories with the most Fraud transactions")
st.text(" ")
st.text(" ")
st.plotly_chart(fig)
