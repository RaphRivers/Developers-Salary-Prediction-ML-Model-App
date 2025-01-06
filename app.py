import streamlit as st
from predict_page import show_predict_page
from explore_page import show_explore_page
from data_table import show_data_table

page = st.sidebar.selectbox("Select Action",("Predict", "Explore", "View Source Dataset"))
if page == "Predict":
    show_predict_page()
elif page == "Explore":
    show_explore_page()
else:
    show_data_table()


