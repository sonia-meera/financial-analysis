import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.signal import find_peaks 
from data import getEodData

def plotTimeSeries():
    eod_data = getEodData()
    xAxis, yAxis = getPlotData()

    plt.plot(xAxis, yAxis)
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

plotTimeSeries()
