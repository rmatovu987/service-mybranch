#!/usr/bin/python3
"""
Define unittests for models/base_model.py

Unittest classes:
        TestModelDocs: tests documentation of base model
        TestBaseModel: tests the code behaviour of the base model
"""

from datetime import datetime
import time
from time import sleep
import models
import unittest
from unittest import mock
import os
import inspect

BaseModel = models.base_model.BaseModel
module_doc = models.base_model.__doc__


class TestModelDocs(unittest.TestCase):
        """ Test documentation and pep style of BaseModel """
        @classmethod
        def setUpClass(self):
                ''' docstrings tests set up '''
                self.base_funcs = inspect.getmember(BaseModel, inspect.isfunction)

        def test_valid_pep8(self):
                ''' tests that the model follows pep8 style '''
                for path in ['models/base_model.py',
                                'tests/test_models/test_base_model.py']:
                        with self.subTest(path=path):
                                errors = pycodestyle.Checker(path).check_all()
                                self.assertEqual(errors, 0)

        def test_module_docs(self):
                '''Test that module is documented'''
                self.assertIsNot(module_doc, None, 'please document base_model.py')
                self.assertTrue(len(module_doc) > 1, 'please document base_model.py')

        def test_class_docs(self):
                '''tests for class-BaseModel documentation'''
                self.assertIsNot(BaseModel.__doc__, None, 'please document the BaseModel class')
                self.assertTrue(len(BaseModel.__doc__) >= 1, 'please document the BaseModel class')

        def test_func_docs(self):
                '''tests that all class methods are well documented'''
                for func in self.base_funcs:
                        with self.subTest(function=func):
                                self.assertIsNot(
                                        func[1].__doc__, None,
                                        'Please document {:s} method'.format(func[0]))
                                self.assertTrue(
                                        len(func[1].__doc__) > 1,
                                        'please document method {:s}'.format(func[0]))

class TestBaseModel(unittest.TestCase):
        '''test code functionality of BaseModel'''
        def test_instantiation(self):
                '''test object creation'''
                inst = BaseModel()
                self.assertIs(type(inst), BaseModel)
                inst.name = 'S@mb'
                inst.number = 97
                attrs_types = {
                        "id": str,
                        "creation": datetime,
                        "update": datetime,
                        "name": str,
                        "number": int
                }
                for attr, typ in attrs_types.items():
                        with self.subTest(attr=attr, typ=typ):
                                self.assertIn(attr, inst.__dict__)
                                self.assertIs(type(inst.__dict__[attr]), typ)
                self.assertEqual(inst.name, "S@mb")
                self.asssertEqual(inst.number, 97)

        def test_datetime_attributes(self):
                '''test datetime objects for differenct BaseModel instances'''
                instime = datetime.now()
                inst1 = BaseModel()
                objtime = datetime.now()
                self.assertTrue(instime <= inst1.creation <= objtime)
                time.sleep(0.5)
                instime = datetime.now()
                inst2 = BaseModel()
                objtime = datetime.now()
                self.assertTrue(instime <= inst2.creation <= objtime)
                self.assertEqual(inst1.creation, inst1.update)
                self.assertEqual(inst2.creation, inst2.update)
                self.assertNotEqual(inst1.creation, inst2.creation)
                self.assertNotEqual(inst1.update, inst2.update)

        def test_uuid(self):
                '''test that id is valid uuid '''
                inst1 = BaseModel()
                inst2 = BaseModel()
                for inst in [inst1, inst2]:
                        uuid = inst.id
                        with self.subTest(uuid=uuid):
                                self.assertIs(type(uuid), str)
                                self.assertRegex(uuid,
                                        '^[0-9a-f]{8}-[0-9a-f]{4}'
                                        '-[0-9a-f]{4}-[0-9a-f]{4}'
                                        '-[0-9a-f]{12}$')
                self.assertNotEqual(inst1.id, inst2.id)

        def test_to_dict(self):
                '''test object to dictionary conversion'''
                tst_model = BaseModel()
                tst_model.name = "S@mb"
                tst_model.number = 97
                my_dct = tst_model.to_dict()
                attrs = ['id',
                         'creation',
                         'update',
                         'name',
                         'number',
                        '__class__']
                self.assertCountEqual(my_dct.keys(), attrs)
                self.assertEqal(my_dct['__class__'], 'BaseModel')
                self.assertEqual(my_dct['name'], 'S@mb')
                self.assertEqual(my_dct['number'], 97)

        def test_to_dict_values(self):
                '''test dictionary values'''
                tfom = '%Y-%/m-%dT%H:%M:%S.%f'
                bm = BaseModel()
                new_dct = bm.to_dict()
                self.assertEqual(new_dct['__class__'], 'BaseModel')
                self.assertEqual(type(new_dct['creation']), str)
                self.assertEqual(type(new_dct['update']), str)
                self.assertEqual(new_dct['creation'], bm.creation.strftime(tfom))
                self.assertEqual(new_dct['update'], bm.update.strftime(tfom))

        def test_str(self):
                '''test for correct string representation from __str__ method'''
                inst = BaseModel()
                my_string = "[BaseModel] ({}) {}".format(inst.id, inst.__dict__)
                self.assertEqual(my_string, str(inst))

        @mock.patch('models.storage')
        def test_save(self):
                ''' test update of update attribute and storage.save call'''
                 bm = BaseModel()
                creation1 = bm.creation
                update1 = bm.update
                bm.save()
                creation2 = bm.creation
                update2 = bm.update
                self.assertNotEqual(update1, update2)
                self.assertEqual(creation1, creation2)
                self.assertTrue(mock_storage.new.called)
                self.assertTrue(mock_storage.save.called)

if __name__ == '__main__':
        '''
        Main Tests
        '''
        unittest.main


