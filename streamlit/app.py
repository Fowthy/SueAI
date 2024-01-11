# import streamlit as st
# import pandas as pd
# import numpy as np

# # Function to load data
# def load_data():
#     # Load your data here
#     data = pd.read_csv('/data/merged_cleaned_data.csv')
#     return data

# # Function to get model predictions
# def get_predictions(data):
#     # Preprocess your data
#     processed_data = preprocess(data)
#     # Get predictions
#     predictions = predict(processed_data)
#     return predictions

# # Main app
# def main():
#     st.title("Malicious Attack Prediction in Kubernetes Cluster")

#     # Load your data
#     data = load_data()

#     # Show data overview
#     st.header("Data Overview")
#     st.write(data)

#     # Show model summary
#     st.header("Model Summary")
#     st.write("Model details go here")

#     # Show real-time predictions
#     st.header("Real-time Predictions")
#     user_input = st.text_input("Enter your netflow data here")
#     user_data = pd.DataFrame([user_input.split(',')])
#     # st.write(get_predictions(user_data))

#     # Show prediction explanation
#     st.header("Prediction Explanation")
#     st.write("Explanation goes here")

#     # Show model comparison
#     st.header("Model Comparison")
#     st.write("Comparison details go here")

#     # Show anomaly detection
#     st.header("Anomaly Detection")
#     st.write("Anomaly details go here")

# if __name__ == "__main__":
#     main()

    
import streamlit as st
import random

def main():
    st.title("Number Guessing Game")

    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)

    # Initialize the game
    if 'number_to_guess' not in st.session_state:
        st.session_state['number_to_guess'] = number_to_guess
        st.session_state['guess'] = None

    st.write("Guess a number between 1 and 100.")

    # Get the player's guess
    st.session_state['guess'] = st.number_input("Enter your guess", min_value=1, max_value=100, value=50)

    # Check the player's guess
    if st.session_state['guess'] is not None:
        if st.session_state['guess'] < st.session_state['number_to_guess']:
            st.write("Too low! Try a higher number.")
        elif st.session_state['guess'] > st.session_state['number_to_guess']:
            st.write("Too high! Try a lower number.")
        else:
            st.write("Congratulations! You guessed the number.")
            st.session_state['number_to_guess'] = random.randint(1, 100)  # Generate a new number for the next game
            st.session_state['guess'] = None  # Reset the guess

if __name__ == "__main__":
    main()