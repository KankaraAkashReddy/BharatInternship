import pandas_datareader as pdr

df = pdr.get_data_tiingo('GOOG',api_key='303ab54719a6a63dd1e57c36916695053da99b86')
df.to_csv('GOOG.csv')
import pandas as pd

df = pd.read_csv('GOOG.csv')
print(df.head())
print(df.tail())
