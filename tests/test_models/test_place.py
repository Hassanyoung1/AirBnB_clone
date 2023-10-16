#!/usr/bin/python3
"""
Unit tests for the place module.

Usage:
    Run all tests: python3 -m unittest discover tests
    Run specific file: python3 -m unittest tests.test_models.test_place
"""

from models import place
import inspect
import unittest


class TestPlaceDocumentation(unittest.TestCase):
    """
    TestPlaceDocumentation: (class) - unittest subclass to
    test docstrings in place module

    """

    @classmethod
    def setUpClass(cls):
        """
        setUpClass: (class method) - called before any tests are executed

        Sets up a list of all the functions in
        Place class.
        """
        cls.place_functions = inspect.getmembers(place.BaseModel,
                                                 inspect.isfunction)

    def test_module_docstring_exists(self):
        """
        Check if the module has a docstring.
        """
        self.assertTrue(len(place.__doc__) >= 1)

    def test_class_docstring_exists(self):
        """
        Check if the Place class has a docstring.
        """
        self.assertTrue(len(place.BaseModel.__doc__) >= 1)

    def test_function_docstrings_exist(self):
        """
        Check if all functions in Place class have docstrings.
        """
        for func_name, func in self.place_functions:
            with self.subTest(func_name=func_name):
                self.assertTrue(len(func.__doc__) >= 1)


if __name__ == "__main__":
    unittest.main()
