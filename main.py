from forecast_engine.src.utils import (
    timeseries_format_validity_checker
    )

import pandas as pd
import matplotlib.pyplot as plt
from prophet import Prophet
import streamlit as st
import os

DATA_DIRECTORY_PATH= "/workspaces/data/"
FILE_NAME= [
    "stationary_sales_data_date_valid.csv",
    "non_stationary_sales_data_date_valid.csv", 
    "non_stationary_sales_data_date_invalid.csv",
    ][1]
TIME_SERIES_COLUM_NAME= "date_time"
NEW_TIME_SERIES_COLUM_NAME= "ds"
DATA_COLUM_NAME= "sales"
NEW_DATA_COLUM_NAME= "y"
REQUIRED_TIMESERIES_DATA_DATE_FORMAT= "%d-%m-%Y"
DATA_GRANULARITY_OPTIONS={
    "daily": "D",
    "weekly": "W",
    "monthly": "M"
}
DATA_GRANULARITY= "daily"
PREDICTION_PERIOD=30
EXPECTED_ONE_FULL_CYCLE_PERIOD= 60




st.title("The Forecast Engine App")
st.header("")
st.caption("This app is for demostration purposes only!")






df= pd.read_csv(DATA_DIRECTORY_PATH+FILE_NAME)
df= df.dropna(how="any", axis="rows")
df= df.rename(columns={
    TIME_SERIES_COLUM_NAME: NEW_TIME_SERIES_COLUM_NAME, 
    DATA_COLUM_NAME: NEW_DATA_COLUM_NAME
    })

date_format_validity_status= timeseries_format_validity_checker(
    required_format= REQUIRED_TIMESERIES_DATA_DATE_FORMAT, 
    dataframe=df, 
    date_column= NEW_TIME_SERIES_COLUM_NAME
    )


if date_format_validity_status:
    df[NEW_TIME_SERIES_COLUM_NAME]= pd.to_datetime(
        df[NEW_TIME_SERIES_COLUM_NAME], 
        format=REQUIRED_TIMESERIES_DATA_DATE_FORMAT
        )

    df= df.set_index(NEW_TIME_SERIES_COLUM_NAME)
    df= df.resample(DATA_GRANULARITY_OPTIONS[DATA_GRANULARITY]).mean()
    df= df.reset_index(drop=False)
    df= df.sort_values(by=NEW_TIME_SERIES_COLUM_NAME, ascending=True)

    clf= Prophet()
    clf.add_seasonality(
        name=DATA_GRANULARITY_OPTIONS[DATA_GRANULARITY], 
        period=EXPECTED_ONE_FULL_CYCLE_PERIOD, 
        fourier_order=5
        )
    clf.fit(df)
    future = clf.make_future_dataframe(periods=PREDICTION_PERIOD, freq=DATA_GRANULARITY_OPTIONS[DATA_GRANULARITY])
    forecast = clf.predict(future)

    clf.plot(forecast, xlabel= TIME_SERIES_COLUM_NAME, ylabel= DATA_COLUM_NAME)
    plt.tight_layout()
    plt.show()