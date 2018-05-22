# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 13:14:28 2018

@author: lil
"""

import numpy as np

S0 = 100.
K = 105.
T = 1.0
r = 0.05
sigma = 0.2

I = 100000
z = np.random.standard_normal(I)
ST = S0 * np.exp((r - 0.5 * sigma ** 2) * T + sigma * np.sqrt(T) * z)
hT = np.maximum(ST - K, 0)
C0 = np.exp(-r * T) * sum(hT) / I

import numpy as np
import pandas as pd
import pandas_datareader as pdr

goog=pdr.data.DataReader('GOOG',data_source='google',start='3/14/2009',end='4/14/2014')
goog['Log_Ret'] = np.log(goog['Close'] / goog['Close'].shift(1))
goog['Volatility'] = pd.rolling_std(goog['Log_Ret'],window=252) * np.sqrt(252)
goog[['Close', 'Volatility']].plot(subplots=True, color='blue',figsize=(8, 6))


h5=pd.HDFStore('/home/fdrennan/Documents/Data/vstoxx_data_31032014.h5')
futures_data=h5['futures_data']
options_data=h5['options_data']

#####################################################################################
#Monte Carlo Pure Python
#####################################################################################
import time
import math
import random

random.seed(20000)
t0=time.time()
#parameters
S0=100
K=105
T=1.0
r=0.05
sigma=0.2
M=50
dt=T/M
I=250000

#simulating I paths with M steps
S=[]
for i in range(I):
    path=[]
    for t in range(M+1):
        if t==0:
            path.append(S0)
        else:
            z=random.gauss(0.0,1.0)
            St=path[t-1]*math.exp((r-0.5*sigma**2)*dt+sigma*math.sqrt(dt)*z)
            path.append(St)
    S.append(path)
#Calculate the Monte Carlo estimator
C0=math.exp(-r*T)*sum([max(path[-1]-K,0) for path in S])/I
#Outputs
timerun=time.time()-t0
print('EU Call option value %s'%C0)
print('Time run %s'%timerun)

#################################################################################
##Vectorization the Monte Carlo
################################################################################
import math
import numpy as np
import time

np.random.seed(20000)
t0=time.time()

#parameters
S0=100
K=105
T=1.0
r=0.05
sigma=0.2
M=50
dt=T/M
I=250000
#Simulating
S=np.zeros((M+1,I))
S[0]=S0
for t in range(1,M+1):
    z=np.random.standard_normal(I)
    S[t]=S[t-1]*np.exp((r-0.5*sigma**2)*dt+sigma*math.sqrt(dt)*z)
    
#Calculate the Monte Carlo estimator
C0=math.exp(-r*T)*np.sum(np.maximum(S[-1]-K,0))/I
#Outputs
timerun=time.time()-t0
print('EU Call option value %s'%C0)
print('Time run %s'%timerun)

##############################################################################
#Monte Carlo valuation of European call options with NumPy (log version)
###############################################################################
t0 = time.time()
S = S0 * np.exp(np.cumsum((r - 0.5 * sigma ** 2) * dt+ sigma * math.sqrt(dt)*np. random.standard_normal((M + 1, I)), axis=0))
S[0] = S0
#Calculate the Monte Carlo estimator
C0=math.exp(-r*T)*np.sum(np.maximum(S[-1]-K,0))/I
tnp2 = time.time() - t0
print('EU Call option value %s'%C0)
print('Time run %s'%tnp2)

###############################################################################
#Plot
###############################################################################
import matplotlib.pyplot as plt
plt.plot(S[:,:100])
plt.grid(True)
plt.xlabel('time step')
plt.ylabel('index level')

plt.hist(S[-1],bins=50)
