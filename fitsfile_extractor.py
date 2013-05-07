import pyfits
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import medfilt


class FitsFile(object):  # this will hold a fitsfile so its better to call it a fitsfile
    
    def __init__(self, fits_file=None):

        if fits_file: # The default None argument means we can open a FitsFile object without calling load.
            self.loadfile(fits_file);


    def loadfile(self, fits_file):
        """ I created this method to split the code up a bit and allow me to create a unit test for loading without
        having to make a actual fits file"""

        with pyfits.open(fits_file) as dataFile:
            self.header = dataFile[0].header
            self.data = self.zeroReadSubstract(dataFile[1].data, dataFile[-5].data)
            
    def zeroReadSubstract(self, data, zeroRead):
        return data - zeroRead
            
    def spectrum(self, data): #vertical averaging
        name = "Spectrum (summed over the scan)"
        self.spectrum = Spectrum(data.mean(axis=0), name)
        return self.spectrum
        
    def spatialSpectrum(self, data): #horizontal averaging
        name = "Signal in spatial direction"
        self.spatialspectrum = Spectrum(data.mean(axis=1), name)
        return self.spatialspectrum
        
    """def plot(self, plotted): #Plot data
        plt.figure()
        plt.plot(plotted, 'r+')
        plt.xlabel("pixels")
        plt.ylabel("intensity")
        if plotted.name:
            plt.title(self.spectrumName)
        return plt.show()"""

    
    def derivation(self, array):#Get the derivative of a 1D-array.
        i = 0
        derivative = []
        while i < len(array)-1:
            derivative.append(array[i+1]-array[i])
            i = i+1
            if i >=300:
                break
            
        self.derivative = np.array(derivative)
        return self.derivative
        
    def medianFilter(self, array):#remove salt-and-pepper noise
        self.medfilt = medfilt(array).copy()
        return self.medfilt
        
        
    def autoExtract(self, array):#Extract signal from a 1D-array
        """This method derives the signal. The idea is the extrema values of 
        the derivative flank the signal which has to be extracted. It is very 
        sensitive to artefacts so it should deal with a derivative signal which have
        passed through a median filter which remove artefacts from cosmic rays."""
        
        derivmax = self.medianFilter(self.derivation(array)).argmax()
        derivmin = self.medianFilter(self.derivation(array)).argmin()
        i = 0
        extraction = []
        while i < len(array):
            if i >= derivmax and i <= derivmin:
                extraction.append(array[i])
            else:
                extraction.append(0)
            i = i+1
        self.extraction = np.array(extraction)
        self.derivmax = derivmax
        self.derivmin = derivmin
        return self.extraction
        
        
class Spectrum(object): #hold the spectra and its extracted part. Called by FitsFile which will cut it
    def __init__(self, data, name="Plot", xaxis="Pixels", yaxis="Intensity"):
        self.name = name
        self.data = data
        if xaxis:
            self.xaxis = xaxis
        if yaxis:
            self.yaxis = yaxis
            
    def plot(self, plotted): #Plot data
        plt.figure()
        plt.plot(plotted, 'r+')
        plt.xlabel(self.xaxis)
        plt.ylabel(self.yaxis)
        plt.title(self.name)
        return plt.show()