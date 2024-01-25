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
st.image("./streamlit/media/barchart1.png")
st.markdown("""##### Example 2""")
st.image("./streamlit/media/barchart2.png")

st.markdown("""##### Scatterplots""")
st.write("This type of visualization was used mainly to get more insights into the data representation within one feature, as using scatterplots for this purpos is one of the best choices")
st.image("./streamlit/media/scatterplots.png")

st.markdown("""##### Advanced local bar plot""")
st.write("When implementing XAI into our models, our team had to rely on shap, to gain valuable information about the importance of each individual feature. Advanced local bar plots are very a good fit for this purpose, as they keep the simplicity of the original bar plot, but represent more information and have more organizatinal flexibility")
st.markdown("""##### Learning rate decay""")
st.write("In the beginning of the training the model has a lot to learn, but after a few dozens of epochs, it's quite the opposite. Learning rate decay gradually slows down the learning process to, again, prevent overfitting")

st.markdown("""##### Performance""")
st.write("Sadly, even considering all techniques that were implemented, neural network is extremely prone to overfitting. It seems that the dataset is too easy for the model, as the loss value goes up after some 10 epochs and precision values are usually much higher than recall, but despite those facts the model performed quite well.")
st.markdown("#### Final quality metrics for ANN:")
SGD_train_results_unpotimized = pd.DataFrame({
    'precision': ["0.987", "0.912"],
    'recall': ["0.26", "0.85"],
    'f1': ["0.412", "0.88"],
    'accuracy': ["0.982", "0.975"],
}, index=["Simple ANN", "Advanced ANN"])
# Performance comparison with other models


st.dataframe(SGD_train_results_unpotimized)
st.image("./streamlit/media/ANN_metrics.png")