import numpy as np
import pandas as pd

class MiceT:

    #Class Object Attributes
    #Class Attributes
    #-----empty

    #Class instantiation method
    #Instance Attributes - different for each object
    def __init__(self, name):
        self.name = name

    #Class Methods
    def Make_Rnd_Time (self, mode: float, scale: float, start: datetime64, end: datetime64):
        """
        Creates a Mice time series
        Return: panda dataframe with datetime as index
        """
        mode = mode


#Generating TS data
mode = 1
scale = 0.1
sDays = np.arange('2015-01', '2015-03', dtype='datetime64[D]')
nDays = len(sDays)

s1 = np.random.gumbel(loc=mode,scale=scale,size=nDays)
s1[s1 < 0] = 0

import matplotlib.pyplot as plt
import seaborn as sns

sns.lineplot(data=s1)

from statsmodels.tsa.stattools import adfuller

result = adfuller(s1)

print('ADF Statistic: %f' % result[0])
print('p-value: %f' % result[1])
print('Critical Values:')
for key, value in result[4].items():
	print('\t%s: %.3f' % (key, value))

"""
p-value > 0.05: Fail to reject the null hypothesis (H0), the data has a unit root and is non-stationary.
p-value <= 0.05: Reject the null hypothesis (H0), the data does not have a unit root and is stationary.
"""



from pandas import Series
from matplotlib import pyplot
series = pd.read_csv('/home/clemente/hub/Gen_Tech/Datasets/AirPassengers.csv')
series.plot()
pyplot.show()

series = series['#Passengers']

result = adfuller(series)

print('ADF Statistic: %f' % result[0])
print('p-value: %f' % result[1])
print('Critical Values:')
for key, value in result[4].items():
	print('\t%s: %.3f' % (key, value))
