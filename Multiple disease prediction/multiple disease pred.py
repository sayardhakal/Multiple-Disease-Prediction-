# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 16:10:26 2023

@author: user
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# loading a save models

diabetes_model = pickle.load(open("C:/Users/user/Downloads/Diabetes Prediction/trained_model.sav", 'rb'))
breast_model = pickle.load(open("C:/Users/user/Desktop/Multiple disease prediction/breast_model.sav", 'rb'))
heart_model = pickle.load(open("C:/Users/user/Desktop/Multiple disease prediction/heart_model.sav", 'rb'))


# creating a navbar for navigation

with st.sidebar:
    
    selected = option_menu("Multiple Disease Prediction System", 
                           
                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Breast Cancer Prediction'],
                           
                           icons= ['activity', 'heart-pulse', 'person'],
                           
                           default_index = 0)  # this means we have three button and making index 0 indicate when we open the web it should open index 0 button as default.



 
    
# Diabetes Prediction Page

if (selected == 'Diabetes Prediction'):
    
    # title of page
    st.title("Diabetes Prediction System")
    
    
    # getting the input data from the user
    # columns for input fields 
    
    col1,col2,col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
        
    with col2:
        Glucose = st.text_input('Level of Glucose')
        
    with col3:
        BloodPressure = st.text_input('Level of BloodPressure')
        
    with col1:
        SkinThickness = st.text_input('Level of SkinThickness')
        
    with col2:
        Insulin = st.text_input('Level of Insulin')
        
    with col3:
        BMI = st.text_input('Level of BMI')
        
    with col1:
        DiabetesPedigreeFunction = st.text_input('Level of DiabetesPedigreeFunction')
        
    with col2:
        Age = st.text_input("Age of a person")
    
    
    # code for a prediction
    
    diab_diagnosis = ''
    
    # creating a button for prediction
    
    if st.button('Diabetes Test'):
        diab_prediction = diabetes_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]]) # we have used double list to indicate that we are predicting for one data point.
        
        if (diab_prediction[0]==1):
            diab_diagnosis = "The Person has Diabetes."
            
        else:
            diab_diagnosis = "The Person has not Diabetes."
            
    st.success(diab_diagnosis)
        
        
    
    
    
    
# Heart Disease Prediction    
if (selected == 'Heart Disease Prediction'):
    
    # title of page
    st.title("Heart Disease Prediction System")
    
    # getting the input data from the user
    # columns for input fields
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input("Enter a age of a person")
        
    with col2:
        sex = st.text_input("Enter a sex")
        
    with col3:
        cp = st.text_input("Enter a cp")
        
    with col1:
        trestbps = st.text_input("Enter a trestbps")
        
    with col2:
        chol = st.text_input("Enter a chol")
        
    with col3:
        fbs = st.text_input("Enter a fbs")
        
    with col1:
        restecg = st.text_input("Enter a restecg")
        
    with col2:
        thalach = st.text_input("Enter a thalach")
        
    with col3:
        exang = st.text_input("Enter a exang")
        
    with col1:
        oldpeak = st.text_input("Enter a oldpeak")
        
    with col2:
        slope = st.text_input("Enter a slope")
        
    with col3:
        ca = st.text_input("Enter a ca")
        
    with col1:
        thal = st.text_input("Enter a thal")
        
        
    
    # code for prediciton 
    
    heart_diagnosis = ''
    
    
    #creating a button for prediction
    
    if st.button('Heart Disease Test'):
        heart_prediction = heart_model.predict([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])
        
        
        if (heart_prediction[0]==0):
            heart_diagnosis = "The Person has a healty heart"
            
        else:
            heart_diagnosis = "The Person has a defective heart."
            
            
    st.success(heart_diagnosis)


    

    
    
# Breast Cancer Prediction    
if (selected == 'Breast Cancer Prediction'):
    
    # title of page
    st.title("Breast Cancer Prediction System")
    
    
    # getting the input data from the user
    # columns for input fields
    
    col1,col2,col3,col4,col5 = st.columns(5)
    
    with col1:
        mean_radius = st.text_input("Enter a mean radius")
    with col2:
        mean_texture = st.text_input("Enter a mean texture")
    with col3:
        mean_perimeter = st.text_input("Enter a mean perimeter")
    with col4:
        mean_area = st.text_input("Enter a mean area")
    with col5:
        mean_smoothness = st.text_input("Enter a mean smoothness")
    with col1:
        mean_compactness = st.text_input("Enter a mean compactness")
    with col2:
        mean_concavity = st.text_input("Enter a mean concavity")
    with col3:
        mean_concave_points = st.text_input("Enter a mean concave points")
    with col4:
        mean_symmetry = st.text_input("Enter a mean symmetry")
    with col5:
        mean_fractal_dimension = st.text_input("Enter a mean fractal dimension")
    with col1:
        radius_error = st.text_input("Enter a radius error")
    with col2:
        texture_error = st.text_input("Enter a texture error")
    with col3:
        perimeter_error = st.text_input("Enter a perimeter error")
    with col4:
        area_error = st.text_input("Enter an area error")
    with col5:
        smoothness_error = st.text_input("Enter a smoothness error")
    with col1:
        compactness_error = st.text_input("Enter a compactness error")
    with col2:
        concavity_error = st.text_input("Enter a concavity error")
    with col3:
        points_error = st.text_input("Enter a concave points error")
    with col4:
        symmetry_error = st.text_input("Enter a symmetry error")
    with col5:
        fractal_dimension_error = st.text_input("Enter a fractal dimension error")
    with col1:
        worst_radius = st.text_input("Enter a worst radius")
    with col2:
        worst_texture = st.text_input("Enter a worst texture")
    with col3:
        worst_perimeter = st.text_input("Enter a worst perimeter")
    with col4:
        worst_area = st.text_input("Enter a worst area")
    with col5:
        worst_smoothness = st.text_input("Enter a worst smoothness")
    with col1:
        worst_compactness = st.text_input("Enter a worst compactness")
    with col2:
        worst_concavity = st.text_input("Enter a worst concavity")
    with col3:
        worst_concave_points = st.text_input("Enter a worst concave points")
    with col4:
        worst_symmetry = st.text_input("Enter a worst symmetry")
    with col5:
        worst_fractal_dimension = st.text_input("Enter a worst fractal dimension")
        

    
    # code for prediction
    
    breast_diagnosis = ''
    
    
    # creating a button for prediction 
    
    if st.button('Breast Cancer Test'):
        breast_prediction = breast_model.predict([[mean_radius,mean_texture,mean_perimeter,mean_area,mean_smoothness,mean_compactness,mean_concavity,mean_concave_points,mean_symmetry,mean_fractal_dimension,radius_error,texture_error,perimeter_error,area_error,smoothness_error,compactness_error,concavity_error,points_error,symmetry_error,fractal_dimension_error,worst_radius,worst_texture,worst_perimeter,worst_area,worst_smoothness,worst_compactness,worst_concavity,worst_concave_points,worst_symmetry,worst_fractal_dimension]])
        
        if (breast_prediction[0]==0):
            breast_diagnosis = 'The Breast cancer is Malignant'
            
        else:
            breast_diagnosis = 'The Breast Cancer is Benign'
            
    st.success(breast_diagnosis)

    

    
    
    
    
    
    
    