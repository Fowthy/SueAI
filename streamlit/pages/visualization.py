import streamlit as st
import pandas as pd
from st_pages import add_indentation
add_indentation()

# Introduction
st.header("Data Visualization")
st.write("""Our team consists of 3 former software engineering student, so clearly none of us is a big fan of data visualization. However, it is a crucial step in development process, as it shows all potential data outliers in a way that is informative and pleasant to a human eye. Our team didn't have a standardized way of visualizing data, instead each of us went their own way and so there were multiple types of plots and graphs that we have relied on.""")

st.markdown("#### Barcharts")
st.write("This is one of the simlest, yet most powerful types of data visualization. We mainly used it when a comparison between anomalous data and benign data was required. By plotting the values from this two target groups on one bar chart, it became extremely clear where the outlier is:")
st.markdown("""##### Example 1""")
st.image("./streamlit/media/barcharts1.png")
st.markdown("""##### Example 2""")
st.image("./streamlit/media/barcharts2.png")

st.markdown("""##### Scatterplots""")
st.write("This type of visualization was used mainly to get more insights into the data representation within one feature, as using scatterplots for this purpos is one of the best choices")
st.image("./streamlit/media/scatterplots.png")

st.markdown("""##### Advanced local bar plot""")
st.write("When implementing XAI into our models, our team had to rely on shap, to gain valuable information about the importance of each individual feature. Advanced local bar plots are very a good fit for this purpose, as they keep the simplicity of the original bar plot, but represent more information and have more organizatinal flexibility")
st.image("./streamlit/media/advanced_bar_plot.png")
st.markdown("""##### Confusion matrixes""")
st.write("This type of data visualization was extremely useful when trying to calculate precision and recall. Knowing the percentages is great, but sometimes it is much easier to just spot the color difference to understand the approximate quality metrics.")
st.markdown("""##### Example 1""")
st.image("./streamlit/media/confusion1.png")
st.markdown("""##### Example 2""")
st.image("./streamlit/media/confusion2.png")
df = pd.DataFrame({
    'precision': ["0.915", "0.915", "0.915", "0.85"],
    'f1': ["0.86", "0.86", "0.86", "0.797"],
    'precision': ["0.754", "0.754", "0.754", "0.754"],
    'recall': ["1.0", "1.0", "1.0", "0.844"],
}, index=["10% perturbation, 50% perturbation", "80% perturbation", "without perturbation"])