#!/usr/bin/python3
"""
Unit tests for the base_model module.

Usage:
    Run all tests: python3 -m unittest discover tests
    Run specific file: python3 -m unittest tests.test_models.test_base_model
"""

from models import base_model
import inspect
import unittest

class TestBaseModelDocumentation(unittest.TestCase):
    """
    TestBaseModelDocumentation: (class) - unittest subclass to 
    test docstrings in base_model module
    
    """

    @classmethod
    def setUpClass(cls):
        """
        setUpClass: (class method) - called before any tests are executed

        Sets up a list of all the functions in BaseModel.
        """
        cls.base_model_functions = inspect.getmembers(base_model.BaseModel, inspect.isfunction)

    def test_module_docstring_exists(self):
        """
        Check if the module has a docstring.
        """
        self.assertTrue(len(base_model.__doc__) >= 1)

    def test_class_docstring