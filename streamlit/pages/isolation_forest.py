import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from st_pages import add_indentation
add_indentation()


st.header("Isolation Forest Model Testing")

# Description of the model
st.write("""
        Isolation Forest is a type of machine learning algorithm used for detecting unusual data points, known as anomalies. 
        It works well with large datasets. The algorithm operates by isolating data points and assigning them a score based on how easily they were isolated. 
        The easier it is to isolate a data point, the more likely it is to be an anomaly.
""")



# Predict and display results
st.header("Predictions")

classification_report = pd.DataFrame({
    'Precision': [0.72, 0.68],
    'Recall': [0.65, 0.75],
    'F1-Score': [0.68, 0.71],
    'Support': [30782, 30812]
}, index=['-1', '1'])

st.dataframe(classification_report)
st.write("Accuracy Score: 0.699126538299185")

# Display confusion matrix
st.header("Confusion Matrix")
st.image('./streamlit/media/isolationforestmatrix.png')

# Display SHAP values
st.header("SHAP Values")
st.image("./streamlit/media/isolationforestshap.png")