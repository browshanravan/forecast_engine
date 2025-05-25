import pandas as pd


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
    try:
        dataframe.resample(stated_granularity).mean()
        data_granularity_validity_status= True
    except:
        data_granularity_validity_status= False
    
    return data_granularity_validity_status
