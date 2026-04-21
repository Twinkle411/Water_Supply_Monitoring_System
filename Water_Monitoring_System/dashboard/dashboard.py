import streamlit as st
import pandas as pd

# LOGIN
username = st.text_input("Username")
password = st.text_input("Password", type="password")

if username != "admin" or password != "admin123":
    st.warning("Enter valid login details")
    st.stop()

# LOAD DATA
df = pd.read_csv("data/brisbane_water_quality.csv")


df.columns = df.columns.str.lower()

# DASHBOARD
st.title("Water Supply Monitoring System")

st.subheader("Water Data")
st.dataframe(df)

# CHARTS
st.subheader("pH Chart")
if "ph" in df.columns:
    st.line_chart(df["ph"])
else:
    st.error("Column 'ph' not found")

st.subheader("Turbidity Chart")
if "turbidity" in df.columns:
    st.bar_chart(df["turbidity"])
else:
    st.error("Column 'turbidity' not found")