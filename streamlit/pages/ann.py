import streamlit as st
import pandas as pd
from st_pages import add_indentation
add_indentation()

# Introduction
st.header("Artificial Neural Network")
st.write("""Deep learning is extrmely popular right now, and  it is well-deserved, since Neural Networks had been proven useful in solving many complex tasks, that were impossible before. For example with the help of transformers, a newest deep learning model, it became possible to create extremely large easily scaleable models, which lead to creation of ChatGPT. Considering all of the above, we have decided to try to train neural networks for anomaly detection, especially considering that with Keras and Tensorflow it is simpler then ever. """)

st.header("Archutecture")
st.write("We've decided to use a simple architecture, with 1 input layer, three hidden layers and 1 output layer. All in all, the architecture of our ANN looks like this:")
st.write("Input layer - 15 neurons")
st.markdown("__Hidden layer 1 - 30 neurons__")
st.markdown("__Hidden layer 2 - 50 neurons__")
st.markdown("__Hidden layer 3 - 70 neurons__")
st.markdown("__Output layer - 1 neuron__")
st.markdown("#### Techniques used")
st.write("To prevent overfitting and improve prediction results, our group used the following techniques:")
st.markdown("##### L1 Regularization")
st.write("L1 regularization is a powerful tool, which penalizes the neurons that learn too fast, preventing overfitting. It's similar to dropout, but is applied individually on a layer level")
st.markdown("""##### Dropout""")
st.write("Another powerful technique, that randomly disconnects a certain percentage of neurons each training epoch to prevent overfitting")
st.markdown("""##### Early stopping""")
st.write("The quality of the predictions in ANN are defined by loss function. If it goes down each training epoch, it means that the model learns well without overfitting. However if it goes up it doesn't lead to anything great, so with early stopping the training process stops when the loss value starts to fluctuate")
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