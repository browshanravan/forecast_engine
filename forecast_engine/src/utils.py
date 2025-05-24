import pandas as pd

def timeseries_format_validity_checker(required_format, dataframe, date_column):
    try:
        pd.to_datetime(dataframe[date_column], format=required_format)
        date_format_validity_status= True
    except:
        date_format_validity_status= False
    
    return date_format_validity_status