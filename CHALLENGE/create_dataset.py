import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta
import os

# ========================================================
# =========== ⚠ PROVIDE YOUR USERNAME HERE ==============
# ========================================================

username = "EDGARJN" # Replace with your username

# you can edit this to any number of patients you want
num_patients = 100

# ========================================================
# =========== ================= 🤖
# ========================================================

# create new directory with name username
if not os.path.exists(username):
    # newFolder = os.getcwd()
    # os.path.join(newFolder,)
    os.makedirs(username)


# Set random seed for reproducibility
random.seed(123)
np.random.seed(123)

# Generate sample data
# you can edit this to any number of patients you want
num_patients = 100

patient_ids = np.array(['P{:03}'.format(i) for i in range(1, num_patients + 1)])
admission_dates = np.array([datetime(2022, 1, 1) + timedelta(days=random.randint(0, 365)) for _ in range(num_patients)])
discharge_dates = np.array([admission + timedelta(days=random.randint(1, 14)) for admission in admission_dates])
diagnoses = np.random.choice(['Heart Failure', 'Pneumonia', 'Stroke', 'Heart Attack', 'Asthma', None, '', ], size=num_patients)
comorbidities = np.random.choice(['Hypertension', 'Diabetes', None, '', ], size=num_patients)
medications = np.array([['ACE Inhibitors', 'Diuretics'],
                        ['Antibiotics', 'Insulin'],
                        ['Antiplatelets', 'Blood Pressure Medications'],
                        ['Statins', 'Beta-blockers', 'Aspirin', 'Insulin'],
                        ['Inhalers', 'Corticosteroids'], None])
length_of_stay = np.random.randint(-1, 10, size=num_patients)
readmission_status = np.random.choice(['Yes', 'No', None], size=num_patients, p=[0.2, 0.7, .1])
ages = np.random.randint(18, 90, size=num_patients)
genders = np.random.choice(['Male', 'Female'], size=num_patients)

# Create the DataFrame
data = np.vstack((patient_ids, admission_dates, discharge_dates, diagnoses, comorbidities,
                  np.random.choice(medications, size=num_patients),
                  length_of_stay, readmission_status, ages, genders)).T

columns = ['Patient ID', 'Admission Date', 'Discharge Date', 'Primary Diagnosis', 'Comorbidities',
           'Medication History', 'Length of Stay', 'Readmission Status', 'Age', 'Gender']

df = pd.DataFrame(data, columns=columns)


# ========================================================
# Save the DataFrame to a CSV file named "challenge_initial_dataset.csv"
# ========================================================
df.to_csv(f"{username}/challenge_initial_dataset.csv",index=False)