import streamlit as st
import pandas as pd
from st_pages import add_indentation
add_indentation()

# Introduction
st.header("State machines")
st.write("""State machines are very powrful models - the previous group specified that out of all models they tried, state machines performed best and were the most robust. 
         In the context of our project, state machines has two big strong points:""")
st.markdown("""###### a) State machines are from a subset of unsupervised learning models. See the webpage "Supervised vs. Unsupervised" on why this is important """)
st.markdown("""###### b) State machines take non-numeric data as an input. Our dataset has around 30% of non-numeric features and by using state machines we can efficiently use them in training """)

st.markdown("""#### Disadvantages""")
st.write("""Though state machines have many strong points, they also have a number of disadvantages, that make the training process more difficult then with other algorithms""")
st.markdown("""##### Lack of educational material""")
st.write("""State machines are niché models, so there's no tutorials available online. Instead we had to analyze research papers and contact the researchers to get more info.""")
st.markdown("""##### Complicated encoding process""")
st.write("""Before training could even start, a strict encoding process should be performed, formatting the dataset in Abbadingo format. The process is complex, and coupled with the fact that there's zero tutorials available online, this has slowed down the development progress significantly""")
st.markdown("""##### Computational capabilities""")
st.write("""State machines require a lot of RAM and GPU in order to train - even 32GB RAM is not enough when training on a dataset with one million rows.""")

st.markdown("#### Results")
st.write("Combined together, the negative factors that I've stated above made it impossible for us to reproduce the results of a previous group. The model constantly produced a lot of errors which took a lot time to fix, and when the training process started, the estimated training time was 4 days. ")
st.write("""For reference, below are the state machines quality metrics of a previous group:""")
df = pd.DataFrame({
    'precision': ["0.915", "0.915", "0.915", "0.85"],
    'f1': ["0.86", "0.86", "0.86", "0.797"],
    'precision': ["0.754", "0.754", "0.754", "0.754"],
    'recall': ["1.0", "1.0", "1.0", "0.844"],
}, index=["10% perturbation, 50% perturbation", "80% perturbation", "without perturbation"])
st.dataframe(df)
