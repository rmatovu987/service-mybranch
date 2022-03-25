#!/usr/bin/python3
"""
Defines the unittests for the Bank model 
"""

from datetime import datetime
import inspect
import models
from models import bank
from models.base_model import BaseModel
import pep8
import unittest
Bank = bank.Bank


class TestBankDocs(unittest.TestCase):
    """Tests to check the documentation and pep style of Bank class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.bank_funcs = inspect.getmembers(State, inspect.isfunction)
        
    def test_pep8_conformance_bank(self):
        """Test that models/bank.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/bank.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
        
    def test_pep8_conformance_test_bank(self):
        """Test that test_bank.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_bank.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
        
    def test_bank_module_docstring(self):
        """Test for the bank.py module docstring"""
        self.assertIsNot(bank.__doc__, None,
                         "Please provide docstrings for bank.py")
        self.assertTrue(len(bank.__doc__) >= 1,
                        "Please provide docstrings for bank.py")
        
    def test_bank_class_docstring(self):
        """Test for the Bank class docstrings"""
        self.assertIsNot(Bank.__doc__, None,
                         "Please document the Bank class")
        self.assertTrue(len(Bank.__doc__) >= 1,
                        "Please document the Bank class")
        
    def test_bank_func_docstrings(self):
        """Test for the presence of docstrings in Bank methods"""
        for func in self.bank_funcs:
            self.assertIsNot(func[1].__doc__, None,
                             "Please document method {:s}".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "Please document method {:s} ".format(func[0]))
            
class TestBank(unittest.TestCase):
    """Test the Bank class"""
    def test_is_subclass(self):
        """Test that Bank is a subclass of BaseModel"""
        bank = Bank()
        self.assertIsInstance(bank, BaseModel)
        self.assertTrue(hasattr(bank, "id"))
        self.assertTrue(hasattr(bank, "creation"))                                                 
        self.assertTrue(hasattr(bank, "update"))
        
    def test_name_attr(self):
        """Test that Bank has an empty string name attribute"""
        bank = Bank()
        self.assertTrue(hasattr(bank, "name"))
        if models.storage_t == 'db':
            self.assertEqual(bank.name, None)
        else:                                                                                                                       
            self.assertEqual(bank.name, "")
            
    def test_to_dict(self):
        """test to_dict method creates a dictionary representation of instance"""
        b = Bank()
        new_dct = b.to_dict()
        self.assertEqual(type(new_dct), dict)
        self.assertFalse("_sa_instance_state" in new_dct)
        for attr in b.__dict__:
            if attr is not "_sa_instance_state":
                self.assertTrue(attr in new_dct)
        self.assertTrue("__class__" in new_dct)
        
    def test_to_dict_values(self):
        """test that values in dictionary returned from to_dict are correct"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        b = Bank()
                new_d = b.to_dict()
        self.assertEqual(new_d["__class__"], "Bank")
        self.assertEqual(type(new_d["creation"]), str)
        self.assertEqual(type(new_d["update"]), str)
        self.assertEqual(new_d["creation"], b.creation.strftime(t_format))
        self.assertEqual(new_d["update"], b.update.strftime(t_format))
        
    def test_str(self):
        """test that the str method outputs proper string representation of the object"""
        bank = Bank()
        string = "[Bank] ({}) {}".format(bank.id, bank.__dict__)
        self.assertEqual(string, str(bank))
