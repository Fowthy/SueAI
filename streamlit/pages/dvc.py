import streamlit as st
import os
from st_pages import add_indentation
add_indentation()

st.markdown("As a part of the project's AI Dev/Ops tools, [DVC](https://dvc.org/) has been used to manage data and AI models")
st.markdown("Datasets used within the AI domain can become very large, so large infact that typical file management tools such as the used [GitHub Repository blocks them from being uploaded](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github#file-size-limits).")
st.markdown("The implemented DVC pipeline integrates on top of the existing GitHub repository, allowing any collaborators on the project to easily obtain any dataset they need from the project's [S3 bucket](https://aws.amazon.com/s3/). \n\
            This allows anyone from anywhere to directly obtain the datasets they require, including any cloud services such as this streamlit app!, or a automated pipeline such as GitHub actions")

st.markdown("To use DVC locally to pull the project's datasets, first set the authentication keys for the AWS S3 bucket:")
st.code("dvc remote modify --local sue_2023 access_key_id TOKENHERE", language="bash")
st.code("dvc remote modify --local sue_2023 secret_access_key TOKENHERE", language="bash")
st.markdown("Then simply pull the file (or pull everything = -a):")
st.code("dvc pull -a", language="bash")

csv_files = [file for file in os.listdir("data") if file.endswith(".csv")]
st.selectbox("Available DVC files", list(csv_files))
st.markdown("NOTE: *The DVC tool is not limited to datasets, and can be used to store any filetype, as well as keep a history of file changes*")

st.markdown("The project's DVC toolchain is furter expanded with Iterative Studio, this allows us to store results of models for later reference or evaluation, and together with the DVC file storage also allows for the models to be directly stored for later use.")

with st.container(border=True):
    # Github
    left_col, right_col = st.columns([0.2, 0.8])
    left_col.image("./streamlit/media/github.png", width=120)
    right_col.write('')
    right_col.write('')
    right_col.write('')
    right_col.write('')
    right_col.write('')
    right_col.markdown("All technical research files such as source code and Jupiter notebooks are stored within a GitHub repository to simplify collaboration and version control.")
    _, child_col = st.columns([0.1, 0.9])
    # Github children, DVC, Iterative Studio
    with child_col:
        left_col, right_col = st.columns([0.2, 0.8])
        left_col.image("./streamlit/media/dvc.png", width=100)
        right_col.write('')
        right_col.write('')
        right_col.markdown("Large files, such as datasets are stored and management via DVC, allowing them to be downloaded on demand when required.")
        left_col, right_col = st.columns([0.2, 0.8])
        left_col.image("./streamlit/media/iterativestudio.png", width=100)
        right_col.markdown("Models and their results are stored within Iterative Studio where they can be downloaded or directly evaluated/compared.")
    # Sharepoint
    left_col, right_col = st.columns([0.2, 0.8])
    left_col.image("./streamlit/media/sharepoint.png", width=120)
    right_col.write('')
    right_col.write('')
    right_col.write('')
    right_col.write('')
    right_col.write('')
    right_col.markdown("Sharepoint is used to store and collaborate on any complementary documentation.")