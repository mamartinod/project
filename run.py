""" module to run the code in the class
"""

import pylab as pl
from fitsfile_extractor import FitsFile



fits = FitsFile("ibxy01aoq_raw.fits")

pl.imshow(fits.data)
pl.show()