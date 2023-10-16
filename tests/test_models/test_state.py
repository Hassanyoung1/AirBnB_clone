#!/usr/bin/python3
"""
Unit tests for the state module.

Usage:
    Run all tests: python3 -m unittest discover tests
    Run specific file: python3 -m unittest tests.test_models.test_state
"""

from models import state
import inspect
import unittest


class TestStateDocumentation(unittest.TestCase):
    """
    TestStateDocumentation: (class) - unittest subclass to test
    docstrings in state module

    """

    @classmethod
    def setUpClass(cls):
        """
        setUpClass: (class method) - called before any tests are executed

        Sets up a list of all the functions in State class.
        """
        cls.state_functions = inspect.getmembers(state.BaseModel,
                                                 inspect.isfunction)

    def test_module_docstring_exists(self):
        """
        Check if the module has a docstring.
        """
        self.assertTrue(len(state.__doc__) >= 1)

    def test_class_docstring_exists(self):
        """
        Check if the State class has a docstring.
        """
        self.assertTrue(len(state.BaseModel.__doc__) >= 1)

    def test_function_docstrings_exist(self):
        """
        Check if all functions in State class have docstrings.
        """
        for func_name, func in self.state_functions:
            with self.subTest(func_name=func_name):
                self.assertTrue(len(func.__doc__) >= 1)


if __name__ == "__main__":
    unittest.main()
