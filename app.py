
## Load packages

import pickle
import streamlit as st

## Loading Model

pickle_in = open("Hearth_model.pkl", 'rb')
classifier = pickle.load(pickle_in)

## Creating pre-processing function

def pred_function(time,serum_sodium,ejection_fraction,age,platelets,serum_creatinine,creatinine_phosphokinase, high_blood_pressure,sex, anaemia, diabetes, smoking):
    if Anaemia == "Yes":
        anaemia = 1
    else:
        anaemia = 0
    if Diabetes == "Yes":
        diabetes = 1
    else:
        diabetes = 0
    if Hypertension == "Yes":
        high_blood_pressure = 1
    else: 
        high_blood_pressure = 0
    if Sex == "Male":
        sex = 1
    else:
        sex = 0
    if Smoking == "Yes":
        smoking = 1
    else:
        smoking = 0
    
    
    ## Creating prediction function

    input_user = pd.DataFrame([[time,serum_sodium,ejection_fraction,age,platelets,serum_creatinine,creatinine_phosphokinase, high_blood_pressure,sex, anaemia, diabetes, smoking]])

    predictor = classifier.predict(input_user)
    
    return predictor


    
