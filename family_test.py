# Imprting libraries
import unittest
import sys
from family import Family
from person_relations import Person
import customized_exceptions

# Inheriting Testcase Class
class TestFamily(unittest.TestCase):

    def setUp(self):
        self.King = Person("King","M")
        self.family = Family(self.King)
        self.person_1 = Person("person1","M")
        self.person_2 = Person("person2","F")
    
    def test_search_function(self):
        with self.assertRaises(customized_exceptions.PersonNotFoundError):
            self.family.search(self.person_1)
    def test_child_addition(self):
        with self.assertRaises(customized_exceptions.ChildAdditionFailedError):
            self.family.add_child_to_family(self.King, self.person_1)
    def test_get_relationship(self):
        with self.assertRaises(customized_exceptions.CommandNotFoundError):
            self.family.get_relationship(self.King,"not related")

#Driver Function
if __name__=="__main__":
    unittest.main()