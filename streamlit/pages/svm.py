import streamlit as st
import pandas as pd
from st_pages import add_indentation
add_indentation()

# Introduction
st.header("One-class SVM Model Testing")
st.write("""One-class SVM is a Support Vector Machine used for unsupervised learning, it is called One-class as it will classify the data into a single classification cluster, thereby finding any outliers/anomalies by the data points not covered within the single classification cluster (also referred to as novelty detection).""")

# Performance comparison with other models
st.header("Performance")
st.write("""
        Support Vector Machines, tries to solve a convex optimization problem as part of the deviation algorithm to detect outliers from the trained norm,
        this method of finding outliers, is extremely computationally intensive (especially with large amount of datapoints/features) compared to other anomaly detecting algorithms and thus generally takes significantly more time to train and predict. 
""")

model_execution_time = pd.DataFrame({
    'Model': ["RandomForestClassifier", "ExtraTreesClassifier", "BaggingClassifier", "DecisionTreeClassifier", "ExtraTreeClassifier", "KNeighborsClassifier", "AdaBoostClassifier", "SVC", "NuSVC", "BernoulliNB", "NearestCentroid", "PassiveAggressiveClassifier", "SGDClassifier", "LogisticRegression", "LinearDiscriminantAnalysis", "LinearSVC", "RidgeClassifier", "RidgeClassifierCV", "CalibratedClassifierCV", "DummyClassifier", "Perceptron", "GaussianNB", "QuadraticDiscriminantAnalysis"],
    'Prediction Time (ms)': [28.32, 9.46, 5.27, 0.87, 0.22, 10.25, 9.77, 1210.87, 4393.41, 0.26, 0.20, 0.64, 0.91, 1.45, 0.43, 86.11, 0.38, 0.60, 241.89, 0.15, 0.67, 0.17, 0.25]
})
model_execution_time = model_execution_time.sort_values(by=["Prediction Time (ms)"], ascending=False)
def highlight_SVM(val):
    color = 'dodgerblue' if val.endswith("SVC") else 'transparent'
    return f'background-color: {color}'

st.dataframe(model_execution_time.style.applymap(highlight_SVM, subset=['Model']))
st.markdown("*SVC = Support Vector Classifier*")

# SVM Model training exploration
st.header("Training")
st.write("""Novelty detection models are different from normal classification models, as they only try to predict a single class (therefore One-class), it does this in a similar manner to more complex anomaly detectors, by effectively modelling the "normal behavior" and thereby be able to detect outliers by removing any inliers.""")

st.write("""When these models are incorrectly trained, such as by providing it with unexpected outlier data, it will not be able to properly create distinctions between inliers and outliers (note: Many models offer hyperparameters to help difine how much of the data is expected to be outliers in the training set).""")

incorrect_train_results = pd.DataFrame({
    'precision': ["0.73", "0.00", "", "0.36", "0.53"],
    'recall': ["1.00", "0.00", "", "0.50", "0.73"],
    'f1': ["0.84", "0.00", "0.73", "0.42", "0.61"],
    'support': ["57523", "21649", "79172", "79172", "79172"],
}, index=["benign", "malicious", "accuracy", "maxro avg", "weighted avg"])
st.dataframe(incorrect_train_results)

st.write("""Keep in mind, that depending on the model and data distribution, even telling the model to be extremely tolerant to outliers, the model might still not be able to properly distinguish outliers (for OneClassSVM this is the nu value).""")
st.write("""nu = 0.9""")
incorrect_train_results_high_tolerance = pd.DataFrame({
    'precision': ["0.77", "0.98", "", "0.88", "0.83"],
    'recall': ["1.00", "0.22", "", "0.61", "0.79"],
    'f1': ["0.87", "0.36", "0.79", "0.61", "0.73"],
    'support': ["57523", "21649", "79172", "79172", "79172"],
}, index=["benign", "malicious", "accuracy", "maxro avg", "weighted avg"])
st.dataframe(incorrect_train_results_high_tolerance)

# SGD variant
st.header("SGD (Stochastic Gradient Descent) One-class SVM")
st.write("""
        Special types of Support Vector Machines for novelty detection exist, a popular one is SGD which works fairly similar to the higher processing time variants, but instead is able to perform some mathematical shorthands to approximate the same predictions.
        The performance improvements, combined with giving it a favorable dataset (exclusively benign data) allows the One-class SVM to perform significantly better than similarly classed models.
""")

SGD_train_results_unpotimized = pd.DataFrame({
    'precision': ["0.56", "0.96", "", "0.76", "0.82"],
    'recall': ["0.95", "0.60", "", "0.78", "0.72"],
    'f1': ["0.71", "0.74", "0.72", "0.72", "0.73"],
    'support': ["57723", "107245", "164968", "164968", "164968"],
}, index=["benign", "malicious", "accuracy", "maxro avg", "weighted avg"])
st.dataframe(SGD_train_results_unpotimized)

# Kernel Exploration 
st.header("One-Class SVM Kernel Exploration")
st.write("""Other than changing the SVM model technique and optimizing the training data, there are also several kernels that can be used to calculate similarities between data points in a higher-dimensional space.""")

st.write("""A common kernel is RBF, which uses a radial basis function to find the similarities in data, this generally expects the data to be normally distributed""")
RBF_train_results = pd.DataFrame({
    'precision': ["0.80", "0.77", "", "0.79", "0.78"],
    'recall': ["0.50", "0.93", "", "0.71", "0.78"],
    'f1': ["0.61", "0.85", "0.78", "0.73", "0.76"],
    'support': ["58234", "107245", "165479", "165479", "165479"],
}, index=["benign", "malicious", "accuracy", "maxro avg", "weighted avg"])
st.dataframe(RBF_train_results)

st.write("""Most features from the dataset, do not follow this expected normal distribution, thereby lowering the effectiveness of the RBF kernel.
         One way to improve this, is to process the data to make it normally distributed, such as putting it on a logarithmic scale in this case""")
st.image("./streamlit/media/ocsvm/bytes_distribution.png")

st.write("""Instead of processing the data logarithmically, the sigmoid kernel can be used that uses a form of logistic regression already.""")
sigmoid_train_results = pd.DataFrame({
    'precision': ["1.00", "0.82", "", "0.91", "0.88"],
    'recall': ["0.60", "1.00", "", "0.80", "0.86"],
    'f1': ["0.75", "0.90", "0.86", "0.83", "0.85"],
    'support': ["58234", "107245", "165479", "165479", "165479"],
}, index=["benign", "malicious", "accuracy", "maxro avg", "weighted avg"])
st.dataframe(sigmoid_train_results)
st.image("./streamlit/media/ocsvm/sigmoid_confusion_matrix.png")