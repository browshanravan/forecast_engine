import pandas as pd
import streamlit as st
from prophet import Prophet

@st.cache_data(show_spinner= "Reading your data...")
def read_csv_file(file_path):
    df= pd.read_csv(file_path)
    return df.dropna(how="any", axis="rows")


def timeseries_format_validity_checker(required_format, dataframe, date_column):
    try:
        pd.to_datetime(dataframe[date_column], format=required_format)
        date_format_validity_status= True
    except:
        date_format_validity_status= False
    
    return date_format_validity_status


def timeseries_date_granularity_validity_checker(stated_granularity, dataframe):
    if dataframe.resample(stated_granularity).mean().isna().sum().values == 0:
        data_granularity_validity_status= True
    else:
        data_granularity_validity_status= False
    
    return data_granularity_validity_status


@st.cache_resource(show_spinner="Modelling the data...")
def fit_model_to_data(dranularity, full_cycle, dataframe):
    clf= Prophet()
    clf.add_seasonality(
    name= dranularity, 
    period= full_cycle, 
    fourier_order=5
    )
    clf.fit(dataframe)
    
    return clf