import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Data functions for exploration

# define a function to Separate Countries with 1 value counts as threshold to avoid overfitting 
def shorten_cat(cat, threshold): 
    map_cat = {} # Create a dictionary to map the categories into
    for i in range(len(cat)): # iterate through the Country categories
        if cat.values[i] >= threshold: # if the country value is greater than or equals the threshold
            map_cat[cat.index[i]] = cat.index[i]  # Keep the category as is
        else:
            map_cat[cat.index[i]] = 'Other Countries' # If not combine it into a new category 'other countries'
    return map_cat  

# Define a function to add 0.5 value to YearCodePro column for Year of experience 'Less than 1 year' value
def clean_experience(x):
    if x == 'Less than 1 year':
        return 0.5
    return float(x)

# Combine EdLevel values to reduce the number of categories
def shorten_edu(edu):
    if 'Bachelor’s degree' in edu:
        return 'Bachelor’s degree'
    if 'Master’s degree' in edu:
        return 'Master’s degree'
    if 'Professional degree' in edu or 'Other doctoral' in edu:
        return 'PhD'
    return 'Less than a Bachelor’s degree'

@st.cache_data # Cache the data to avoid loading it multiple times

def load_data():
    df = pd.read_csv('data/developer-survey-2024/survey_results_public.csv')
    df = df[['Country', 'EdLevel', 'YearsCodePro','Employment', 'ConvertedCompYearly']]
    df = df[df["ConvertedCompYearly"].notnull()]
    df = df.rename({'ConvertedCompYearly': 'Salary'}, axis=1)
    df = df.dropna()
    
    # Filter where employment was full time
    df = df[df['Employment'] == 'Employed, full-time']   
    df = df.drop('Employment', axis=1) #Drop the column as it is no longer needed
    
    map_country = shorten_cat(df['Country'].value_counts(), 400)
    df['Country'] = df['Country'].map(map_country)
    df = df[df['Salary'] <= 250000]
    df = df[df['Salary'] >= 10000]
    df = df[df['Country'] != 'Other Countries']

    # Transfform the YearsCodePro column to clean the work experience
    df = df.rename({'YearsCodePro': 'Years of Experience'}, axis=1)
    df['Years of Experience'] = df['Years of Experience'].apply(clean_experience)
    

    # Transform the EdLevel 
    df['EdLevel'] = df['EdLevel'].apply(shorten_edu)
    return df
df = load_data()

def show_explore_page():
    st.title('Explore 2024 Developers Salary')

    st.write("""#### Source: Stack Overflow Developer Survey 2024""")

    # Pie chart for Country counts
    data = df["Country"].value_counts()

    fig1, ax1 = plt.subplots()
    ax1.pie(data, labels=data.index, autopct='%1.1f%%', startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    st.write("""#### Percentage of Developers Data per Country""")
    st.pyplot(fig1)

    # Bar chart for Mean Salary per Country
    st.write("""#### Average Salary per Country""")
    data = df.groupby('Country')['Salary'].mean().sort_values(ascending=True)

    # Plot the chart
    st.bar_chart(data)

    # Line chart for Years of Professional Coding Experience
    st.write("""#### Average Salary Based on Years of Professional Experience""")
    data = df.groupby('Years of Experience')['Salary'].mean().sort_values(ascending=True)

    # Plot the chart
    st.line_chart(data)