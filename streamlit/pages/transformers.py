import streamlit as st
import pandas as pd
from st_pages import add_indentation
add_indentation()

# Introduction
st.header("Transformer Model Testing")
st.write("""The use of transformers for detecting anomalies over multivariate time series data has recently become more popularity, 
         coincidentally, the networking logs captured for this project to be analyzed for anomalies is multivariate and has a very important time series element attached to it.
         Transformers aim to supersede older neural network technologies such as RNN's and LSTMs, which have previously also been used for anomaly detection on timeseries data, so it is only logical to attempt to use transformers for this use-case too""")

st.header("Complications")
st.write("""A major downside, both in the ability to use transformers as an ethical concern, is the disproportionate amount of resources that are required to train and use transformers for the amount of data they process and return.
         Due to the ever increasing concern on this topic, more modern transformers have attempted to improve their data efficiency; allowing the models to be trained faster and with less data.""")

st.write("""Another possible issue for using transformers in our project, is the complexity and the non-standard nature of these models, this makes them hard (or even impossible in limited time with a small project group) to create one from scratch, and no resources exist yet to easily implement specialized models, such as tensorflow or sci-kit learn.""")

st.header("TranAD")
st.write("""The transformer that has been explored for this project is [TranAD](https://vldb.org/pvldb/vol15/p1201-tuli.pdf), an anomaly detection deep transformer network that is optimized for training on limited multivariate time series data.""")
st.image("./streamlit/media/transformers/tranad_model_comparison.png")

st.write("""TranAD uses two encoders and two decoders to generate an anomaly score for detecting anomalies.
         The two encoders are able to process the incoming multivariate data and store in a time encoded window, the first decoder tries to reproduce the data from the window, while the second decoder tries to detect differences between the decoders output and the window (effectively running out of sequence of one-another).
         The output of the second decoder can be used as the anomaly score/factor of the actual data, if this anomaly score meets given thresholds, the data within that window, can be marked as an outlier.
         Keep in mind that this process happens seperately for each feature, and thereby can have the weight of a given features anomaly score changed as well as aggregated depending on the expected data and use-case.""")
st.image("./streamlit/media/transformers/tranad_structure.png")

st.header("Training")
st.write("""As previously mentioned as part of possible complications, and attempted to be mitigated when choosing the model, training of transformers can take a lot of time, especially with limited computing resources.
         The dataset this transformer was trained on only includes ~1% of the total dataset (42.500/5.082.019), this took ~2 hours over 5 epochs.
         The limited dataset and training time have to be kept in mind during evaluation, as well as the lack of parameter tuning as this could possibly cause the maximum potential of the model to be misrepresented.""")
st.write("""The TranAD model was trained using a modified version of the sourcecode found on the [GitHub repository](https://github.com/imperial-qore/TranAD), with the network_bytes, event_duration and transport_type (one-hot encoded into multiple features) being order based on timestamp and vector encoded.""")

st.write("""The model will output its anomaly score for every dimension (feature) seperately and can be used to identify anomalies.""")
st.image(["./streamlit/media/transformers/output_dim0.png", "./streamlit/media/transformers/output_dim1.png", "./streamlit/media/transformers/output_dim2.png", "./streamlit/media/transformers/output_dim3.png"])

st.write("""These predictions are compared to given thresholds to determine malicious records.""")
tranad_results = pd.DataFrame({
    'precision': ["0.810"],
    'recall': ["0.999"],
    'f1': ["0.8952"],
    'accuracy': ["97.94%"],
})
st.dataframe(tranad_results)
st.image("./streamlit/media/transformers/tranad_confusion_matrix.png")