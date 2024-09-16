from unittest import TestCase
from statistics import variance, stdev, average
from math import sqrt

class StatisticsTest(TestCase):

    def test_variance_typical_values(self):
        """variance of typical values"""
        self.assertEqual(0.0, variance([10.0,10.0,10.0,10.0,10.0]))
        self.assertEqual(2.0, variance([1,2,3,4,5]))
        self.assertEqual(8.0, variance([10,2,8,4,6]))

    def test_variance_non_integers(self):
        """variance should work with decimal values"""
        # variance([x,y,z]) == variance([x+d,y+d,z+d]) for any d
        self.assertAlmostEqual(4.0, variance([0.1, 4.1]))
        # variance([0,4,4,8]) == 8
        self.assertAlmostEqual(8.0, variance([0.1, 4.1, 4.1, 8.1]))

    def test_stdev(self):
        # standard deviation of a single value should be zero
        self.assertEqual(0.0, stdev([10.0]))
        # simple test
        self.assertEqual(2.0, stdev([1, 5]))
        # variance([0, 0.5, 1, 1.5, 2.0]) is 0.5
        self.assertEqual(sqrt(0.5), stdev([0, 0.5, 1, 1.5, 2]))

    def test_average(self):
        """average function should work with any numeric values"""
        # integer value, float results
        self.assertEqual(1.5, average([1, 2]))
        # integer value, integer results
        self.assertEqual(2, average([1, 3]))
        # float value
        self.assertEqual(2.5, average([1.5, 3.5]))
        # mixed value
        self.assertEqual(2.25, average([2.5, 2]))

    def test_nodata(self):
        """ test stdev, average, varience with empty list"""
        # average
        self.assertRaises(ValueError, average, [])
        # variance
        self.assertRaises(ValueError, variance, [])


if __name__ == '__main__':
    import unittest
    unittest.main(verbosity=1)
