import unittest
import cmd
from models.base_model import BaseModel

class TestHBNBCommand(unittest.TestCase):

    def setUp(self):
        self.cmd = HBNBCommand()

    def test_create(self):
        # Test with valid input
        self.assertEqual(self.cmd.do_create("BaseModel"), "BaseModel.{}".format(BaseModel.id))

        # Test with invalid class name
        self.assertEqual(self.cmd.do_create("InvalidClass"), "** class doesn't exist **")

        # Test without class name
        self.assertEqual(self.cmd.do_create(""), "** class name missing **")

    def test_show(self):
        # Test with valid input
        self.cmd.do_create("BaseModel")
        instance_id = BaseModel.id
        expected_output = "[BaseModel] ({}) {}".format(instance_id, BaseModel.__dict__)
        self.assertEqual(self.cmd.do_show("BaseModel {}".format(instance_id)), expected_output)

        # Test with invalid class name
        self.assertEqual(self.cmd.do_show("InvalidClass {}".format(instance_id)), "** class doesn't exist **")

        # Test with invalid instance id
        self.assertEqual(self.cmd.do_show("BaseModel InvalidId"), "** no instance found **")

        # Test without instance id
        self.assertEqual(self.cmd.do_show("BaseModel"), "** instance id missing **")

        # Test without class name
        self.assertEqual(self.cmd.do_show(""), "** class name missing **")

    def test_destroy(self):
        # Test with valid input
        self.cmd.do_create("BaseModel")
        instance_id = BaseModel.id
        self.assertEqual(self.cmd.do_destroy("BaseModel {}".format(instance_id)), None)

        # Test with invalid class name
        self.assertEqual(self.cmd.do_destroy("InvalidClass {}".format(instance_id)), "** class doesn't exist **")

        # Test with invalid instance id
        self.assertEqual(self.cmd.do_destroy("BaseModel InvalidId"), "** no instance found **")

        # Test without instance id
        self.assertEqual(self.cmd.do_destroy("BaseModel"), "** instance id missing **")

        # Test without class name
        self.assertEqual(self.cmd.do_destroy(""), "** class name missing **")

    def test_all(self):
        # Test with valid input
        self.cmd.do_create("BaseModel")
        instance_id = BaseModel.id
        expected_output = "[BaseModel] ({}) {}".format(instance_id, BaseModel.__dict__)
        self.assertEqual(self.cmd.do_all("BaseModel"), [expected_output])

        # Test with invalid class name
        self.assertEqual(self.cmd.do_all("InvalidClass"), [expected_output])

    def test_sort_alphabets(self):
        # test for basic sorting of words
        self.assertEqual(sort_alphabets(["dog", "cat", "horse"]), ["cat", "dog", "horse"])
        self.assertEqual(sort_alphabets(["apple", "banana", "cherry"]), ["apple", "banana", "cherry"])
        
        # test for sorting of words with uppercase letters
        self.assertEqual(sort_alphabets(["Apple", "Banana", "Cherry"]), ["Apple", "Banana", "Cherry"])
        
        # test for sorting of words with special characters and numbers
        self.assertEqual(sort_alphabets(["dog1", "cat2", "horse#"]), ["cat2", "dog1", "horse#"])
        
        # test for sorting of words with empty string
        self.assertEqual(sort_alphabets(["", "dog", "cat"]), ["", "cat", "dog"])
        
        # test for sorting of words with multiple spaces
        self.assertEqual(sort_alphabets(["dog  ", " cat", "  horse"]), [" cat", "  horse", "dog  "])
    def test_all(self):
        # Test with valid input
        self.cmd.do_create("BaseModel")
        instance = BaseModel.find(BaseModel.id)
        expected_output = str(instance)
        result = self.cmd.do_all("BaseModel")

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], expected_output)

        # Test with invalid class name
        result = self.cmd.do_all("InvalidClass")
        self.assertEqual(result, "** class doesn't exist **")
