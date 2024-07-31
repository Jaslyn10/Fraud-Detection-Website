import pickle as pkl

import streamlit as st

with open("./graphs/chart5.pkl", "rb") as file:
    fig = pkl.load(file)

st.write("## Jobs with the highest Fraud transactions")
st.plotly_chart(fig)
