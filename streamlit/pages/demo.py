import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import time
import numpy as np
from st_pages import add_indentation
add_indentation()


# Load your data
data = pd.read_csv('data/test_data.csv')

benign = data[data['label'] == 0]
malicious = data[data['label'] == 1]

# Keep 20% of the benign data
benign_sample = benign.sample(frac=0.01, random_state=1)

# Concatenate the benign sample and the malicious data
data = pd.concat([benign_sample, malicious])

data.dropna()

# Add a 'prediction' column with 20% malicious (1) and 80% benign (0) entries
data['prediction'] = np.random.choice([0, 1], size=len(data), p=[0.8, 0.2])

# Function to highlight malicious
def highlight_malicious(row):
    color = 'red' if row['prediction'] == 1 else 'green'
    return ['background-color: %s' % color]*len(row)

# Create a placeholder for the table
table_placeholder = st.empty()

# Number of rows to display at a time
num_rows = 20

# Update the table in the placeholder
for i in range(0, len(data), num_rows):
    # Display the rows based on the 'prediction' column
    table_placeholder.write(data[i:min(i + num_rows, len(data))].style.apply(highlight_malicious, axis=1))
    
    # Wait for 2 seconds before updating the table with the next row
    time.sleep(1)
