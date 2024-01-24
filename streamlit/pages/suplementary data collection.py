import streamlit as st
import pandas as pd
import joblib
from sklearn.metrics import accuracy_score

from joblib import load

model = load('isolationforest.joblib')

# Function to preprocess and predict
def predict(df):
    df = df.rename(columns={
    'Network bytes': '_source_network_bytes',
    'Destination Port': '_source_destination_port',
    'Source Port': '_source_source_port',
    'HTTP': 'udp',
    'TCP': 'tcp'
    })

    X_test = df

    non_numeric_cols = X_test.select_dtypes(include=['object']).columns

    # Drop or encode non-numeric columns
    X_test = X_test.drop(columns=non_numeric_cols)
    X_test = X_test.drop(columns=['No.', 'predicted_label','predicted_label_isolationforest', 'Unnamed: 0'])
    X_test.head(5)
    
    st.write('Data for testing')
    st.dataframe(X_test)
    # Predict
    y_pred = model.predict(X_test)
    
    # Add predictions to DataFrame
    df['predicted_label'] = y_pred
    
    return df

# Main function for your Streamlit app
def main():
    st.title("My Streamlit App")
    
    # Display DataFrame
    st.header("DataFrame")
    df = pd.read_csv('./data/generateddata.csv')
    
    # st.dataframe(df)
    
    # Predict and display results
    df = predict(df)
    st.header("Predictions")
    st.dataframe(df)
    
    # Display images
    st.header("Kubernetes Cluster")
    st.image('path_to_your_kubernetes_image.png')
    
    st.header("JMeter Test Project")
    st.image('path_to_your_jmeter_image.png')

# Run the app
if __name__ == "__main__":
    main()