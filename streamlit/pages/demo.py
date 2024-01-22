import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import time


# Load the model
model = joblib.load('./model.pkl')

# Load your data
data = pd.read_csv('./data/test_data.csv')

benign = data[data['label'] == 0]
malicious = data[data['label'] == 1]

# Keep 20% of the benign data
benign_sample = benign.sample(frac=0.07, random_state=1)

# Concatenate the benign sample and the malicious data
data = pd.concat([benign_sample, malicious])

st.text("This is not a test")


# Ensure the order of columns matches the order of features in the trained model
data = data[model.feature_names_in_]

# Function to highlight malicious
def highlight_malicious(val):
    color = 'red' if val == '1' else 'green'
    return 'background-color: %s' % color

# Create a placeholder for the table
table_placeholder = st.empty()

# Number of rows to display at a time
num_rows = 1

# Update the table in the placeholder
for i in range(len(data)):
    # Make prediction for the current row
    if 'prediction' in data.columns:
        # Make prediction for the current row
        prediction = model.predict(data[i:i+1].drop(columns=['prediction']))
    else:
        # Make prediction for the current row
        prediction = model.predict(data[i:i+1])
    
    # Add prediction to the data
    data.loc[i, 'prediction'] = prediction[0]
    
    # Update the table in the placeholder
    table_placeholder.write(data[:i+1].style.applymap(highlight_malicious))
    
    # Wait for 2 seconds before updating the table with the next row
    time.sleep(0.5)