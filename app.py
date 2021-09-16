
## Load packages

import pickle
import streamlit as st

## Loading Model

pickle_in = open("Hearth_model.pkl", 'rb')
classifier = pickle.load(pickle_in)

## Designing app

def pred_function(time,serum_sodium,ejection_fraction,age,platelets,serum_creatinine,creatinine_phosphokinase, high_blood_pressure,sex, anaemia, diabetes, smoking):
    if Anaemia == "Yes":
        anaemia = 1
    else:
        anaemia = 0
    
    


    
