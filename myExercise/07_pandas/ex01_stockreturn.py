# Use Pandas DataReader to removely access data

import pandas as pd
import matplotlib.pyplot as plt
import pandas.io.data as web

# define the ticker list
ticker_list = {'INTC': 'Intel',
               'MSFT': 'Microsoft',
               'IBM': 'IBM',
               'BHP': 'BHP',
               'RSH': 'RadioShack',
               'TM': 'Toyota',
               'AAPL': 'Apple',
               'AMZN': 'Amazon',
               'BA': 'Boeing',
               'QCOM': 'Qualcomm',
               'KO': 'Coca-Cola',
               'GOOG': 'Google',
               'SNE': 'Sony',
               'PTR': 'PetroChina'}

# Get data
data = web.DataReader(list(ticker_list.keys()), 'yahoo', '2014/1/1')
data = data['Adj Close']

data = data.ix[[0,-1],:]
data = data.transpose()
data.columns = ['S0','S1']

data['YTD_return'] = data.S1 / data.S0 - 1

data = data.sort_index(by='YTD_return')

data['YTD_return'].plot(kind='bar')

plt.show()