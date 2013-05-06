""" module to run the code in the class
"""

import pylab as pl
from fitsfile_extractor import FitsFile
import numpy as np

fits = FitsFile("ibxy01aoq_raw.fits")

#pl.imshow(fits.data)
#pl.show()
#fits.cropBox(62,153,193,242)
#fits.spatialSpectrum()
#fits.plot(fits.spatialspectrum)

#fits.Spectrum()
#fits.plot(fits.spectrum)

#fits.fitting(fits.spectrum)

fits.spectrum = fits.data.mean(axis=0)/fits.data.mean(axis=0).sum()
fits.plot(fits.spectrum)
fits.plot(fits.derivation(fits.spectrum))