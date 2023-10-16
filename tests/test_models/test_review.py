#!/usr/bin/python3
"""
Unit tests for the review module.

Usage:
    Run all tests: python3 -m unittest discover tests
    Run specific file: python3 -m unittest tests.test_models.test_review
"""

from models import review
import inspect
import unittest


class TestReviewDocumentation(unittest.TestCase):
    """
    TestReviewDocumentation: (class) - unittest subclass
    to test docstrings in review module

    """

    @classmethod
    def setUpClass(cls):
        """
        setUpClass: (class method) - called before any tests are executed

        Sets up a list of all the functions in Review class.
        """
        cls.review_functions = inspect.getmembers(review.BaseModel,
                                                  inspect.isfunction)

    def test_module_docstring_exists(self):
        """
        Check if the module has a docstring.
        """
        self.assertTrue(len(review.__doc__) >= 1)

    def test_class_docstring_exists(self):
        """
        Check if the Review class has a docstring.
        """
        self.assertTrue(len(review.BaseModel.__doc__) >= 1)

    def test_function_docstrings_exist(self):
        """
        Check if all functions in Review class have docstrings.
        """
        for func_name, func in self.review_functions:
            with self.subTest(func_name=func_name):
                self.assertTrue(len(func.__doc__) >= 1)


if __name__ == "__main__":
    unittest.main()
