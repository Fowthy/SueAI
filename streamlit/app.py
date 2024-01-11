import streamlit as st
import random
import pandas as pd
import numpy as np
from dvc.api import DVCFileSystem

def fetch_data():
    # Load all data files from DVC remote
    # try:
    dvc_config = {
        "remote": {
            st.secrets.dvc.remote_name: {
                "url": st.secrets.dvc.remote_url,
                "access_key_id": st.secrets.dvc.access_key_id,
                "secret_access_key": st.secrets.dvc.secret_access_key
            },
        },
    }
    fs = DVCFileSystem(st.secrets.dvc.git_url, config=dvc_config) # Go up in the directory to enter the root of the repository where the dvc file system should start
    print("Started fetching DVC data")
    fs.get("data/", "data", recursive=True) # Pull all dvc files from the data folder and populate them in-place
    print("Completed fetching data")
    # except Error
        # print("Failed to obtain data from remote, continuing execution, some data files might not be available")


def main():
    fetch_data()

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