import base64
import streamlit as st
from st_clickable_images import clickable_images

tict_categories = ["human", "transparency", "impact", "stakeholders", "sustainability", "criminal", "data", "future", "privacy", "inclusivity"]
images = []
for category in tict_categories:
    with open(f"media/tict/{category}.png", "rb") as image:
        encoded = base64.b64encode(image.read()).decode()
        images.append(f"data:image/png;base64,{encoded}")

clicked = clickable_images(
    images,
    titles=[f"Image #{str(i)}" for i in range(2)],
    div_style={"display": "flex", "justify-content": "center", "flex-wrap": "wrap"},
    img_style={"margin": "5px", "height": "120px", "cursor": "pointer"},
)

selected_category = tict_categories[clicked if clicked > -1 else 6]
if selected_category == "human":
    st.header("Human Values")
    st.markdown("The engineers utilizing this tool will be able to spend less time investigating potential problems and work more targeted, but might become biased to specific applications that are often flagged by the detector (incorrectly or not).")
elif selected_category == "transparency":
    st.header("Transparency")
    st.markdown("The underlying technologies have been clearly explored and described to the stakeholders, technologies used such as State Machines are easily human understandable due to their logical flow, while Transformers are not and thus will be hard to explain the decision making.")
    st.markdown("SUE didn't give us any direct instructions on how transparent our model should be, but we know for a fact that the previous student group preferred state machines (simple and explainable) to neural networks (efficient but convoluted). With this information in mind, we try to make the results as clear as possible - our goal is to ensure the client understands what happens behind the scenes. We believe that currently we are keeping SUE sufficiently informed – we explain every step we take in detail, for instance when dealing with state machines we spent a fair share of our presentation explaining how everything works to the client. Same goes for other models – instead of giving simple quality metrics, we try to show our workflow in Jupiter Notebooks or similar environments, so that the client can understand what is going on. We also use data visualization quite extensively, to be transparent about such important aspects as dataset outliers, data representation, confusion matrix and such. Perhaps we could have also made use of explainable AI (such as SHAP) that represents the \"logical process\" behind AI decision making. However, in the current state of affairs this feature is out of scope, so the only thing we can do now is to mention it in the transfer document – perhaps succeeding groups might find this idea useful.")
    st.markdown("As for user transparency – first of all it is difficult to say whether regular people would make use of our project in the first place. Moreover, we don't have any specific requirements from SUE for this regard, however we think that this matter is not in our team's competence, since we were only given the task to provide SUE with irregularity-detecting model, and it is up to them to decide on how they are planning to dispose it.")
elif selected_category == "impact":
    st.header("Impact on Society")
    st.markdown("Kubernetes clusters are attacked by malicious users")
elif selected_category == "stakeholders":
    st.header("Stakeholders")
    st.markdown("Stakeholders of solution:")
    st.markdown("- Engineers maintaining Kubernetes clusters")
    st.markdown("- Users of the hosted services")
    st.text('')
    st.markdown("Stakeholders of project:")
    st.markdown("Our primary stakeholder is SUE; SUE is a company that, alongside other things, works with managing security in Kubernetes clusters of their clients. They have ordered us to train a model that is able to efficiently predict irregularities inside of the aforementioned clusters.")
    st.markdown("Due to the project's specifics, our team has to constantly keep SUE's needs and wants in mind, in fact the projects workflow consists of multiple feedback loops - we conduct an interview with our client, get some valuable feedback and incorporate the feedback into what we already have. Of course, we are not obligated to fulfill every single requirement – after all we, as students, have limited time resources and computational power. That's why when the next feedback loop occurs, we elaborate on what we were able to implement and what had stayed out of scope. Then the client gives us new instructions based on our team's report and the cycle goes on.")
    st.markdown("Our secondary stakeholders are teachers and Fontys in general.")
    st.markdown("At first glance our only stakeholder is the client, but our teachers and Fontys in general also have an interest in our project, though not as much as SUE of course. Teachers want to know the progress on the project, as their job is to review what we have done so far and provide feedback, so that we have something to work on. Moreover, if we deal with the task successfully and pass the project, it might improve teachers' reputation, leading to a potential raise. Similarly, Fontys university also influences our workflow in a way, since it plays the role of a facilitator between us and the client. Moreover, if we succeed in our project, it will also boost the reputation of Fontys, so in a way, Fontys could also be called our stakeholder.")
elif selected_category == "sustainability":
    st.header("Sustainability")
    st.markdown("With the various possible technologies available, the efficiency in both time and resources is accounted for when determining the best technology to use.")
