""" module to run the code in the class
"""

import pylab as pl
from fitsfile_extractor import FitsFile


fits = FitsFile("ibxy01aoq_raw.fits")
pl.imshow(fits.data)
pl.show
fits.cropBoxMean(62,153,193,242)
fits.plot(fits.mean)
