import pickle as pkl

import streamlit as st

with open("./graphs/chart6.pkl", "rb") as file:
    fig = pkl.load(file)

st.write("## Transaction Amount Distribution for each category")
st.plotly_chart(fig)
