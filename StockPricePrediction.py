import pandas_datareader as pdr
import pandas as pd

#Loading Google Stock Price data till date using tiingo
df = pdr.get_data_tiingo('GOOG',api_key='303ab54719a6a63dd1e57c36916695053da99b86')
df.to_csv('GOOG.csv')

df = pd.read_csv('GOOG.csv')
print(df.head())
print(df.tail())
