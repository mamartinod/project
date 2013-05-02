import pyfits
import numpy as np
import matplotlib.pyplot as plt

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
            
    def spectrumBoxVert(self): #vertical averaging
        self.spectrumName = "Vertical averaging spectrum"
        self.spectrumVert = self.box.mean(axis=0)
        return self.spectrumVert
        
    def spectrumBoxHorz(self): #horizontal averaging
        self.spectrumName = "Horizontal averaging spectrum"
        self.spectrumHorz = self.box.mean(axis=1)
        return self.spectrumHorz
        
    def plot(self, plotted):
        plt.plot(plotted, '+')
        plt.xlabel("pixels")
        plt.ylabel("intensity")
        plt.title(self.spectrumName)
        return plt.show()
        
    #def polyfit(self, pixel, fitted):
        
