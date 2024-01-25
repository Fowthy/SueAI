import streamlit as st
from st_pages import add_indentation
add_indentation()

st.write("""
         Throughout the course of the research project, a comprehensive exploration of both unsupervised as supervised models have been done, allowed by the labelled dataset provided for this research.  
         From working with these various models, distinct advantages and disadvantages for these two techniques have been discovered.""")
st.write("""Supervised learning is good at predicting malicious records similar to known malicious attacks from the past, but it has limitations, it can only predict based on patterns it has seen before, and labeling the data takes a lot of time and can introduce bias due to bad labeling or poorly defined environments for obtaining the data.""")
st.write("""
         Unsupervised learning is effective in understanding normal patterns in the data without needing predefined labels, it can spot anomalies by recognizing deviations from what's considered the norm (benign).  
         This makes unsupervised learning a better fit for this project's problem statement and solution, as it doesn't rely on exhaustive manual labeling and adapts to changes in the environment automatically.""")
st.write("""These statements can be corroborated by providing supervised learning models with new data from a slightly altered environment, as the hard rules the supervised models set will not be able to properly handle these changes, while a supervised model can deal with them more effectively.  
         Note however, that both types of models are trained based on the interactions within and around the given environment, and changing too much (via updates or restructures), or using the trained model for a different cluster will most likely lead to bad results and the model will have to be retrained.""")