# -*- coding: Latin-1 -*-
import unittest
import numpy
from math import floor

a = numpy.array([[0,1,2],[3,4,5],[6,7,8]])


b = a.mean(axis=0).reshape(1,len(a.mean(axis=0)))
#b = b.reshape(1,len(b))
print  a
print b