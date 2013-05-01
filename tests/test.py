# -*- coding: Latin-1 -*-
import unittest
import numpy
from math import floor

x1 = 0
x2 = 2
y1 = 0
y2 = 2
a = numpy.array([[0,1,2],[3,4,5],[6,7,8]])

d = numpy.copy(a[x1:x2,y1:y2])
print a

print d
