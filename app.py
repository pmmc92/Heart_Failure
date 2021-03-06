
## Load packages

import pickle
import streamlit as st
import pandas as pd
import sklearn
from xgboost import XGBClassifier

## Loading Model

pickle_in = open("hearth_model.pkl", 'rb')
classifier = pickle.load(pickle_in)

## Creating pre-processing function

Hypertension = 0
Diabetes = 0
Sex = 0
Smoking = 0

def pred_function(serum_sodium,ejection_fraction,age,platelets,serum_creatinine,creatinine_phosphokinase, Hypertension,Sex, Anaemia, Diabetes, Smoking):
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
    if Smoking == "Smoker":
        smoking = 1
    else:
        smoking = 0
    
    
    ## Creating prediction function

    input_user = pd.DataFrame([[age,anaemia,creatinine_phosphokinase, diabetes, ejection_fraction, high_blood_pressure, platelets, serum_creatinine, serum_sodium, sex, smoking]], columns = ["age","anaemia","creatinine_phosphokinase", "diabetes", "ejection_fraction", "high_blood_pressure", "platelets", "serum_creatinine", "serum_sodium", "sex", "smoking"])

    predictor = classifier.predict(input_user)
    
    return predictor

## Main page

st.set_page_config(page_title="Predicting Heart Failure", page_icon = ":blue_heart:")

def main():
    st.title("Heart Failure Prediction")

    st.markdown("This simple app uses a machine learning algorithm to predict the probability of death by heart failure in a 6 month period. To know more about this project click [here](https://github.com/pmmc92/Heart_Failure/blob/master/README.md)")

    Sex = st.radio("Gender",("Male","Female"))
    age = st.slider("Age", min_value = 18, max_value = 110, step = 1)
    Anaemia = st.radio("Does the patient has anaemia?",("Yes","No"))
    Diabetes = st.radio("Does the patient has diabetes?",("Yes","No"))
    Smoking = st.radio("Smoking status",("Smoker","Non-Smoker"))
    platelets = st.number_input("Platelets (Kp/ml)")
    serum_sodium = st.number_input("Sodium blood level (mEq/L)")
    serum_creatinine = st.number_input("Serum Creatinine (mg/dl)")
    creatinine_phosphokinase = st.number_input("CPK blood level (ug/L)")
    ejection_fraction = st.number_input("Ejection Fraction (%)")

    if st.button("Predict"):
        if ((platelets ==  0) or (serum_sodium == 0) or (serum_creatinine == 0) or (creatinine_phosphokinase == 0) or (ejection_fraction == 0)):
            st.warning('Please fill all fields')
            st.stop()
        else:
            result = pred_function(serum_sodium,ejection_fraction,age,platelets,serum_creatinine,creatinine_phosphokinase, Hypertension,Sex, Anaemia, Diabetes, Smoking)
            if result == 1:
                st.success("High probability of death within 1 year")
            else:
                st.success("Low probability of death within 1 year")

if __name__=='__main__': 
    main()
    
