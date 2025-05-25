from forecast_engine.src.utils import (
    read_csv_file,
    timeseries_format_validity_checker,
    timeseries_date_granularity_validity_checker,
    )

import pandas as pd
import altair as alt
import matplotlib.pyplot as plt
from prophet import Prophet
import streamlit as st
import os


NEW_TIME_SERIES_COLUM_NAME= "ds"
NEW_DATA_COLUM_NAME= "y"
REQUIRED_TIMESERIES_DATA_DATE_FORMAT= "%d-%m-%Y"
DATA_GRANULARITY_OPTIONS={
    "daily": "D",
    "weekly": "W",
    "monthly": "M"
}

PREDICTION_PERIOD=30
EXPECTED_ONE_FULL_CYCLE_PERIOD= 60


if "part_1" not in st.session_state:
    st.session_state["part_1"] = False
if "part_2" not in st.session_state:
    st.session_state["part_2"] = False


st.title("Welcome to Forecast Engine App")
st.caption("This app is for demostration purposes only!")
st.header("")

uploaded_file = st.file_uploader(
    label="Choose a CSV file", 
    accept_multiple_files=False
)

##Part 1 of data analysis
if uploaded_file:
    st.session_state["part_1"] = True
    df= read_csv_file(file_path= uploaded_file)
    ALL_COLUMNS= df.columns.tolist()
    TIME_SERIES_COLUM_NAME= st.selectbox(
        label= "Please select the date column. The date MUST be in the `DD-MM-YYYY` format",
        options= ALL_COLUMNS,
        placeholder= "Date column ...",
        index=None
        )
    
    if uploaded_file and TIME_SERIES_COLUM_NAME != None:
        date_format_validity_status= timeseries_format_validity_checker(
            required_format= REQUIRED_TIMESERIES_DATA_DATE_FORMAT, 
            dataframe=df, 
            date_column= TIME_SERIES_COLUM_NAME,
            )

        if not date_format_validity_status:
            st.write("The date column is not in the `DD-MM-YYYY` required format. Please upload a correctly formatted file.")
        
        elif date_format_validity_status:
            DATA_COLUM_NAME= st.selectbox(
                label= "Please select the target column you wish to predict",
                options= [i for i in ALL_COLUMNS if i != TIME_SERIES_COLUM_NAME],
                placeholder= "Target column ...",
                index=None
                )
            
            if DATA_COLUM_NAME != None:
                df= df[[DATA_COLUM_NAME, TIME_SERIES_COLUM_NAME]]
                df= df.rename(columns={
                    TIME_SERIES_COLUM_NAME: NEW_TIME_SERIES_COLUM_NAME, 
                    DATA_COLUM_NAME: NEW_DATA_COLUM_NAME
                    })
                df[NEW_TIME_SERIES_COLUM_NAME]= pd.to_datetime(
                    df[NEW_TIME_SERIES_COLUM_NAME], 
                    format=REQUIRED_TIMESERIES_DATA_DATE_FORMAT
                    )
                df= df.set_index(NEW_TIME_SERIES_COLUM_NAME)
                
                
                DATA_GRANULARITY = st.selectbox(
                    label= "Please select the granularity/resolution of your data",
                    options= list(DATA_GRANULARITY_OPTIONS.keys()),
                    placeholder="Data granularity...",
                    index=None,
                )
                
                if DATA_GRANULARITY != None:
                    data_granularity_validity_status= timeseries_date_granularity_validity_checker(
                        stated_granularity= DATA_GRANULARITY_OPTIONS[DATA_GRANULARITY], 
                        dataframe=df
                        )
                    if data_granularity_validity_status:
                        df= df.resample(DATA_GRANULARITY_OPTIONS[DATA_GRANULARITY]).mean()
                        df= df.reset_index(drop=False)
                        df= df.sort_values(by=NEW_TIME_SERIES_COLUM_NAME, ascending=True)
                        
                        if st.button("Generate Plot") == True:
                            st.session_state["part_2"] = True
                            Chart= (alt.Chart(df.reset_index()).mark_line().encode(
                                alt.X(NEW_TIME_SERIES_COLUM_NAME, title=TIME_SERIES_COLUM_NAME),
                                alt.Y(NEW_DATA_COLUM_NAME, title=DATA_COLUM_NAME),
                                tooltip=[NEW_TIME_SERIES_COLUM_NAME]
                            )).interactive()
                            st.altair_chart(Chart)
                        else:
                            st.session_state["part_2"] = False
                    else:
                        st.write("There are missing data points for the selected granularity. Please select another option.")
else:
    st.session_state["part_1"] = False


##Part 2 of data analysis
# if st.session_state["part_1"] and st.session_state["part_2"]:
#     pass


# clf= Prophet()
# clf.add_seasonality(
#     name=DATA_GRANULARITY_OPTIONS[DATA_GRANULARITY], 
#     period=EXPECTED_ONE_FULL_CYCLE_PERIOD, 
#     fourier_order=5
#     )
# clf.fit(df)
# future = clf.make_future_dataframe(periods=PREDICTION_PERIOD, freq=DATA_GRANULARITY_OPTIONS[DATA_GRANULARITY])
# forecast = clf.predict(future)

# clf.plot(forecast, xlabel= TIME_SERIES_COLUM_NAME, ylabel= DATA_COLUM_NAME)
# plt.tight_layout()
# plt.show()