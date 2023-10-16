#!/usr/bin/python3
"""
Unit tests for the amenity module.

Usage:
    Run all tests: python3 -m unittest discover tests
    Run specific file: python3 -m unittest tests.test_models.test_amenity
"""

from models import amenity
import inspect
import unittest


class TestAmenityDocumentation(unittest.TestCase):
    """
    TestAmenityDocumentation: (class) - unittest subclass to
    test docstrings in amenity module

    """

    @classmethod
    def setUpClass(cls):
        """
        setUpClass: (class method) - called before any tests are executed

        Sets up a list of all the functions in
        Amenity class.
        """
        cls.amenity_functions = inspect.getmembers(amenity.BaseModel,
                                                   inspect.isfunction)

    def test_module_docstring_exists(self):
        """
        Check if the module has a docstring.
        """
        self.assertTrue(len(amenity.__doc__) >= 1)

    def test_class_docstring_exists(self):
        """
        Check if the Amenity class has a docstring.
        """
        self.assertTrue(len(amenity.BaseModel.__doc__) >= 1)

    def test_function_docstrings_exist(self):
        """
        Check if all functions in Amenity class have docstrings.
        """
        for func_name, func in self.amenity_functions:
            with self.subTest(func_name=func_name):
                self.assertTrue(len(func.__doc__) >= 1)


if __name__ == "__main__":
    unittest.main()
