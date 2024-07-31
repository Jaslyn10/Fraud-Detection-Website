import pickle as pkl

import streamlit as st

with open("./models/model_randforest.pkl", "rb") as file:
    model = pkl.load(file)

with open("./testset.pkl", "rb") as file:
    testset = pkl.load(file)

st.title("Online Payment Fraud Detection")
st.write("")
st.write("")
st.write("##### Pick one of the transactions below to predict")
st.write("")

choice = st.radio(
    "Pick one",
    [
        "$60.05, Misc POS, 37 years, 12 AM, Zip: 32780, Latitude: 28.5697, Longitude: -80.8191",
        "$105.1, Kids/Pets, 40 years, 3 PM, Zip: 38922, Latitude: 33.9215, Longitude: -89.6782",
        "$780.52, Misc Net, 66 years, 11 PM, Zip: 53803, Latitude: 42.461127, Longitude: -91.147148",
        "$4.32, Shopping POS, 69 years, 1 AM, Zip: 46702, Latitude: 40.8618, Longitude: -85.6067",
        "$868.09, Shopping POS, 65 years, 10 PM, Zip: 38668, Latitude: 34.6323, Longitude: -89.8855",
    ],
    index=None,
)
st.write("")
if st.button("Predict"):
    if (
        choice
        == "$60.05, Misc POS, 37 years, 12 AM, Zip: 32780, Latitude: 28.5697, Longitude: -80.8191"
    ):
        predicted = model.predict([testset[0]])

    if (
        choice
        == "$105.1, Kids/Pets, 40 years, 3 PM, Zip: 38922, Latitude: 33.9215, Longitude: -89.6782"
    ):
        predicted = model.predict([testset[1]])

    if (
        choice
        == "$780.52, Misc Net, 66 years, 11 PM, Zip: 53803, Latitude: 42.461127, Longitude: -91.147148"
    ):
        predicted = model.predict([testset[2]])

    if (
        choice
        == "$4.32, Shopping POS, 69 years, 1 AM, Zip: 46702, Latitude: 40.8618, Longitude: -85.6067"
    ):
        predicted = model.predict([testset[3]])

    if (
        choice
        == "$868.09, Shopping POS, 65 years, 10 PM, Zip: 38668, Latitude: 34.6323, Longitude: -89.8855"
    ):
        predicted = model.predict([testset[4]])

    if predicted == 0:
        st.success("Not a fraudulent transaction")
    if predicted == 1:
        st.error("Fraudulent transaction")
