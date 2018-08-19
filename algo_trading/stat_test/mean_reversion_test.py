
import numpy as np
import pandas as pd
import matplotlib as plt
#from matplotlib import pyplot
import quandl
#import statsmodels as ts
import statsmodels.tsa.stattools as ts


# Augmented Dickey-Fuller Test
# Δy(t) = λy(t − 1) + μ + βt + α1Δy(t − 1) + … + αkΔy(t − k) + ∋t
def ADF_Test(data_path):
    #import data
    #df = pd.read_csv(r'C:\Users\baek6\PycharmProjects\Test\venv\Lib\international-airline-passengers.csv')
    df = pd.read_csv(data_path)

    df.drop(df.tail(1).index,inplace=True)
    #df.plot()
    #plt.pyplot.show()

    # built-in function of adf with lag value of 1
    result = ts.adfuller(df[df.columns[1]],1)
    print(result)
    # (test stats(adf), pval, # lag used, # obs, crit val, icbest, resstore)

#Run Function
ADF_Test(r'C:\Users\baek6\PycharmProjects\Test\venv\Lib\international-airline-passengers.csv')


# def Hurst_Test():










