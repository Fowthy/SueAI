import streamlit as st
from st_pages import add_indentation
add_indentation()

st.header("Recommendation")
st.write("For the future, our group recommends finishing training :blue[State Machines] and the :blue[Tran-AD transformer], as they have the best performance so far.")
st.write("""We also advise to use models that support unsupervised learning, as in practice it is extremely difficult to classify all possible anomalies – malicious data is a very broad term, so algorithms that heavily rely on an existing labeled data (such as decision trees) would not be useful in a real-world scenario.  
         Instead, we recommend using models that are trained on representing a benign system and find malicious data by identifying deviations from the expected result, as benign data is expected and follows the artificially learned complex set of rules.""")