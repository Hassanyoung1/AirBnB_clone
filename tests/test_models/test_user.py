#!/usr/bin/python3
"""
Unit tests for the user module.

Usage:
    Run all tests: python3 -m unittest discover tests
    Run specific file: python3 -m unittest tests.test_models.test_user
"""

from models import user
import inspect
import unittest


class TestUserDocumentation(unittest.TestCase):
    """
    TestUserDocumentation: (class) - unittest subclass to
    test docstrings in user module

    """

    @classmethod
    def setUpClass(cls):
        """
        setUpClass: (class method) - called before any tests are executed

        Sets up a list of all the functions in User class.
        """
        cls.user_functions = inspect.getmembers(user.BaseModel,
                                                inspect.isfunction)

    def test_module_docstring_exists(self):
        """
        Check if the module has a docstring.
        """
        self.assertTrue(len(user.__doc__) >= 1)

    def test_class_docstring_exists(self):
        """
        Check if the User class has a docstring.
        """
        self.assertTrue(len(user.BaseModel.__doc__) >= 1)

    def test_function_docstrings_exist(self):
        """
        Check if all functions in User class have docstrings.
        """
        for func_name, func in self.user_functions:
            with self.subTest(func_name=func_name):
                self.assertTrue(len(func.__doc__) >= 1)


if __name__ == "__main__":
    unittest.main()
