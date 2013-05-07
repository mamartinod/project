""" module to run the code in the class
"""

import pylab as pl
from fitsfile_extractor import *
import numpy as np


fits = FitsFile("ibxy01aoq_raw.fits")


#pl.imshow(fits.data)
#pl.show()

fits.Spectrum(fits.data)
fits.spatialSpectrum(fits.data)
fits.autoExtract(fits.spectrum)
fits.plot(fits.extraction)
fits.autoExtract(fits.spatialspectrum)
fits.plot(fits.extraction)

"""fits.spectrum = fits.data.mean(axis=0)/fits3.data.mean(axis=0).sum()
fits.derivation(fits.spectrum)
fits.medianFilter(fits.derivative)
fits.autoExtract(fits.spectrum)
#fits.plot(fits.spectrum)
#fits.plot(fits.derivative)
#fits.plot(fits.extraction)
#fits.plot(fits.medfilt)"""