# 2025 Developers Salary Prediction App
![App Image](https://github.com/RaphRivers/Developers-Salary-Prediction-ML-Model-App/blob/main/pred-1.png)

Discover your earning potential with this interactive Salary Prediction App, powered by Python and Streamlit. Simply select your country, education level, and years of experience, and get an instant salary estimate. Perfect for developers curious about 2025 salary trends worldwide, this tool delivers insights in a fast and engaging way.

# Features
- Interactive UI: Users can input their details such as country, education level, and years of experience.
- Real-time Predictions: The app leverages a pre-trained machine learning model to estimate salaries instantly.
- Country and Education Encoding: Encoded input data ensures compatibility with the model.
- Works with any data source E.g Stack overflow survey data

![Explore Data Source Page](https://github.com/RaphRivers/Developers-Salary-Prediction-ML-Model-App/blob/main/explore.png)

# How It Works
### Inputs: 
The user selects their country and education level, then adjusts the slider for years of experience.
Prediction: On submitting the inputs, the app processes the data using a machine learning model to predict the salary.
### Output: 
The estimated salary is displayed on the app interface.
Model and Code Source
The machine learning model used in this app was pre-trained and serialized using the pickle library. It includes:

# A regression model for salary prediction.
Label encoding for country and education level inputs.
This app is adapted from the original implementation available at patrickloeber/ml-app-salaryprediction.

# Technologies Used
Streamlit: For building the user interface.
Python: Core programming language.
Pickle: For saving and loading the serialized model.
NumPy: For numerical operations.
Getting Started
To run the app locally:

# Clone this repository.
- Install the required libraries using pip install -r requirements.txt.
- Place the serialized model file (salary_prediction_model.pkl) in the root directory.
- Run the app with streamlit run app.py.
  
Disclaimer: Please note this app is intended for education and demonstration purposes and may not reflect actual market conditions or salary trends.
