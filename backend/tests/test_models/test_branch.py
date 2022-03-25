#!/usr/bin/python3
"""
Defines unittests for the branch model
"""

from datetime import datetime
import inspect
import models
from models import branch
from models.base_model import BaseModel
import pep8
import unittest
Branch = branch.Branch


class TestCityDocs(unittest.TestCase):
    """Tests to check the documentation and pep style of Branch class"""

    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.branch_funcs = inspect.getmembers(City, inspect.isfunction)

    def test_pep8_conformance_branch(self):
        """Test that models/branch.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/branch.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_branch_module_docstring(self):
        """Test for the branch.py module docstring"""
        self.assertIsNot(city.__doc__, None,
                         "branch.py needs docstrings")
        self.assertTrue(len(city.__doc__) >= 1,
                        "branch.py needs docstrings")

    def test_branch_class_docstring(self):
        """Test for the Branch class docstrings"""
        self.assertIsNot(City.__doc__, None,
                         "Please document the Branch class")
        self.assertTrue(len(City.__doc__) >= 1,
                        "Please document the Branch class")

    def test_branch_func_docstrings(self):
        """Test for the presence of docstrings in Branch methods"""
        for func in self.branch_funcs:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))

class TestBranch(unittest.TestCase):
    """Test the Branch class"""
    def test_is_subclass(self):
        """Test that Branch is a subclass of BaseModel"""
        branch = Branch()
        self.assertIsInstance(branch, BaseModel)
        self.assertTrue(hasattr(city, "id"))
        self.assertTrue(hasattr(city, "creation"))
        self.assertTrue(hasattr(city, "update"))

    def test_name_attr(self):
        """Test that Branch has name attribute, and it's an empty string"""
        branch = Branch()
        self.assertTrue(hasattr(branch, "name"))
        if models.storage_t == 'db':
            self.assertEqual(branch.name, None)
        else:
            self.assertEqual(branch.name, "")

    def test_bank_id_attr(self):
        """Test that Branch has attribute bank_id, and it's an empty string"""
        branch = Branch()
        self.assertTrue(hasattr(branch, "bank_id"))
        if models.storage_t == 'db':
            self.assertEqual(branch.bank_id, None)
        else:
            self.assertEqual(branch.bank_id, "")

    def test_to_dict_creates_dict(self):
        """test to_dict method creates a dictionary with proper attrs"""
        brnch = Branch()
        new_dct = brnch.to_dict()
        self.assertEqual(type(new_dct), dict)
        self.assertFalse("_sa_instance_state" in new_dct)
        for attr in brnch.__dict__:
            if attr is not "_sa_instance_state":
                self.assertTrue(attr in new_dct)
        self.assertTrue("__class__" in new_dct)

    def test_to_dict_values(self):
        """test that values in dict returned from to_dict are correct"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        brnch = Branch()
        new_dct = brnch.to_dict()
        self.assertEqual(new_dct["__class__"], "Branch")
        self.assertEqual(type(new_dct["creation"]), str)
        self.assertEqual(type(new_dct["update"]), str)
        self.assertEqual(new_dct["creation"], brnch.creation.strftime(t_format))
        self.assertEqual(new_dct["update"], brnch.update.strftime(t_format))

    def test_str(self):
        """test that the str method has the correct output"""
        branch = Branch()
        string = "[Branch] ({}) {}".format(branch.id, branch.__dict__)
        self.assertEqual(string, str(branch))

if __name__ == "__main__":
    unittest.main
