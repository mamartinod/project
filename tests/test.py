# -*- coding: Latin-1 -*-
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.misc import factorial

x = np.arange(10000)

def gauss(x, a, mu, sigma): #gaussian
    return a*np.exp(-(x-mu)**2/(2*sigma**2))
    
print gauss(x[150], 3806., 130., 46.)