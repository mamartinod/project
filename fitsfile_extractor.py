import pyfits

class FitsExtractor:
    
    def __init__(self, fits_file):
        with pyfits.open(fits_file) as dataFile:
            self.header = dataFile[0].header
            self.data = dataFile[1].data