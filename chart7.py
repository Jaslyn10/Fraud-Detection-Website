import pickle as pkl

import streamlit as st

with open("./graphs/chart7.pkl", "rb") as file:
    fig = pkl.load(file)

st.write("## Map View of Fraud Transactions")
st.plotly_chart(fig)
