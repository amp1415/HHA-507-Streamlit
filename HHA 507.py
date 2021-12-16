import streamlit as st
import pandas as pd
import numpy as np
import time

##LOAD IN CSV 
@st.cache
def load_hospital():
    hospital_df= pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_DataSci_507/main/Deployment_Streamlit/hospital_info.csv')
    return hospital_df
@st.cache 
def load_inpatient():
    inpatientdf =pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_DataSci_507/main/Deployment_Streamlit/inpatient_2015.csv')
    return inpatientdf
@st.cache
def load_outpatient():
    outpaitent= pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_DataSci_507/main/Deployment_Streamlit/outpatient_2015.csv')

# FAKE LOADER BAR TO STIMULATE LOADING    
# my_bar = st.progress(0)
# for percent_complete in range(100):
#     time.sleep(0.1)
#     my_bar.progress(percent_complete + 1)

st.title('HHA 507 - Final Assignment')
st.write('Amanda Power :sunglasses:')
st.write('Questions:')
st.write('1. How does Stony Brook compare to the rest of NY?')
st.write('2. Which APC code has the largest number of services for New York?')
st.write('3. Where are most of the hospitals located in New York state?')
st.write('4. How had better care timliness? NY or CA')

#LOAD DATA
hospital_df = load_hospital()
inpatientdf= load_inpatient()
outpaitentdf= load_outpatient()

##PREVIEW DATA SET
st.header('Hospital Data Preview')
st.markdown('This dataset consists of 5,314 hospitals in the United States. Each row represents a unique hospital, referenced by "provider_id", and additional info for each location.')
st.dataframe(load_hospital())

st.header('Inpatient Data Preview')
st.markdown('This dataset consists of drg codes for multiple inpatient locations. Each row represents a unique drg code, referenced by "drg_definition", along with payment details for each code.')
st.dataframe(load_inpatient())

st.header('Outpatient Data Preview')
st.markdown('This dataset consists of apc codes for multiple outpatient locations. Each row represents a unique apc code, referenced by "apc", along with service and payment details for each code.')
st.dataframe(load_outpatient())
