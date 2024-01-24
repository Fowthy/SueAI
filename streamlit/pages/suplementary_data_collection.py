import streamlit as st
import pandas as pd
import joblib
from sklearn.metrics import accuracy_score
from joblib import load
from st_pages import add_indentation
add_indentation()

model = load('isolationforest.joblib')

# Function to preprocess and predict
def predict(df):
    df = df.rename(columns={
    'Network bytes': '_source_network_bytes',
    'Destination Port': '_source_destination_port',
    'Source Port': '_source_source_port',
    'HTTP': 'udp',
    'TCP': 'tcp'
    })

    X_test = df

    non_numeric_cols = X_test.select_dtypes(include=['object']).columns

    # Drop or encode non-numeric columns
    X_test = X_test.drop(columns=non_numeric_cols)
    X_test = X_test.drop(columns=['No.', 'predicted_label','predicted_label_isolationforest', 'Unnamed: 0'])
    X_test.head(5)
    
    # Predict
    y_pred = model.predict(X_test)
    
    # Add predictions to DataFrame
    df['predicted_label_isolationforest'] = y_pred
    
    return df

# Main function for your Streamlit app
def main():
    st.title("Kubernetes Cluster Logs Collection and Testing")
    st.write("In order to further test the models, we have collected data from a public Kubernetes cluster. The data was collected using the kuberentes sniff tool.")
    st.image("./streamlit/media/wiresharkjmeter.png")

    st.header("Kubernetes Goat Setup")
    st.write("First we had to setup a kubernetes environment in order to monitor the logs. We used the Kubernetes Goat project for this purpose. Kubernetes Goat is a vulnerable by design Kubernetes cluster that allows security researchers and enthusiasts to learn Kubernetes security, practice Kubernetes penetration testing, and to learn more about Kubernetes. Kubernetes Goat is an vulnerable by design Kubernetes cluster that allows security researchers and enthusiasts to learn Kubernetes security, practice Kubernetes penetration testing, and to learn more about Kubernetes.")
    st.write("The Kubernetes Goat project is available at https://github.com/madhuakula/kubernetes-goat")
    st.write("To run the kubernetes environment locally we used the following commands:")
    st.code("git clone 'https://github.com/madhuakula/kubernetes-goat'")
    st.code("cd kubernetes-goat")
    st.code("bash setup-kubernetes-goat.sh")
    st.code("bash access-kubernetes-goat.sh")
    st.write("Now it can be accessible at http://localhost:1234. Obviously you must have docker installed and running on your machine. More instructions can be found in repository")
    st.write("In order to collect the logs we used the kubernetes sniff tool: https://github.com/eldadru/ksniff. Instructions on how to install on Windows or Linux can be found in repository.")
    st.write("To collect the logs we used the following command (You must have Wireshark installed):")
    st.code("kubectl sniff pod_name -n default")
    st.write("And to get the pods names we use kubectl get pods")
    
    st.header("Data Collection")
    st.write("We collected data for roughly one hour of normal and malicious activity on the home page of the kubernetes goat.")

    # Create a DataFrame from your text
    df = pd.DataFrame([
        ('15:04', 50, 800, 'Normal'),
        ('15:04', 30, 1100, 'Normal'),
        ('15:07', None, None, None),
        ('15:08', 2000, 700, 'Malicious'),
        ('15:09', 150, 800, 'Normal'),
        ('15:14', 1250, 500, 'Malicious'),
        ('15:15', 1250, 600, 'Malicious'),
        ('15:17', 3000, 700, 'Malicious'),
        ('15:53', None, None, None)
    ], columns=['Time', 'Users', 'Timer', 'Attack'])

    # Display the DataFrame
    st.dataframe(df)
    st.image("./streamlit/media/jmeter.png")

    # Display DataFrame
    # st.header("DataFrame")
    df = pd.read_csv('./data/generateddata.csv')
    
    
    # Predict and display results
    df = predict(df)
    st.header("Predictions")
    counts = df['predicted_label'].value_counts()

    # Display the counts
    st.write("This shows how many rows were predicted as normal or malicious on the new dataset. And as you can see the results are almost 50/50, which means both IsolationForest and DecisionTrees models does not perform well on a new data.")
    st.write(counts)

    counts = df['predicted_label_isolationforest'].value_counts()
    st.write(counts)

    # Convert 'Time' to datetime format
    df['Time'] = pd.to_datetime(df['Time'])

    # Set the time range
    start_time = pd.to_datetime('2024-01-24 15:08:00')
    end_time = pd.to_datetime('2024-01-24 15:09:00')

    # Filter the DataFrame by the time range
    df_range = df[(df['Time'] >= start_time) & (df['Time'] <= end_time)]

    # Display the filtered DataFrame
    counts = df_range['predicted_label'].value_counts()
    st.write("And this are the results between the time range of 15:08 and 15:09, where the attack took place. Still the results are almost random.")
    st.write(counts)

    

# Run the app
if __name__ == "__main__":
    main()