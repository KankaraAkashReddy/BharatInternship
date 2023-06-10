import pandas_datareader as pdr
import pandas as pd

#Loading Google Stock Price data till date using tiingo
df = pdr.get_data_tiingo('GOOG',api_key='303ab54719a6a63dd1e57c36916695053da99b86')
df.to_csv('GOOG.csv')

df = pd.read_csv('GOOG.csv')
print(df.head())
print(df.tail())

df1 = df.reset_index()['close']
print(df1.shape)

import matplotlib.pyplot as plt

plt.plot(df1)

import numpy as np
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler(feature_range=(0,1))
df1 = scaler.fit_transform(np.array(df1).reshape(-1,1))

df1.shape
