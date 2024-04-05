from prescription_data import *

trial_patients = ["Kenny"]


#Remove
for patient in trial_patients:
    prescription = patients[patient]
    prescription.remove(Antidepressant)
    print(patient, prescription)
