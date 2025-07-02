**Car Resale Price Prediction Web App**

An end-to-end machine learning project to predict the resale price of cars using Linear Regression, deployed using Streamlit and GitHub

---
**Project Overview**

This project aims to build a machine learning model that can predict the resale price of a car based on input features like _make_, _model_, _year_, _fuel type_, _transmission_, etc. The model is wrapped in a Streamlit web app and deployed online using GitHub and Streamlit Cloud.

---
**Technologies & Libraries Used:**

**Python**

**pandas** – For data manipulation and preprocessing

**scikit-learn** – For model building, pipelines, and transformations

**pickle** – For saving and loading the trained model and transformers

**Streamlit** – For creating and deploying the web app

**Git & GitHub** – For version control and deployme

---
**Steps Followed:**

**1. Data Cleaning:**
Removed duplicate and missing values
Converted categorical variables into suitable format
Cleaned and standardized inconsistent values (e.g., fuel types, years)

**2. Feature Engineering & Preprocessing:**
Applied ColumnTransformer to handle categorical (OneHotEncoder) and numerical (StandardScaler) features
Created a pipeline to automate preprocessing and model training steps

**4. Model Building:**
Used Linear Regression from scikit-learn to predict car resale price
Split the dataset into training and testing sets
Evaluated model performance using metrics like R² score and MAE

**4. Model Tuning & Saving:**
Tuned pipeline for better feature handling
Serialized the pipeline using pickle for later use in the app

**5. Web App Interface (Streamlit):**
Built a simple user interface for inputs like car model, year, km driven, etc.
Displayed real-time prediction based on user inputs

**6. Deployment:**
Uploaded the project to GitHub
Deployed the app using Streamlit Cloud


---

**Note:**

The predicted resale prices are entirely based on the patterns learned from the dataset used during training. The accuracy and reliability of the results may vary depending on the quality and size of the dataset. For better and more accurate predictions, the model can be improved by training on a larger and more comprehensive dataset.
