import streamlit as st
import pandas as pd
from st_pages import add_indentation
add_indentation()

data_dir = "data/"
st.write("""Multiple datasets are used throughout this project, to standardize the use of these and thereby allow cross comparison between research/models, the datasets are standardized too, into a couple versions that can be used and referenced easily.""")

st.markdown("First all datasets are loaded: elastic_may2021_malicious_data, elastic_may2021_benign_data, elastic_february2022_data, elastic_may2022_data (all of the datasets are obtained from the same [research paper](https://data.4tu.nl/articles/dataset/AssureMOSS_Kubernetes_Run-time_Monitoring_Dataset/20463687))")
df = pd.read_csv(data_dir + 'elastic_may2021_malicious_data.csv', nrows=20) # We just load one for space savings
st.dataframe(df.head(20))
st.markdown("These datasets are stored as one large dataset, to be cleaned and processed, this dataset has 5090910 records with 11 features.")


st.markdown("Next missing data is analyzed and cleaned accordingly.")
st.image("./streamlit/media/missing_data.png", width=1000)

st.markdown("Next the label distribution is displayed, to give an idea of possible label imbalance, which for these datasets is definitely the case.")
st.image("./streamlit/media/label_distribution.png", width=1000)

st.markdown("The same can be done for features with labels, such as the network transport type.")
st.image("./streamlit/media/network_type_distribution.png", width=500)

st.markdown("Looking at the missing values from the merged dataset, there are three features with a relativelt small amount of missing data (8891/5090910)")
missing_data = pd.DataFrame({
    'Missing values': [7686, 8891, 8891]
}, index=['_source_network_transport', '_source_destination_port', '_source_source_port'])
st.dataframe(missing_data)
st.image("./streamlit/media/label_distribution_merged.png", width=500)

st.markdown("After cleaning the dataset:")
st.image("./streamlit/media/label_distribution_merged_cleaned.png", width=500)

st.markdown("Now that the dataset is cleaned, it can be processed for easier use with modelling, such as on-hot encoding the network transport type, and the label.")
df = pd.read_csv(data_dir + 'merged_cleaned_encoded_data.csv', nrows=20)
st.dataframe(df.head(20))


st.markdown("Some models might work better when the time-series nature of the data is encoded directly into the record, this can be achieved by merging a group of records (flow) into a single record and calculating features from the merge.")
df = pd.read_csv(data_dir + 'flow_data.csv', nrows=20)
st.dataframe(df.head(20))

st.write("This process, also greatly compresses the amount of records in the dataset, and seems to balance out the label distribution due to benign flows consisting of generally more records per flow")
st.image("./streamlit/media/label_distribution_flow.png", width=500)

st.write("Now the last step can take place, where the dataset is pre-split with a plit of 80/20 train/test, so that it can more easily be imported for training, and it is ensured that all training models use the same data split to avoid random bias or \"luck\".")

st.write("All of the datasets, with their relavent processing step are stored in the DVC file manager, allowing them to be pulled on demand by any collaborator or auomated tool.")