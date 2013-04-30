import pyfits


class FitsFile(object):  # this will hold a fitsfile so its better to call it a fitsfile
    
    def __init__(self, fits_file):
        with pyfits.open(fits_file) as dataFile:
            self.loadfile(dataFile)

    def loadfile(self, dataFile):
        """ I created this method to split the code up a bit and allow me to create a unit test for loading without
        having to make a actual fits file
        """

        self.header = dataFile[0].header
        self.data = self.zeroReadSubstract(dataFile[1].data, dataFile[-5].data)
            
    def zeroReadSubstract(self, data, zeroRead):
        return data - zeroRead