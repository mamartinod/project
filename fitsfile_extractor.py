import pyfits
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.misc import factorial


class FitsFile(object):  # this will hold a fitsfile so its better to call it a fitsfile
    
    def __init__(self, fits_file=None):

        if fits_file: # The default None argument means we can open a FitsFile object without calling load.
            self.loadfile(fits_file)


    def loadfile(self, fits_file):
        """ I created this method to split the code up a bit and allow me to create a unit test for loading without
        having to make a actual fits file
        """

        with pyfits.open(fits_file) as dataFile:
            self.header = dataFile[0].header
            self.data = self.zeroReadSubstract(dataFile[1].data, dataFile[-5].data)
            
    def zeroReadSubstract(self, data, zeroRead):
        return data - zeroRead
        
    def cropBox(self, x1, y1, x2, y2): #Extract the spectrum
        x1 = int(x1)
        x2 = int(x2)
        y1 = int(y1)
        y2 = int(y2)

        if x1 < x2 and y1 < y2:
            self.box = np.copy(self.data[y1:y2,x1:x2])
            return self.box
        else:
            return "x1 >= x2 or y1 >= y2"
            
    def Spectrum(self): #vertical averaging
        self.spectrumName = "Spectrum (summed over the scan)"
        self.spectrum = self.box.mean(axis=0)
        return self.spectrum
        
    def spatialSpectrum(self): #horizontal averaging
        self.spectrumName = "Spectrum in spatial direction"
        self.spatialspectrum = self.box.mean(axis=1)
        return self.spatialspectrum
        
    def plot(self, plotted):
        plt.figure()
        plt.plot(plotted, 'r+')
        plt.xlabel("pixels")
        plt.ylabel("intensity")
        plt.title(self.spectrumName)
        return plt.show()

    
    def fitting(self, y):
        """order = int(order)
        x = np.arange(len(y))
        fit = np.polyfit(y,x,order)
        self.p = np.poly1d(fit)
        #xp = np.linspace(0, len(y), 10*len(y))"""
        
        x = np.arange(len(y))
        def func(x, a,b,c,d):
            return a + b*x + c*x**2 + d*x**3
            
        def gauss(x, a, mu, sigma): #gaussian
            return a*np.exp(-(x-mu)**2/(2*sigma**2))
            
        def cauchy(x, a, b, c): #Cauchy distribution
            return a/(1+((x-b)/c)**2)
            
        def poisson(x, a, b): #Poisson
            return np.exp(-a)*a**b/factorial(b)
            
        popt, pcov = curve_fit(func, x, y)
        self.popt = popt
        yf = func(x, popt[0], popt[1], popt[2], popt[3])
        
        gaussp, gausscov = curve_fit(gauss, x, y)
        self.gaussp = gaussp
        ygauss = gauss(x, gaussp[0], gaussp[1], gaussp[2])
        print gauss(x, gaussp[0], gaussp[1], gaussp[2])
        
        cauchyp, cauchycov = curve_fit(cauchy, x, y)
        self.cauchyp = cauchyp
        ycauchy = cauchy(x, cauchyp[0], cauchyp[1], cauchyp[2])
        self.cauchy = ycauchy
        
        poissonp, poissoncov = curve_fit(poisson, x, y)
        self.poissonp = poissonp
        ypoisson = poisson(x, poissonp[0], poissonp[1])
        self.poisson = ypoisson
        
        plt.figure()
        #plt.plot(x, y, '+', x, self.p(x))
        #plt.plot(x, y, 'b+', x, yf, 'g-', x, ygauss, 'r.', x, ycauchy, 'yo', x, ypoisson, 'v')
        plt.plot(x, y, x, ygauss)
        plt.xlabel('pixels')
        plt.ylabel('intensity')
        #plt.title("fit of {} by a polynom of order 2".format(self.spectrumName))
        return plt.show()
        
    