# Importing required libraries
from person_relations import Person
import constants
import customized_exceptions

class Family:
    # To store all the family members, so that we can search from the list
    family_members = []
    # To add root node
    def __init__(self, head):
        self.head = head
        self.family_members.append(head)
        
    def search(self, name):
        for member in self.family_members:
            if member.name == name:
                return member
        raise customized_exceptions.PersonNotFoundError(constants.PERSON_ERROR) 

# Functions which will add child and spouse to the each person object
    def add_spouse_to_family(self, member, spouse):
        member = self.search(member.name)
        member.add_spouse(spouse)
        spouse.add_spouse(member)
        self.family_members.append(spouse)

    def add_child_to_family(self, mother, child):
        mother = self.search(mother.name)
        mother.add_children(child)
        self.family_members.append(child)

# cases of different relations

    def get_relationship(self, member, relation):
        person = self.search(member.name)

        if(relation == constants.SON):
            result = [son.name for son in person.sons]

        elif(relation == constants.DAUGHTER):
            result = [daughter.name for daughter in person.daughters]

        elif(relation == constants.SIBLINGS):
            result = [sibling.name for sibling in person.fetch_brothers()+ person.fetch_sisters()]

        elif(relation == constants.PATERNAL_UNCLE):
            result = [paternal_uncle.name for paternal_uncle in person.fetch_paternal_uncles()]

        elif(relation == constants.PATERNAL_AUNT):
            result = [paternal_aunt.name for paternal_aunt in person.fetch_paternal_aunts()]

        elif(relation == constants.MATERNAL_UNCLE):
            result = [maternal_uncle.name for maternal_uncle in person.fetch_maternal_uncles()]

        elif(relation == constants.MATERNAL_AUNT):
            result = [maternal_aunt.name for maternal_aunt in person.fetch_maternal_aunts()]

        elif(relation == constants.SISTER_IN_LAW):
            result = [sister_in_law.name for sister_in_law in person.fetch_sister_in_laws()]

        elif(relation == constants.BROTHER_IN_LAW):
            result = [brother_in_law.name for brother_in_law in person.fetch_brother_in_laws()]

        else:
            raise customized_exceptions.CommandNotFoundError(constants.COMMAND_ERROR)

        if(len(result) == 0):
            raise customized_exceptions.NullPointerError(constants.NULLPOINTER_ERROR)

        return result
