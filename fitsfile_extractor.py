import pyfits

class FitsExtractor:
    
    def __init__(self, fits_file):
        with pyfits.open(fits_file) as dataFile:
            self.header = dataFile[0].header
            self.data = dataFile[1].data
            self.zero = dataFile[-5].data
            
    def zeroReadSubstract(self):
        self.data = self.data - self.zero