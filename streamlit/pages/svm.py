import streamlit as st
from st_pages import add_indentation
add_indentation()

st.write("""
        One-class SVM is a Support Vector Machine used for unsupervised learning, it is called One-class as it will classify the data into a single classification cluster, thereby finding any outliers/anomalies by the data points not covered within the single classification cluster (also referred to as novelty detection).
""")

