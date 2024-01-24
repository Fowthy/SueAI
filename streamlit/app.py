import streamlit as st
import random
import pandas as pd
import numpy as np

def main():
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