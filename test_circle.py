"""Unit tests of the Circle class using unittest or pytest (your choice).

Write unit tests as described in README.md.

1. Unit test for add_area using typical values.
2. Unit test for add_area for an "edge case" where one circle has radius 0.
3. Unit test that circle constructor raises exception of radius is negative.

"""
from circle import Circle
import unittest

class CircleTest(unittest.TestCase):

    def test_negative_radius_construction(self):
        """Illegal case : Trying to construct a circle with negative number radius"""
        with self.assertRaises(ValueError):
            c1 = Circle(-2)
        with self.assertRaises(ValueError):
            c2 = Circle(-2.12)

    def test_add_area_normal_case(self):
        """Legal case : Trying to add area of two circles to get a bigger circle"""
        c1 = Circle(3)
        self.assertEqual(3,c1.get_radius())
        c2 = Circle(4)
        self.assertEqual(4,c2.get_radius())
        c3 = c1.add_area(c2)
        self.assertEqual(5,c3.get_radius())
        c4 = c2.add_area(c1)
        self.assertEqual(5,c4.get_radius())

    def test_add_area_with_radius_zero(self):
        """Edge case : Trying to add area of two circles which one of them is zero radius"""
        c1 = Circle(3)
        self.assertEqual(3,c1.get_radius())
        c2 = Circle(0)
        self.assertEqual(0,c2.get_radius())
        c3 = c1.add_area(c2)
        self.assertEqual(3,c3.get_radius())
        c4 = c2.add_area(c1)
        self.assertEqual(3,c4.get_radius())

if __name__ == '__main__':
    unittest.main(verbosity = 2)
    