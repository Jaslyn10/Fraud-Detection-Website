import streamlit as st

pg = st.navigation(
    {
        "Fraud Detection": [st.Page("predict.py", title="Prediction")],
        "Data Visualization": [
            st.Page("chart1.py", title="Fraud vs Non Fraud"),
            st.Page("chart2.py", title="Gender Distribution"),
            st.Page("chart3.py", title="Top Fraud Categories"),
            st.Page("chart4.py", title="Hourly Fraud Distribution"),
            st.Page("chart5.py", title="Top Fraud Job Categories"),
            st.Page("chart6.py", title="Transaction Amount Distribution"),
            st.Page("chart7.py", title="Map View"),
        ],
    }
)
st.set_page_config(page_title="App", layout="wide")
pg.run()
