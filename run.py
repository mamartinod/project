""" module to run the code in the class
"""

import pylab as pl
from fitsfile_extractor import *
import numpy as np


fits = FitsFile("ibxy01aoq_raw.fits")


#pl.imshow(fits.data)
#pl.show()

fits.spectrum(fits.data)
fits.spatialSpectrum(fits.data)
spectralspectrum = fits.autoExtract(fits.spectrum.data)
spatialspectrum = fits.autoExtract(fits.spatialspectrum.data)
fits.spectrum.plot(fits.spectrum.data)
fits.spectrum.plot(spectralspectrum)
fits.spatialspectrum.plot(fits.spatialspectrum.data)
fits.spatialspectrum.plot(spatialspectrum)