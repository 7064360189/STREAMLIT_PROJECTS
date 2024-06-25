import streamlit as st 
st.title("WELCOME TO BMI CALCULATOR")
weight = st.number_input("enter your weight(in kgs)")
status = st.radio('select your height format :',('cms','meters','feet'))
if(status == 'cms'):
    height = st.number_input('centimeters')
    try:
        bmi = weight / ((height/100)**2)
    except:
        st.text("enter some value of height")
elif(status == 'meters'):
    height = st.number_input('meters')
    try:
        bmi = weight / (height**2)
    except:
        st.text("enter some value of height")
else:
    height = st.number_input('feet')
    try:
        bmi = weight / (((height/3.28))**2)
    except:
        st.text("enter some value of height")
if(st.button('calculate bmi')):
    st.text("Your BMI Index is {}.".format(bmi))
    if(bmi < 16):
        st.error("you are extremely under weight")
    elif(bmi >= 16 and bmi < 18.5):
        st.warning("You are underweight")
    elif(bmi >= 18.5 and bmi < 25):
        st.success("Healthy")   
    elif(bmi >= 25 and bmi < 30):
        st.warning("You are overweight")
    elif(bmi >= 30 ):
        st.error("You are extremely overweight")        
