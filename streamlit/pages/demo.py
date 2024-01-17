import streamlit as st
import pandas as pd
import numpy as np
from sklearn.externals import joblib

# Load the model
model = joblib.load('./streamlit/model.pkl')

# Load your data
data = pd.read_csv('./data/train_data.csv')

# Make predictions
predictions = model.predict(data)

# Add predictions to the data
data['prediction'] = predictions

# Function to highlight malicious
def highlight_malicious(s):
    return ['background-color: red' if v == 'malicious' else '' for v in s]

# Auto-scrolling table
for i in range(len(data)):
    st.write(data[i:i+1].style.apply(highlight_malicious, subset=['prediction']))
    st.table(data[i:i+1])
    st.empty()