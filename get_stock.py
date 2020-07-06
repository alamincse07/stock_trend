import requests
import pandas as pd
import csv 
import os 
import sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt 

def get_charts(ticker):

    SYM = ticker.upper()

    API_KEY = ''

    end_date = '2020-07-02'
    start_date = '2020-02-11'
    dates = pd.date_range(start_date, end_date)
    df1 = pd.DataFrame(index=dates)

    if not os.path.exists(f'data/{SYM}.csv'):
        r   = requests.get(f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={SYM}&apikey={API_KEY}&datatype=csv')
        ma  = requests.get(f'https://www.alphavantage.co/query?function=SMA&symbol={SYM}&interval=daily&time_period=50&series_type=open&apikey={API_KEY}&datatype=csv')
        ma2 = requests.get(f'https://www.alphavantage.co/query?function=SMA&symbol={SYM}&interval=daily&time_period=200&series_type=open&apikey={API_KEY}&datatype=csv')
        trend = requests.get(f'https://www.alphavantage.co/query?function=AROON&symbol={SYM}&interval=daily&time_period=14&apikey={API_KEY}&datatype=csv')
        strength = requests.get(f'https://www.alphavantage.co/query?function=ADX&symbol={SYM}&interval=daily&time_period=10&apikey={API_KEY}&datatype=csv')

        with open(f'data/{SYM}.csv', 'wb') as f:
            f.write(r.content)
        with open(f'data/{SYM}_AV.csv', 'wb') as f:
            f.write(ma.content)
        with open(f'data/{SYM}_2AV.csv', 'wb') as f:
            f.write(ma2.content)
        with open(f'data/{SYM}_trend.csv', 'wb') as f:
            f.write(trend.content)
        with open(f'data/{SYM}_strength.csv', 'wb') as f:
            f.write(strength.content)

    df =  pd.read_csv(f'data/{SYM}.csv', index_col='timestamp', parse_dates=True, usecols=['timestamp', 'high', 'close'], na_values=['nan'])  
    df2 = pd.read_csv(f'data/{SYM}_AV.csv', index_col='time', parse_dates=True, usecols=['time', 'SMA'], na_values=['nan']) 
    df3 = pd.read_csv(f'data/{SYM}_2AV.csv', index_col='time', parse_dates=True, usecols=['time', 'SMA'], na_values=['nan']) 
    df4 = pd.read_csv(f'data/{SYM}_trend.csv', index_col='time', parse_dates=True, usecols=['time', 'Aroon Up'], na_values=['nan']) 
    df5 = pd.read_csv(f'data/{SYM}_strength.csv', index_col='time', parse_dates=True, usecols=['time', 'ADX'], na_values=['nan']) 
    df2.rename(columns = {'SMA':'50 DAY MOVING AVG'}, inplace = True) 
    df3.rename(columns = {'SMA':'200 DAY MOVING AVG'}, inplace = True) 
    df4.rename(columns = {'Aroon Up':'Up Trend'}, inplace = True) 
    df4.rename(columns = {'Aroon Down':'Down Trend'}, inplace = True) 
    df1 = df1.join(df)
    df1 = df1.join(df2)
    df1 = df1.join(df3)
    df1 = df1.join(df4)
    df1 = df1.join(df5)
    df1 = df1.dropna()

    df1.plot()
    plt.title(SYM)
    plt.savefig(f'static/{SYM}.png')
 
