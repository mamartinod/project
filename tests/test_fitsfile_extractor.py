""" This runs unit tests. You should get used to writing test as you code. In fact they can be very helpful and avoid
you constantly reloading and running your script. split your code into small testable chunks and write a test that
will validate as true once your code is written. Then write the code until its true!
"""

import unittest  # normal python package imports first

import numpy as np  # then common but non standard third party packages

from fitsfile_extractor import FitsFile  # then ones within your module seperated by a line


class Test_FitsFile(unittest.TestCase):

    def test_zeroReadSubstract(self):

        # TODO create two arrays, open a FitsFile object, and pass them through it
        # Hint: read up on unittests and let the FitsFile class work if no fits file is given to it at first

        fakeFits = FitsFile()

        data = np.array([[6, 2], [3, 9]])
        zeroread = np.array([[2, 1], [0.5, 3]])

        answer = fakeFits.zeroReadSubstract(data, zeroread)
        expected = np.array([[4, 1], [2.5, 6]])

        self.assertTrue(np.all(answer == expected))  # you need to use np.all to compare arrays as otherwise they
        # compare each value so you get a return of [True, True],[True, True]

    def test_cropBox(self):
        fakeFits = FitsFile()
        fakeFits.data = np.array([[0,1,2],[3,4,5],[6,7,8]])

        answer = fakeFits.cropBox(0, 0, 2, 2)

        print answer # temp so you can see what its returning

        expected = np.array([[0,1],[3,4]])
        self.assertTrue(np.all(answer == expected))
        
    def test_cropBoxmean(self):
        fakeFits = FitsFile()
        fakeFits.data = np.array([[0,1,2],[3,4,5],[6,7,8]])
        
        answer = fakeFits.cropBoxMean(0,0,3,3)
        print answer
        
        expected = np.array([[3., 4., 5.]])
        self.assertTrue(np.all(answer == expected))


if __name__ == '__main__':
    unittest.main()