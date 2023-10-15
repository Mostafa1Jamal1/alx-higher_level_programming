#!/usr/bin/python3
'''Module of test suit for the class Rectangle'''


import unittest
from models.rectangle import Rectangle
from models.base import Base

class TestRectangleClass(unittest.TestCase):
    '''Test class for the Rectangle class'''
    def setUp(self):
        '''Befor each test'''
        Base._Base__nb_objects = 0

    def tearDown(self):
        '''After each test'''
        Base._Base__nb_objects = 0

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

    def testThreeArgs(self):
        '''Testing the case of three typical arguments'''
        r1 = Rectangle(10, 2, 3)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 0)
