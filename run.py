""" module to run the code in the class
"""

import pylab as pl
from fitsfile_extractor import FitsFile
import numpy as np

fits = FitsFile("ibh7a7lsq_raw.fits")
fits2 = FitsFile("ibh7a7m2q_raw.fits")
fits3 = FitsFile("ibxy01aoq_raw.fits")
fits4 = FitsFile("ibxy04s4q_raw.fits")
fits5 = FitsFile("ibxy07q9q_raw.fits")

#pl.imshow(fits.data)
#pl.show()
#fits.cropBox(62,153,193,242)
#fits.spatialSpectrum()
#fits.plot(fits.spatialspectrum)

#fits.Spectrum()
#fits.plot(fits.spectrum)

#fits.fitting(fits.spectrum)

fits.spectrum = fits.data.mean(axis=0)/fits3.data.mean(axis=0).sum()
fits.derivation(fits.spectrum)
fits.medianFilter(fits.derivative)
fits.autoExtract(fits.spectrum)
#fits.plot(fits.spectrum)
#fits.plot(fits.derivative)
#fits.plot(fits.extraction)
#fits.plot(fits.medfilt)

fits2.spectrum = fits2.data.mean(axis=0)/fits2.data.mean(axis=0).sum()
fits2.derivation(fits2.spectrum)
fits2.medianFilter(fits2.derivative)
fits2.autoExtract(fits2.spectrum)
#fits2.plot(fits2.spectrum)
#fits2.plot(fits2.derivative)
#fits2.plot(fits2.extraction)
#fits2.plot(fits2.medfilt)

fits3.spectrum = fits3.data.mean(axis=0)/fits3.data.mean(axis=0).sum()
fits3.derivation(fits3.spectrum)
fits3.medianFilter(fits3.derivative)
fits3.autoExtract(fits3.spectrum)
fits3.plot(fits3.spectrum)
#fits3.plot(fits3.derivative)
fits3.plot(fits3.extraction)
#fits3.plot(fits3.medfilt)

fits4.spectrum = fits4.data.mean(axis=0)/fits4.data.mean(axis=0).sum()
fits4.derivation(fits4.spectrum)
fits4.medianFilter(fits4.derivative)
fits4.autoExtract(fits4.spectrum)
#fits4.plot(fits4.spectrum)
#fits4.plot(fits4.derivative)
#fits4.plot(fits4.extraction)
#fits4.plot(fits4.medfilt)

fits5.spectrum = fits5.data.mean(axis=0)/fits5.data.mean(axis=0).sum()
fits5.derivation(fits5.spectrum)
fits5.medianFilter(fits5.derivative)
fits5.autoExtract(fits5.spectrum)
#fits5.plot(fits5.spectrum)
#fits5.plot(fits5.derivative)
#fits5.plot(fits5.extraction)
#fits5.plot(fits5.medfilt)

indicemax = fits.derivmax
indicemin = fits.derivmin
a = fits.spectrum[indicemax:indicemin+1]
a = np.array(a)

if a.all() == fits.extraction.all():
    print True
else:
    print False