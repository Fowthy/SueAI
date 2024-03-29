import streamlit as st
import random
import pandas as pd
import numpy as np
from st_pages import Page, Section, add_indentation, show_pages, hide_pages

def main():
    # Page routing configuration
    add_indentation()
    show_pages(
    [
        Page("./streamlit/app.py", "Time Waster", in_section=False),
        Page("./streamlit/pages/sue.py", "SUE", in_section=False),
        Page("./streamlit/pages/problem.py", "Problem", in_section=False),
        Section("Data"),
        Page("./streamlit/pages/preprocessing.py", "Pre-processing", in_section=True),
        Page("./streamlit/pages/visualization.py", "Data visualization", in_section=True),
        Page("./streamlit/pages/dvc.py", "DVC", in_section=True),
        Page("./streamlit/pages/suplementary_data_collection.py", "Suplementary Data Collection", in_section=True),
        Section("Models"),
        Page("./streamlit/pages/isolation_forest.py", "Isolation Forest", in_section=True),
        Page("./streamlit/pages/ann.py", "Neural Networks", in_section=True),
        Page("./streamlit/pages/state_machines.py", "State machines", in_section=True),
        Page("./streamlit/pages/decision_trees.py", "Decision Trees", in_section=True),
        Page("./streamlit/pages/svm.py", "One-class SVM", in_section=True),
        Page("./streamlit/pages/transformers.py", "TranAD", in_section=True),
        Page("./streamlit/pages/ethics.py", "Ethics", in_section=False),
        Page("./streamlit/pages/demo.py", "Demo", in_section=False),
        Section("Findings"),
        Page("./streamlit/pages/model_results.py", "Model Results", in_section=True),
        Page("./streamlit/pages/labelled_learning_findings.py", "Supervised Vs Unsupervised", in_section=True),
        Page("./streamlit/pages/future_work.py", "Future Work", in_section=False),
        Page("./streamlit/pages/debug.py", "Debug", in_section=False),
    ])

    st.title("Number Guessing Game")

    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)

    # Initialize the game
    if 'number_to_guess' not in st.session_state:
        st.session_state['number_to_guess'] = number_to_guess
        st.session_state['guess'] = None

    st.write("Guess a number between 1 and 100.")

    st.session_state['guess'] = st.number_input("Enter your guess", min_value=1, max_value=100, value=1)

    if st.session_state['guess'] is not None:
        if st.session_state['guess'] < st.session_state['number_to_guess']:
            st.write("Too low! Try a higher number.")
        elif st.session_state['guess'] > st.session_state['number_to_guess']:
            st.write("Too high! Try a lower number.")
        else:
            st.write("Congratulations! You guessed the number.")
            st.session_state['number_to_guess'] = random.randint(1, 100)
            st.session_state['guess'] = None  

if __name__ == "__main__":
    main()