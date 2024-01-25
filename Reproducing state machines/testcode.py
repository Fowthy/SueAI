
##Testing flexfringe with a small csv dataset of a few kb's

##Code taken from tudelft flexfringe github repo

import pandas as pd
from flexfringe import FlexFringe

tracefile = "C:/Users/tymak/Documents/GitHub/sueai/Reproducing state machines/sample_dataset.csv"

df_tracefile = pd.read_csv(tracefile)
df_tracefile = df_tracefile.rename(columns={"State": "symb"})

flexfringe = FlexFringe(
    flexfringe_path="C:/Flexfringe/Debug",
    heuristic_name="first_dataset",
    data_name="first_dataset_to_test",
    slidingwindow=1,
    swsize=10,
)

# Learn a state machine
flexfringe.fit(df_tracefile,
               sinkson=1,
               sinkcount=100)

# Use state machine to predict likelihoods
df = flexfringe.predict(df_tracefile)

print(df.head())