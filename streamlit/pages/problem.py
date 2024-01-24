import streamlit as st
from st_pages import add_indentation
add_indentation()


st.title("Which :blue[AI methods] can be used to :blue[detect irregularities] in cloud-based :blue[Kubernetes clusters]?")


st.header("Context")
st.markdown("Kubernetes is an open-source container management system to support the process of running large microservice-based applications.")
st.markdown("Kubernetes is used by many large companies to help orchestrate the communication and resource management between services within a product (containers)")
services = ["./streamlit/media/google.png", "./streamlit/media/gmail.png", "./streamlit/media/maps.png", "./streamlit/media/drive.png"]
with st.container(border = True):
    user_col, kubernetes_col, services_col = st.columns([0.3, 0.3, 0.2], gap="small")
    with user_col:
        st.write('')
        left_col, right_col = st.columns(2, gap="small")
        left_col.image("./streamlit/media/user.png", width=150)
        right_col.write('')
        right_col.write('')
        right_col.image("./streamlit/media/arrow_right.png", width=75)
    with kubernetes_col:
        st.write('')
        left_col, right_col = st.columns(2, gap="small")
        left_col.image("./streamlit/media/kubernetes.png", width=150)
        right_col.write('')
        right_col.write('')
        right_col.image("./streamlit/media/arrow_right.png", width=75)
    with services_col:
        st.image(services, width=75)
st.markdown("There are many bad actors out there, trying to maliciously attack the services hosted within these Kubernetes clusters.")
st.markdown("Protecting against these attacks, and maintaining the clusters can be a lot of hard work for many companies.")

st.header("Opportunity")
st.markdown("SUE tries to aleviate some of the stress associated with hosting these services by taking care of the Kubernetes management process for their clients.  \n\
            However, keeping these services protected is complicated and requires a lot of human attention, so it was decided to make use of recent developments in the field of AI to simplify the monitoring process.")
st.markdown("SUE would like to investigate the possibility of an AI model which would continuously analyze networking logs from their clusters, thereby automatically identifying the irregularities in Kubernetes clusters, and be able to take action faster and more decisively.")


st.header("Questions")
st.markdown("“Which AI model techniques are best suited for predicting cloud-hosted Kubernetes cluster irregularities?”")
st.markdown("“What are the more common irregularities within cloud-hosted Kubernetes clusters?”")
st.markdown("“What data should be collected for predicting irregularities within an accepted margin of error?”")
st.markdown("“How should individuals be notified of any identified problems?”")
st.markdown("“Will changes in deployments effect a general model’s results?”")
st.markdown("“What privacy concerns should be taken into account when using data from company’s applications?”")
st.markdown("“How can models be evaluated and compared to define their effectiveness in predicting irregularities?”")
st.markdown("“What solutions already exists for predicting issues within Kubernetes clusters?”")


st.header("Methodology")
st.markdown("The [DOT framework](https://ictresearchmethods.nl/The_DOT_Framework) will be used when conducting research within this project. Within this research, many different methods from multiple research strategies will be utilized to allow for method triangulation, improving the quality and results of the research done.")
st.markdown("During this project, methods primarily from the Library, Workshop and Field strategies will be utilized, such as: [Available product analysis](https://ictresearchmethods.nl/Available_product_analysis), [Literature study](https://ictresearchmethods.nl/Literature_study), [Expert interview](https://ictresearchmethods.nl/Expert_interview), [Prototyping](https://ictresearchmethods.nl/Prototyping) and [Problem analysis](https://ictresearchmethods.nl/Problem_analysis).")