import streamlit as st
from dvc.api import DVCFileSystem
import os
import pandas as pd
from st_pages import add_indentation
add_indentation()

data_path = "data"

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
    fs.get("data/", data_path, recursive=True) # Pull all dvc files from the data folder and populate them in-place
    print("Completed fetching data")
    # except Error
        # print("Failed to obtain data from remote, continuing execution, some data files might not be available")
    
# manually pull the DVC
st.button("Pull DVC", on_click=fetch_data)

# Get a list of all files in the data directory ending with ".csv"
csv_files = [file for file in os.listdir(data_path) if file.endswith(".csv")]
# Create a dictionary with file names and their full paths
file_dict = {file: os.path.join(data_path, file) for file in csv_files}
# Create a dropdown to select the file
selected_file = st.selectbox("Select data file", list(file_dict.keys()))

# Display the selected file name and its pandas dataframe
if selected_file:
    file_path = file_dict[selected_file]
    st.write(f"{selected_file}  [{file_path}]")
    df = pd.read_csv(file_dict[selected_file])
    st.dataframe(df)