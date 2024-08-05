# IDS
# Importing the necessary libraries
import pandas as p
import numpy as n
from sklearn.ensemble import IsolationForest
import os
import time

# Read and input the data into Pandas
data = p.read_csv("D:/ShanB/Downloads/Final Project Files/Final Project Files/KDDTrain+.txt")

# If the "id" column is present, drop it from the dataset provided
if "id" in data.columns:
    data = data.drop("id", axis=1)

# Convert categorical variables to binary "dummy" variables for panda to utilise.
data = p.get_dummies(data)

# Creates an Isolation Forest model with specified parameters of 100 estimators and a contamination rate of 1%
model = IsolationForest(
    n_estimators=100,
    contamination=0.01,
    random_state=42)

# Starts the timer
start_time = time.time()

# Fits the inputted dataset to the Isolation Forest Algorithm.
model.fit(data.values)

# starts the predict anomalies function using the Isolation Forest Model.
anomalies = model.predict(data.values)
 
# Stops the timer and calculates the time taken to analyse the dataset. It also stores the caculation to the variablke 'Elapsed_time'
end_time = time.time()
elapsed_time = end_time - start_time

# If an anomaly is detected, print a warning message
if -1 in anomalies:
    print("Warning: Possible intrusion detected!")
else:
    print("No intrusion detected.")

# Print Time taken value from the time variable time
print(f"Elapsed time: {elapsed_time:.2f} seconds")

# Writes the results to a file called IDS_RESULTS.txt with the correct representations
with open("IDS_RESULTS.txt", "w") as f:
    f.write("Intrusion detection results:\n\n")
    if -1 in anomalies:
        f.write("A possible intrusion has been detected within the file\n\n")
        f.write("Intrusion details:\n")
        for i, a in enumerate(anomalies):
            if a == -1:
                f.write(f"Row {i} is an anomaly, Please seek attention!\n")
    else:
        f.write("No intrusion detected.\n\n")

    f.write(f"Elapsed time: {elapsed_time:.2f} seconds\n")

# Opens the file in the default text editor
os.startfile("IDS_RESULTS.txt")
