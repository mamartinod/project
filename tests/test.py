# -*- coding: Latin-1 -*-
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.misc import factorial

x = np.array([1,2,7,7,7,2,1])
y = []
z = []

y = x.sum()
print y
"""i=0
while i < len(x)-1:
    z.append(x[i+1]-x[i])
    i = i+1
z = np.array(z)
print z
i = 0
while i < len(x):
    if i >= z.argmax() and i <= z.argmin()+1:
        y.append(x[i])
    i = i+1
    
print y"""