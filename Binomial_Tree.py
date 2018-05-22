# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 10:14:15 2018

@author: lil
"""
import numpy as np
import numba as nb

S0=100
T=1.
r=0.05
vola=0.20

M=1000
dt=T/M
df=np.exp(-r*dt)
#binomial parameters
u=np.exp(vola*np.sqrt(dt))
d=1/u
q=(np.exp(r*dt)-d)/(u-d)
#Pure Python
def binomial_py(strike):
    S=np.zeros((M+1, M+1), dtype=np.float64)
    S[0,0]=S0
    z1=0
    for j in range(1,M+1):
        z1=z1+1
        for i in range(z1+1):
            S[i,j]=S[0,0] * (u**j) * (d ** (i*2))
    
    iv=np.zeros((M+1, M+1), dtype=np.float64)
    z2=0
    for j in range(0,M+1):
        for i in range(z2+1):
            iv[i,j]=max(S[i,j]-strike, 0)
        z2=z2+1
    
    pv=np.zeros((M+1, M+1), dtype=np.float64)
    pv[:, M]=iv[:, M]
    z3=M+1
    for j in range(M-1,-1,-1):
        z3=z3-1
        for i in range(z3):
            pv[i,j]=(q * pv[i, j+1] + (1-q) * pv[i+1, j+1]) * df
    return pv[0,0]


#NumPy
def binomial_np(strike):
    mu=np.arange(M+1)
    mu=np.resize(mu, (M+1, M+1))
    md=np.transpose(mu)
    mu=u**(mu-md)
    md=d**md
    S=S0*mu*md
    
    pv=np.maximum(S-strike, 0)
    z=0
    for t in range(M-1, -1, -1):
        pv[0:M-z, t]=(q * pv[0:M-z, t+1] + (1-q) * pv[1:M-z+1, t+1]) * df
        z+=1
    return pv[0,0]

#Numba

binomial_nb=nb.jit(binomial_py)
binomial_nb(100)