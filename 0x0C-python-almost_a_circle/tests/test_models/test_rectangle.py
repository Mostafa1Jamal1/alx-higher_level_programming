#!/usr/bin/python3
'''Module of test suit for the class Rectangle'''


import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangleClass(unittest.TestCase):
    '''Test class for the Rectangle class'''
# The setUp and tearDown of all tests
    def setUp(self):
        '''Befor each test'''
        Base._Base__nb_objects = 0

    def tearDown(self):
        '''After each test'''
        Base._Base__nb_objects = 0
# **************************************************************************
# Check inheritance from Base
    def test_inheritationfromBase(self):
        '''Test if the Rectangle is inherited from Base'''
        self.assertTrue(issubclass(Rectangle, Base))
# **************************************************************************
# Check the existing of all the attributes
    def test_attributs(self):
        '''test that attributes exists'''
        r1 = Rectangle(10, 2)
        self.assertTrue(hasattr(r1, 'width'))
        self.assertTrue(hasattr(r1, 'height'))
        self.assertTrue(hasattr(r1, 'x'))
        self.assertTrue(hasattr(r1, 'y'))
        self.assertTrue(hasattr(r1, 'id'))
# **************************************************************************
# Check Validation of all setters about type
    def test_validation_Width_type(self):
        '''Test the validation of width of type'''
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1 = Rectangle("str", 2)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1 = Rectangle(True, 2)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1 = Rectangle(None, 2)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1 = Rectangle([10], 2)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1 = Rectangle((10, ), 2)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1 = Rectangle({'str': 10}, 2)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1 = Rectangle(10.52, 2)

    def test_validation_height_type(self):
        '''Test the validation of height of type'''
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r1 = Rectangle(10, "str")
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r1 = Rectangle(10, True)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r1 = Rectangle(10, None)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r1 = Rectangle(10, [10])
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r1 = Rectangle(10, (10, ))
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r1 = Rectangle(10, {'str': 10})
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r1 = Rectangle(10, 2.52)

    def test_validation_x_type(self):
        '''Test the validation of x of type'''
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r1 = Rectangle(10, 2, "str")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r1 = Rectangle(10, 2, True)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r1 = Rectangle(10, 2, None)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r1 = Rectangle(10, 2, [10])
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r1 = Rectangle(10, 2, (10, ))
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r1 = Rectangle(10, 2, {'str': 10})
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r1 = Rectangle(10, 2, 10.25)

    def test_validation_y_type(self):
        '''Test the validation of y of type'''
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r1 = Rectangle(10, 2, 3, "str")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r1 = Rectangle(10, 2, 3, True)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r1 = Rectangle(10, 2, 3, None)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r1 = Rectangle(10, 2, 3, [10])
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r1 = Rectangle(10, 2, 3, (10, ))
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r1 = Rectangle(10, 2, 3, {'str': 10})
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r1 = Rectangle(10, 2, 3, 10.25)
# **************************************************************************
# Check Validation of all setters about value
    def test_validation_width_value(self):
        '''Test the validation of width of value'''
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r1 = Rectangle(0, 2)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r1 = Rectangle(-10, 2)

    def test_validation_height_value(self):
        '''Test the validation of height of value'''
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r1 = Rectangle(10, 0)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r1 = Rectangle(10, -2)

    def test_validation_x_value(self):
        '''Test the validation of x of value'''
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r1 = Rectangle(10, 2, -2)

    def test_validation_y_value(self):
        '''Test the validation of y of value'''
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r1 = Rectangle(10, 2, 3, -2)
# **************************************************************************
# Check with different number of arguments
    def test_TwoTipicalArgs(self):
        '''Testing the case of two typical arguments'''
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r2.width, 2)
        self.assertEqual(r2.height, 10)
        self.assertEqual(r2.x, 0)
        self.assertEqual(r2.y, 0)

    def test_ThreeArgs(self):
        '''Testing the case of three typical arguments'''
        r1 = Rectangle(10, 2, 3)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 0)

    def test_FourArgs(self):
        '''Testing the case of four typical arguments'''
        r1 = Rectangle(10, 2, 3, 4)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 4)

    def test_FiveArgs(self):
        '''Testing the case of five typical arguments'''
        r1 = Rectangle(10, 2, 3, 4, 15)
        self.assertEqual(r1.id, 15)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 4)

    def test_MoreThanFiveArgs(self):
        '''Testing the case of three typical arguments'''
        with self.assertRaises(TypeError):
            r1 = Rectangle(10, 2, 3, 4, 15, 20)
# ***************************************************************************
