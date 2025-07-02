import pandas as pd
import pickle
import streamlit as st
import sklearn

model = pickle.load(open('LinearRegressionModel.pkl', 'rb'))
cars = pd.read_csv('Cleaned_df.csv')

st.title('Refurbished Car Price Predictor')

#input fields
car_name = st.selectbox("Car Name",sorted(cars['name'].unique()))
company = st.selectbox("Company Name",sorted(cars['company'].unique()))
year = st.number_input('Year',min_value=1999,max_value=2025,step=1)
kms_driven = st.number_input('KMS Driven',min_value=0)
fuel = st.selectbox('Fuel type',sorted(cars['fuel_type'].unique()))


if st.button('Predict'):
    input_data = [[car_name,company,year,kms_driven,fuel]]
    prediction = model.predict(pd.DataFrame(input_data,columns=['name','company','year','kms_driven','fuel_type']))
    st.success(f"Estimated Resale Price: ₹{int(prediction[0]):,}")
