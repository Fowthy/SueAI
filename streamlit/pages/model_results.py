import streamlit as st
import pandas as pd
from st_pages import add_indentation
add_indentation()

model_results = pd.DataFrame({
    'Model': ["Probabilistic State Machine*", "TranAD**", "One-Class SVM", "Decision Tree", "Isolation Forest", "ANN"],
    'Recall': ["N/A", "0.99", "0.80", "0.89", "0.75", "0.85"],
    'Precision': ["N/A", "0.81", "0.91", "0.96", "0.64", "0.91"],
    'F1': ["0.98", "0.90", "0.83", "0.93", "0.67", "0.88"],
    'Accuracy': ["99%", "98%", "86%", "96%", "91%", "90%"],
    'Unsupervised': [True, True, True, False, True, True]
})
st.dataframe(model_results, width=1000)

st.write("""
        *Probabilistic State Machines results were obtained from a third party’s research paper, based on the same dataset  
        **TranAD was trained on ~1% of dataset with no parameter tuning
        """)