elif selected_category == "criminal":
    st.header("Hateful and Criminal actors")
    st.markdown("The technology can be used to break the law by enabling malicious users to launch cyberattacks on Kubernetes clusters, such as data theft or denial of service. If the attackers learn how the technology catches malicious attacks, it would allow them to bypass it. These attacks can compromise the security, availability, and performance of the hosted services and cause financial or reputational damage to the cluster owners and users.")
    st.markdown("Fakers, thieves or scammers can abuse the technology by exploiting the vulnerabilities or misconfigurations of the Kubernetes clusters or the anomaly detection system. For example, they can use social engineering, phishing, or malware to gain access to the cluster credentials or the anomaly detection system. They can then manipulate the system to either bypass the detection, generate false positives, or disable the alerts. This can allow them to carry out their malicious activities without being noticed or stopped.")
    st.markdown("Since the technology only uses netflow data (IPs and ports) and does not involve any personal data, it is unlikely to be used against certain (ethnic) groups or (social) classes.")
    st.markdown("Given that the technology only deals with netflow data and does not involve any personal or sensitive information, it is unlikely that bad actors can use this technology to pit certain groups against each other.")
    st.markdown("Bad actors could potentially learn how the model is predicting and devise new attacks that can bypass the detection. They could also attempt to manipulate the netflow data or the system settings to interfere with the detection process or to produce misleading or false results. This could undermine the integrity and reliability of the technology and lead to incorrect decisions or actions. Therefore, it is crucial to continuously monitor, update, and improve the technology to stay ahead of the evolving threats and challenges.")
    st.markdown("Continually refine the anomaly detection models to stay ahead of evolving threats, implement robust security measures and regularly monitor network traffic, educate users on cybersecurity best practices and establish clear policies for handling security incidents.")
elif selected_category == "data":
    st.header("Data")
    st.markdown("Our project relies on networking data collected from active Kubernetes clusters, this data is therefore inherently linked to individual user behavior which immediately brings up possible privacy concerns such as GDPR regulations, some aspects of this private data can be anonymized to ensure no record can be linked back to an individual user (such as IP addresses, timestamps, etc.). But it might also be worth considering that to collect enough data to be valuable, more private and user-specific data needs to be used, in which case more direct actions have to be taken to stay compliant with all the regulations different parts of the world have set up where the Kubernetes clusters are serving to, such as disclaimers or opt-out/in options.")
    st.markdown("As the currently proposed solution needs to keep receiving data to make new predictions, including possibly storing this data to retrain the models, any data that must be collected will need to continue indefinitely as long as the solution exists, which could create a very important decision line of what data to collect or not.")
    st.markdown("Due to the invisible nature of the decision making of some models proposed for the solution, labelled data is used during the model selection process to evaluate how and why a model performed specific actions. Using labelled networking data however, comes with some additional concerns; such as unexpected performance differences between the “testing” labelled data and the real data due to unexpected differences in the data or behavior, which would be very hard to detect.  \n\
                Furthermore, the labelling process of malicious vs benign networking logs is done manually, leaving a lot of possibility for human mistakes, or even human bias to be added.  \n\
                The currently used labelled data was collected as part of a research paper, and was done in a reproduceable and controlled environment, following a very methodological process at the cost of increasing the possibility of variation from a real world representation.")
    st.markdown("Due to the significant adoption of the “Big Data” movement over the past few decades, a new problem has arisen within the field of AI and data. In general, there is more data being collected (and collected in the past) than can be effectively processed in the same amount of time. Due to this data surplus vs time deficit, more modern solution that have been considered are actually built to be more time efficient at processing the data at the cost of accuracy. Therefore, a consideration has to be made of how long data will be collected before the solution is used to allow for a proper trade-off to be made between data and time.")
elif selected_category == "future":
    st.header("Future")
    st.markdown("The anomaly detection technology could become more sophisticated, capable of detecting even the most subtle irregularities in network traffic. It could also adapt to new types of attacks as they emerge, ensuring the security of Kubernetes clusters.")
    st.markdown("In a utopian future, the anomaly detection technology has become so advanced that it can predict and prevent cyberattacks before they happen. This has led to a significant decrease in successful attacks, making the digital world a safer place for everyone.")
    st.markdown("In a dystopian future, malicious actors have discovered an infallible method to evade the anomaly detection system. The technology reveals the types of attacks it is designed to capture, eventually providing a roadmap for these attackers.")
    st.markdown("A future where online activities are transparent, and scams and malicious attacks are minimal, would be much more desirable. Its a scenario that aligns with the ideals of safety, trust, and peace of mind in the digital world.")
    st.markdown("If the technology is taken over by another party, its use could change based on the partys intentions. Its crucial to have safeguards in place, like legal agreements, to ensure the technology continues to be used ethically.")
    st.markdown("If the technology is taken over by another party, its use could change based on the partys intentions. Its crucial to have safeguards in place, like legal agreements, to ensure the technology continues to be used ethically.")
elif selected_category == "privacy":
    st.header("Privacy")
    st.markdown("Networking traffic of users is gathered which includes identifiable features such as IP addresses, networking protocols, time stamps (this can be used for online fingerprinting).")
elif selected_category == "inclusivity":
    st.header("Inclusivity")
    st.markdown("Due to our solution labelling networking logs as malicious or benign, we are effectively trying to isolate “malicious” users from “normal” ones, which when considering that the data used to make this separation are abstractly connected to an individual’s behavior online, it is fair to assume that the model must become biased against a kind of user to be effective.  \n\
                This is something that can go wrong very quickly, both by machines and by human, which was indicated towards when our solution was showcased during a midterm Fontys event where multiple individuals asked if the model worked by “paying more attention to Russian users” as in media any large online malicious attack is often linked to “the Russian hackers”.")
    st.markdown("To emphasize the issue, of not properly being able to understand how a model choses to label networking records, most proposed solutions do not “hesitate” when labelling records as benign or malicious as it deterministically determined based on some threshold thereby losing any ambiguity about the decision process (as if a model was only 51% sure something is malicious, you might consider that prediction less valuable or substantiated than if the model says it is 100% sure).")