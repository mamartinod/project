""" module to run the code in the class
"""

import pylab as pl
from fitsfile_extractor import FitsFile


fits = FitsFile("ibxy01aoq_raw.fits")
pl.imshow(fits.data)
pl.show
fits.cropBox(62,153,193,242)
fits.spectrumBox()
fits.plot(fits.spectrum)
