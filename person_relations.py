# importing the required libraries

import constants       
import customized_exceptions

# Class to instantiate each person in the family

class Person:          
    def __init__(self, name, gender, spouse=None, father=None, mother=None):  # constructor
        self.name, self.gender, self.spouse, self.father, self.mother = name, gender, spouse, father, mother
        self.daughters, self.sons = [],[]
    def add_spouse(self, spouse):
        self.spouse = spouse

    # connecting and adding children to parents
    def add_children(self, child):
        if(self.spouse is None or self.gender == constants.MALE):
            raise customized_exceptions.ChildAdditionFailedError(constants.CHILD_ERROR)
        else:
            self.daughters.append(child) if child.gender == constants.FEMALE else self.sons.append(child)
            self.spouse.daughters.append(child) if child.gender == constants.FEMALE else self.spouse.sons.append(child)
            child.mother = self
            child.father = self.spouse

    # Business logic of all possible relations person have with each other

    def fetch_sisters(self):
        if self.mother is None:
            raise customized_exceptions.InsufficientInformationError(constants.INFORMATION_ERROR)
        else:
            sisters = []
            mother = self.mother
            daughters = mother.daughters
            for daughter in daughters:
                if(self.name == daughter.name):
                    continue
                else:
                    sisters.append(daughter)
            return sisters

   
    def fetch_brothers(self):
        if self.mother is None:
            raise customized_exceptions.InsufficientInformationError(constants.INFORMATION_ERROR)
        else:
            brothers = []
            mother = self.mother
            sons = mother.sons
            for son in sons:
                if(self.name == son.name):
                    continue
                else:
                    brothers.append(son)
            return brothers
            

    def fetch_maternal_uncles(self):
        if self.mother is None:
            raise customized_exceptions.NullPointerError(constants.NULLPOINTER_ERROR)
        else:
            mother = self.mother
            return mother.fetch_brothers()

    def fetch_paternal_uncles(self):
        if self.father is None:
            raise customized_exceptions.NullPointerError(constants.NULLPOINTER_ERROR)
        else:
            father = self.father
            return father.fetch_brothers()
    
    def fetch_paternal_aunts(self):
        if self.father is None:
            raise customized_exceptions.NullPointerError(constants.NULLPOINTER_ERROR)
        else:
            father = self.father
            return father.fetch_sisters()
        

    def fetch_maternal_aunts(self):
        if(self.mother is None):
            raise customized_exceptions.NullPointerError(constants.NULLPOINTER_ERROR)
        else:
            mother = self.mother
            return mother.fetch_sisters()


    def fetch_spouse(self):
        return self.spouse
       

    def fetch_sister_in_laws(self):
        In_Laws = []
        try:
            brothers = self.fetch_brothers()
        except customized_exceptions.InsufficientInformationError:
            brothers = None
        else:
            In_Laws.extend([brother.spouse for brother in brothers if brother.spouse is not None])
        if self.spouse is not None:
            try:
                spouse_sisters = self.spouse.fetch_sisters()
            except customized_exceptions.InsufficientInformationError:
                spouse_sisters = None
            else:
                In_Laws.extend(spouse_sisters)
        return In_Laws

    def fetch_brother_in_laws(self):
        In_Laws = []
        try:
            sisters = self.fetch_sisters()
        except customized_exceptions.InsufficientInformationError:
            sisters = None
        else:
            In_Laws.extend([sister.spouse for sister in sisters if sister.spouse is not None])
        if self.spouse is not None:
            try:
                spouse_brothers = self.spouse.fetch_brothers()
            except customized_exceptions.InsufficientInformationError:
                spouse_brothers = None 
            else:
                In_Laws.extend(spouse_brothers)
        return In_Laws

    def fetch_children(self):
        return self.daughters + self.sons
