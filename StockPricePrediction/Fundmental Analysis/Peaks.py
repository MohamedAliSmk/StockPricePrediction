import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt

data = pd.read_csv('data/LeveledLogStockData.csv', index_col=0, parse_dates=True)

features = ['Nasdaq', 'S&P', 'Russell', 'DJIA', 'Gold', '1yr T', '10yr Bond']
data.columns = ['Nasdaq', 'S&P', 'Russell', 'DJIA', 'Gold', '1yr T', '10yr Bond']


# try nasdaq
from scipy import signal

# find peaks
peak_ix = signal.find_peaks_cwt(data['Nasdaq'], np.arange(1, 253))
peaks = np.zeros(len(data))
for i in peak_ix:
    peaks[i] = 1
data['Nasdaq_peaks'] = peaks


# find floors
data['Flipped Nasdaq'] = data['Nasdaq'] * -1.0
floor_ix = signal.find_peaks_cwt(data['Flipped Nasdaq'], np.arange(1, 253))
floors = np.zeros(len(data))
for i in floor_ix:
    floors[i] = 1
data['Nasdaq_floors'] = floors


# plt data
plt.figure(figsize=(18,16))
plt.plot(data['Nasdaq'] + 1.0, label='Nasdaq')
plt.plot(data['Nasdaq_peaks'] * 3., label='Peaks', alpha=0.5)
plt.plot(data['Nasdaq_floors'] * 3., label='Floors', alpha=0.5)
plt.grid('on')
plt.legend(loc='best')
plt.title("Top Peaks, Floors in Nasdaq 1990-2016")
plt.savefig("FindStockIndexInflections.png")
plt.show()



