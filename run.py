""" module to run the code in the class
"""

import pylab as pl
from fitsfile_extractor import FitsFile


pl.imshow(fits.data)
pl.show

fits = FitsFile("ibxy01aoq_raw.fits")
fits.cropBox(62,153,193,242)