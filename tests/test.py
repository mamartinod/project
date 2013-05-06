# -*- coding: Latin-1 -*-
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.misc import factorial
from scipy.signal import medfilt

x = np.array([0,0,0,7,2,1,2,3,7,7,7,7,7,7,7,7,4,2,0])
y = x[:]

if x.all() == y.all(): 
    print True
else:
    print False


