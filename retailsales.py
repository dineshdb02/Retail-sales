import pandas as pd
import numpy as np
import pickle 
from datetime import date
import os
import streamlit as st


st.set_page_config(
                    page_title="RETAIL_SALES",
                    page_icon="",
                    layout="wide",
                    initial_sidebar_state="collapsed"
                    )

st.markdown("""
                    <style>
                    div.stButton > button:first-child {
                                                        background-color: #367F89;
                                                        color: white;
                                                        width: 70%}
                    </style>
                """, unsafe_allow_html=True)

st.markdown("""
            <style>
            .center-text {
                text-align: center;
                color: #20CA0C
            }
            </style>
            """,
            unsafe_allow_html=True
            )

class option:
    
    
    Store_values=[ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17,
           18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34,
           35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45]
    
    Dept=[ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 16, 17, 18,
          19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35,
          36, 37, 38, 40, 41, 42, 44, 45, 46, 47, 48, 49, 51, 52, 54, 55, 56,
          58, 59, 60, 67, 71, 72, 74, 77, 78, 79, 80, 81, 82, 83, 85, 87, 90,
          91, 92, 93, 94, 95, 96, 97, 98, 99, 39, 50, 43, 65]
    
    Type={"A":0,"B":1,"C":2}
    
    IsHoliday={True:1,False:0}
    
    
    
tab1=st.tabs(["Weekly_sales"])

with st.form("my_form"):
      
        
    col1,col2,col3 = st.columns([0.5,0.1,0.5])

    with col1:
        
        store= st.selectbox(label='Store',options=option.Store_values)
        
        dept = st.selectbox(label='Department',options=option.Dept)
        
        Type = st.selectbox(label='Type', options=option.Type)
        
        temperature = st.number_input(label='Temperature(Range:1-100)', min_value=-10, max_value=100, value=1)
        
        Fuel_Price = st.number_input(label='Fuel_Price',min_value=0.5,max_value=10.0,value=2.5)
        
    with col3:
        
        Size= st.number_input(label='Size',min_value=34875,max_value=219622)
        
        cpi= st.number_input(label='CPI',min_value=105.45,max_value=250.123)
  
        Unemployment= st.number_input(label='Unemployment',min_value=2.879,max_value=15.123)
        
        Isholiday = st.selectbox(label="IsHoliday",options=option.IsHoliday)
        
        month=st.number_input(label='Month',max_value=12,min_value=1)
        
        year= st.number_input(label='Year',min_value=2000,max_value=2050,value=2010)
        
        submitted = st.form_submit_button("Predict")
        
    col1,col2 = st.columns([0.65,0.35])
    with col2:
        st.caption(body='*Min and Max values are reference only')
        
        
    if submitted:
        
        with open(r"C:/Users/catch/OneDrive/Desktop/demo/sales_model.pkl",'rb') as f:
            weekly_sales=pickle.load(f)
            
            user_input=np.array([store,dept,option.Type[Type],temperature,Fuel_Price,Size,cpi,Unemployment,option.IsHoliday[Isholiday],month,year])
            user_input=user_input.reshape(1,-1)
            y_predict=weekly_sales.predict(user_input)
            predicted=round(y_predict[0],4)
            
            st.header(f"Predicted weekly sales is: {predicted}")