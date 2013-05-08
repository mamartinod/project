""" module to run the code in the class
"""

import pylab as pl
from fitsfile_extractor import *
import numpy as np


fits = FitsFile("ibxy01aoq_raw.fits")


#pl.imshow(fits.data)
#pl.show()

"""
OK so im not certain you've fully grasped the power of classes. When you call a class you create an object or instance
of that class. That class can store variables and perform methods on itself. For that reason if you are using internal
data in the class you dont need to give the method that information.

Now since you make a spectrum and then 'optimise' it it makes sense to do this in the spectrum class
"""

spectralspectrum = fits.spectrum()  # the class already has the data so why give it again?
spatialspectrum = fits.spatialSpectrum()

spectralspectrum.autoExtract()
spatialspectrum.autoExtract()



# fits.spectrum.plot(fits.spectrum.data)

# fits.spatialspectrum.plot(fits.spatialspectrum.data) # this is odd, your asking a class to plot something other than itself
# fits.spatialspectrum.plot() # With no need for any information in the class. Use a normal function outside the
 # class for this perhaps and then make the spectrum plot method call that instead of writing the same code twice

spatialspectrum.plotData()
spatialspectrum.plotExtraction()

spectralspectrum.plotData()
spectralspectrum.plotExtraction()

pl.show()