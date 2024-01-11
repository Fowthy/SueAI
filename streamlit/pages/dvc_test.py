import streamlit as st
import pandas as pd

df = pd.read_csv("data/test_data.csv")
st.dataframe(df)