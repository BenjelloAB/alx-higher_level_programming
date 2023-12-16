#!/usr/bin/python3
import unittest
from models.square import Square
from models.base import Base
import json
from models.rectangle import Rectangle
import os
"""
This module will unittest the Base class
"""


class TestBase(unittest.TestCase):
    """
    Class of tests for Base class
    """

    def test_id(self):
        """
        check  id 
        """
        Base._Base__nb_objects = 0
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base(19)
        b5 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)
        self.assertEqual(b4.id, 19)
        self.assertEqual(b5.id, 4)

    def test_from_json_string(self):
        """
        check json string
        """
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        with self.subTest():
            r1 = Rectangle(19, 7, 2, 80, 1)
            r1_dict = r1.to_dictionary()
            json_dict = Base.to_json_string([r1_dict])
            self.assertEqual(r1_dict, {'x': 2, 'width': 19,
                                       'id': 1, 'height': 7,
                                       'y': 80})
            self.assertIs(type(r1_dict), dict)
            self.assertIs(type(json_dict), str)
            self.assertEqual(json.loads(json_dict), json.loads('[{"x": 2, '
                                                               '"width": 19, '
                                                               '"id": 1, '
                                                               '"height": 7, '
                                                               '"y": 80}]'))

    def test_rectangle(self):
        """
        check for rectangle create and to_dict
        """
        R1 = Rectangle(8, 51, 60)
        R1_dict = R1.to_dictionary()
        R2 = Rectangle.create(**R1_dict)
        self.assertNotEqual(R1, R2)

    def test_square(self):
        """
        Test for square create and to_dict
        """
        S1 = Square(44, 55, 66, 77)
        S1_dict = S1.to_dictionary()
        S2 = Rectangle.create(**S1_dict)
        self.assertNotEqual(S1, S2)

    def test_file_rectangle(self):
        """
        Test check if file loads from rectangle
        """
        R1 = Rectangle(3, 4, 5, 6)
        R2 = Rectangle(2, 2132)
        lst_R = [R1, R2]
        Rectangle.save_to_file(lst_R)
        lst_R2 = Rectangle.load_from_file()
        self.assertNotEqual(lst_R, lst_R2)

    def test_file_square(self):
        """
        Test check if file loads from square
        """
        S1 = Square(22)
        S2 = Square(44, 44, 55, 66)
        lst_S = [S1, S2]
        Square.save_to_file(lst_S)
        lst_S2 = Square.load_from_file()
        self.assertNotEqual(lst_S, lst_S2)
