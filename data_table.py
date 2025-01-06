import streamlit as st
import pandas as pd

def show_data_table():
    data = pd.read_csv('data/developer-survey-2024/survey_results_public.csv')
    st.write(data)