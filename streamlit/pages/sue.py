import streamlit as st
import pandas as pd
from st_pages import add_indentation
add_indentation()

# Introduction
st.header("SUE")
st.write("""SUE is our client and main stakeholder. They are a large multinational company which mission is enabling organizations to realize their full potential using dedicated and powerful IT solutions. This also includes ensuring security within Kubernete's clusters of their clients, and with recent advancements in AI field it became possible to use Artificial Intelligence to assist regular people in preventing DDOS attacks and similar malicious activities. So SUE had turned to us, students, hopng that we can come up with an algorithm that efficiently detects malicious activity in real time.""")

st.markdown("#### Some information about the project")
st.write("Before we have started to work on this project, there was another group of students from TU Delft, who worked on the exact same task in the previous 6 months. They have achieved some great results and shared their findings, helping us with our research where possible.")
st.markdown("#### Quick facts about SUE")
st.markdown("###### - 26 years of experience")
st.markdown("###### - 50 succesful cloud migrations")
st.markdown("###### - AWS Star partner of the year 2023")
st.markdown("###### - #1 largest cloud-native business community in Europe")
st.image("./streamlit/media/sue.png")
st.markdown("###### Sue logo")