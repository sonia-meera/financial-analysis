import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.signal import find_peaks 
from data import getEodData

def plotTimeSeries():
    eod_data = getEodData()
    xAxis, yAxis = getPlotData()
    sma50 = getMovingAverages(yAxis, 50)
    sma200 = getMovingAverages(yAxis, 200)

    print(sma50)

    plt.plot(xAxis, yAxis)
    plt.plot(xAxis, sma50)
    plt.plot(xAxis, sma200)
    plt.title("Chart Title")
    plt.xlabel("Date")
    plt.ylabel("Adjusted Close")

    plt.show()

def getPlotData():
    eod_data = getEodData()
    xAxis = []
    yAxis = []

    for i in range(len(eod_data)):
        xAxis.append(np.datetime64(eod_data[i]['date']))
        yAxis.append(eod_data[i]['adjusted_close'])
    
    return (xAxis, yAxis)

def getMovingAverages(adj_close, window):
    series = pd.Series(adj_close)
    sma = series.rolling(window=window).mean()
    return sma

plotTimeSeries()
