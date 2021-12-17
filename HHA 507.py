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
    outpatientdf = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_DataSci_507/main/Deployment_Streamlit/outpatient_2015.csv')
    return outpatientdf

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

#LOAD DATA
hospital_df = load_hospital()
inpatientdf= load_inpatient()
outpaitentdf= load_outpatient()

##PREVIEW DATA SET
st.header('Hospital Data Preview')
st.markdown('This dataset consists of 5,314 hospitals in the United States.')
st.dataframe(load_hospital())

st.header('Inpatient Data Preview')
st.markdown('DRG CODE AND PAYMENT')
st.dataframe(load_inpatient())

st.header('Outpatient Data Preview')
st.markdown('UNIQUE APC CODES')
st.dataframe(load_outpatient())
##NY HOSPITALS
hospitals_ny = hospital_df[hospital_df['state'] == 'NY']
st.header('Hospitals in New York Summary')
st.markdown('NY HOSPITALS ONLY')
st.dataframe(hospitals_ny)

##NY HOSPITAL BREAKDOWN
table1 = hospitals_ny['hospital_type'].value_counts().reset_index()
st.header('Hospital Types for NY')
st.markdown('5 NY HOSPITALS AND AMOUNTS')
st.dataframe(table1)
st.markdown('ACUTE CARE IS MOST POPULAR IN NY')
st.markdown('SBU IS AN ACUTE CARE FACILITY')
##SBU BREAKDOWN LOOK AT IN AND OUT PATIENT
sbu_inpatient = inpatientdf[inpatientdf['provider_id']==330393]
st.header('FILTERED SBU INPATIENT DATA')
st.markdown('INPATIENT SBU')
st.dataframe(sbu_inpatient)

sbu_outpatient = outpatientdf[outpatientdf['provider_id']==330393]
st.header('Outpatient Data for Stony Brook')
st.markdown('This dataset filters out outpatient data for Stony Brook University Hospital from the main outpatient dataframe')
st.dataframe(sbu_outpatient) 


##MAP
st.subheader('Map of NY Hospital Locations')
st.markdown('USING MAPPING TOOL')
hospitals_ny_gps = hospitals_ny['location'].str.strip('()').str.split(' ', expand=True).rename(columns={0: 'Point', 1:'lon', 2:'lat'}) 	
hospitals_ny_gps['lon'] = hospitals_ny_gps['lon'].str.strip('(')
hospitals_ny_gps = hospitals_ny_gps.dropna()
hospitals_ny_gps['lon'] = pd.to_numeric(hospitals_ny_gps['lon'])
hospitals_ny_gps['lat'] = pd.to_numeric(hospitals_ny_gps['lat'])
st.map(hospitals_ny_gps)


st.title ('Bye for now')




