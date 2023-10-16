#!/usr/bin/python3
"""
Unit tests for the city module.

Usage:
    Run all tests: python3 -m unittest discover tests
    Run specific file: python3 -m unittest tests.test_models.test_city
"""

from models import city
import inspect
import unittest


class TestCityDocumentation(unittest.TestCase):
    """
    TestCityDocumentation: (class) - unittest subclass to
    test docstrings in city module

    """

    @classmethod
    def setUpClass(cls):
        """
        setUpClass: (class method) - called before any tests are executed

        Sets up a list of all the functions in City class.
        """
        cls.city_functions = inspect.getmembers(city.BaseModel,
                                                inspect.isfunction)

    def test_module_docstring_exists(self):
        """
        Check if the module has a docstring.
        """
        self.assertTrue(len(city.__doc__) >= 1)

    def test_class_docstring_exists(self):
        """
        Check if the City class has a docstring.
        """
        self.assertTrue(len(city.BaseModel.__doc__) >= 1)

    def test_function_docstrings_exist(self):
        """
        Check if all functions in City class have docstrings.
        """
        for func_name, func in self.city_functions:
            with self.subTest(func_name=func_name):
                self.assertTrue(len(func.__doc__) >= 1)


if __name__ == "__main__":
    unittest.main()
