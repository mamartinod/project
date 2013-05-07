# -*- coding: Latin-1 -*-
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.misc import factorial
from scipy.signal import medfilt

x = np.array([0,0,0,7,2,1,2,3,7,7,7,7,7,7,7,7,4,2,0])
y = np.arange(len(x))


def derivation(array):#Get the derivative of a 1D-array.
    i = 0
    derivative = []
    while i < len(array)-1:
        derivative.append(array[i+1]-array[i])
        i = i+1
        if i >=300:
            break
    
    derivative.append(0)
    derivative = np.array(derivative)
    return derivative
    
def medianFilter(array):#remove sal-and-pepper noise
    medianfilt = medfilt(array).copy()
    return medianfilt
        
        
def autoExtract(array):#Extract signal from a 1D-array
    """This method derives the signal. The idea is the extrema values of 
    the derivative flank the signal which has to be extracted. It is very 
    sensitive to cosmic ray so it deals with a derivative signal which have
    passed through a median filter which remove artefacts from cosmic rays."""
    
    derivmax = medianFilter(derivation(array)).argmax()
    derivmin = medianFilter(derivation(array)).argmin()
    i = 0
    extraction = []
    while i < len(array) or i <= 300:
        if i >= derivmax and i <= derivmin:
            extraction.append(array[i])
        i = i+1
    extraction = np.array(extraction)
    derivmax = derivmax
    derivmin = derivmin
    return extraction
    
print x, len(x)
print derivation(x), len(derivation(x))
print medianFilter(derivation(x)), len(medianFilter(derivation(x)))
print autoExtract(x), len(autoExtract(x))

plt.figure()
plt.plot(y,x)
plt.plot(y,derivation(x))
#plt.plot(y, autoExtract(x))
plt.show()