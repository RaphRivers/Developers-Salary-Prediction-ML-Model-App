import streamlit as st
import pickle
import numpy as np

# Def function to load the pickled model
def load_model():
    with open('salary_prediction_model.pkl', 'rb') as file: # Read binary mode
        data = pickle.load(file)
    return data

# Execute the function
data = load_model()

# Access the different encoding keys
regressor_model = data['model']
le_country = data['le_country'] 
le_edlevel = data['le_edlevel']

# Defining a function to create a prediction page
def show_predict_page():
    # Title widget
    st.title('2025 Developers Salary Prediction')
    
    st.write("""### Please enter some information to predict your salary""")
    
    countries = (                                        
        "Australia",
        "Brazil",
        "Canada",
        "France",
        "Germany",
        "India",
        "Italy",
        "Netherlands",
        "United Kingdom of Great Britain and Northern Ireland",     
        "United States of America", 
        "Ukraine",                                              
        "Spain"         
    )

    education = (
        'Post grad', 
        'Master’s degree', 
        'Bachelor’s degree',
        'Less than a Bachelor’s degree'

    )
    
    # Create a select box for country
    country = st.selectbox("Select Country", countries)

    # Create a select box for country
    education = st.selectbox("Education Level", education)

    # Create a slider input for years of experience
    experience = st.slider("Years of Experience", 0, 10, 3)

    # Add Button to predict salary
    submit = st.button("Predict Salary")
    if submit:
        X = np.array([[country, education, experience]])
        X[:, 0] = le_country.transform(X[:, 0])
        X[:, 1] = le_edlevel.transform(X[:, 1])
        X = X.astype(float)
        salary = regressor_model.predict(X) # Calculate the predictions
        st.subheader(f"The estimated salary for your selection is ${salary[0]:.2f}") # Display Predictions