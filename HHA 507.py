
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 13:35:04 2021

@author: apowe
"""

import streamlit as st
import pandas as pd
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 13:35:04 2021

@author: apowe
"""

import streamlit as st
import pandas as pd
import numpy as np 
import time
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go

## Load in the 3 primary csv files for display  

@st.cache
def load_hospitals():
   hospitaldf = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_DataSci_507/main/Deployment_Streamlit/hospital_info.csv')
   return hospitaldf
@st.cache
def load_inatpatient():
    inpatientdf = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_DataSci_507/main/Deployment_Streamlit/inpatient_2015.csv')
    return inpatientdf
@st.cache
def load_outpatient():
    outpatientdf = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_DataSci_507/main/Deployment_Streamlit/outpatient_2015.csv')
    return outpatientdf
    
# FAKE LOADER BAR TO STIMULATE LOADING    
# my_bar = st.progress(0)
# for percent_complete in range(100):
#     time.sleep(0.1)
#     my_bar.progress(percent_complete + 1)
  
st.title('HHA 507 - Streamlit Assignment')
st.write('Amanda Power :sunglasses:') 

# Load the data:     
hospitaldf = load_hospitals()
inpatientdf = load_inatpatient()
outpatientdf = load_outpatient()  

# Preview the dataframes 
st.header('Hospital Data Preview')
st.dataframe(load_hospitals())

st.header('Inpatient Data Preview')
st.dataframe(load_inatpatient())

st.header('Outpatient Data Preview')
st.dataframe(load_outpatient() )


# Create a unique dataframe for New York Hospitals 
hospitals_ny = hospitaldf[hospitaldf['state'] == 'NY']
st.header('Hospitals in New York Summary')
st.dataframe(hospitals_ny)


# Create a breakdown of the hospital types for New York (Q1 ANSWER)
table1 = hospitals_ny['hospital_overall_rating'].value_counts().reset_index()
st.header('Hospital rating for New York')
st.dataframe(table1)


st.subheader('Map of NY Hospital Locations')

hospitals_ny_gps = hospitals_ny['location'].str.strip('()').str.split(' ', expand=True).rename(columns={0: 'Point', 1:'lon', 2:'lat'}) 	
hospitals_ny_gps['lon'] = hospitals_ny_gps['lon'].str.strip('(')
hospitals_ny_gps = hospitals_ny_gps.dropna()
hospitals_ny_gps['lon'] = pd.to_numeric(hospitals_ny_gps['lon'])
hospitals_ny_gps['lat'] = pd.to_numeric(hospitals_ny_gps['lat'])

st.map(hospitals_ny_gps)




# Generate a summary for Stony Brook 
SBUinfo = hospitaldf[hospitaldf['hospital_name'] == 'SUNY/STONY BROOK UNIVERSITY HOSPITAL']

st.header('Stony Brook University Comparison')
st.dataframe(SBUinfo)
st.markdown('In comparison to the other hospitals in New York')

#QUESTIONS 2-6
#2
table2 = outpatientdf['average_estimated_submitted_charges'].value_counts().reset_index()
st.header('outpatient drgs')
st.dataframe(table2)
#3

#4
table4 = outpatientdf['average_total_payments'].value_counts().reset_index()
st.header('outpatient services')
st.dataframe(table4)
#5

#6