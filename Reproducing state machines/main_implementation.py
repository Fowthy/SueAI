import os
os.environ['JOBLIB_START_METHOD'] = 'spawn'
os.environ['LOKY_MAX_CPU_COUNT'] = '8'
from encode.encode import encode
import pandas as pd
from flexfringe import FlexFringe
import multiprocessing

results = pd.read_csv("C:\\Users\\tymak\\Desktop\\AI Stuff\\Reproducing state machines\\merged_cleaned_data.csv")

results = results.sample(frac=0.01)

print(os.cpu_count())
print(results.head())

#make sure that there are no null values (just in case) 
results = results.dropna()

bytes_encoding = encode(
 		feature='_source_network_bytes',
 		time_host_column_mapping={'timestamp': '_source_@timestamp', 'src_ip':'_source_source_ip', 'dst_ip':'_source_destination_ip'},
 		level='conn',
 		kmean_runs=10,
 		num_clusters=51,
		output_folder='C:/Users/tymak/Desktop/AI Stuff/Reproducing state machines',
		data=results,
	)

flexfringe = FlexFringe(
    flexfringe_path="C:/Users/tymak/Desktop/AI Stuff/Flexfringe/flexfringe.exe",
    heuristic_name="alergia",
    data_name="alergia_data",
    slidingwindow=1,
    swsize=10,
)

print(bytes_encoding)

new_df = pd.DataFrame()
new_df["_source_network_bytes"] = bytes_encoding.items()
flexfringe.fit(results,
               sinkson=1,
               sinkcount=100)

df = flexfringe.predict(results)


