# -*- coding: utf-8 -*-
"""
Created on Tue May  2 17:21:58 2023

@author: durka
"""

import numpy as np
import pickle
import streamlit as st

loaded_rf_model = pickle.load(open('trained_rf_model.sav', 'rb'))

#create a function for prediction
def sleep_efficiency(input_data):
    

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting our one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

    prediction = loaded_rf_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction [0] >=0.85):
        return'The person is sleep efficient'
    else:
        return'The person is not sleep efficient'
        
        
        
        
def main():
    
    #giving a title
    st.title('Sleep efficiency Web App')
    
    #getting the input data from the user
    
    Age = st.text_input('Age')
    Sleep_duration = st.text_input('Sleep duration')
    Rem_sleep_percentage = st.text_input('REM sleep percentage')
    Deep_sleep_percentage = st.text_input('Deep sleep percentage')
    Light_sleep_percentage = st.text_input('Light sleep percentage')
    Awakenings = st.text_input('Awakenings')
    Caffeine_consumption = st.text_input('Caffeine consumption')
    Alcohol_consumption = st.text_input('Alcohol consumption')
    Exercise_frequency = st.text_input('Exercise frequency')
    Gender_Female = st.text_input('Female')
    Gender_Male = st.text_input('Male')
    Smoking_status_No = st.text_input('Does not smoke')
    Smoking_status_Yes = st.text_input('Smokes')
    
    #code for prediction
    sleep_efficiency_status = ''
    
    #creating a button for prediction
    if st.button('Sleep Efficiency Status'):
        sleep_efficiency_status = sleep_efficiency([Age, Sleep_duration, Rem_sleep_percentage, Deep_sleep_percentage, Light_sleep_percentage, Awakenings,Caffeine_consumption, Alcohol_consumption, Exercise_frequency,Gender_Female, Gender_Male, Smoking_status_No,Smoking_status_Yes])
        
    st.success(sleep_efficiency_status)
    
    
    
    
    
if __name__ == '__main__':
    main() 