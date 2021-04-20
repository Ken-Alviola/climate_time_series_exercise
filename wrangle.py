import numpy as np
import pandas as pd

def get_manila():
    major_city = pd.read_csv('GlobalLandTemperaturesByMajorCity.csv')
    manila = major_city[major_city.City == 'Manila']
    return manila

def clean_manila(df):
    df = df.fillna(df.mean())
    return df


def prepare_manila(df):
    df.dt = pd.to_datetime(df.dt)
    df = df.set_index('dt').sort_index()
    df['month'] = df.index.month_name()
    df['year'] = df.index.year
    return df

def wrangle_manila():
    df = get_manila()
    df = clean_manila(df)
    df = prepare_manila(df)
    return df