""" 
WAP to demonstrate class method & static method""" 

# use of class method and static method.
from datetime import date
 
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
     
    # a class method to create a Person object by birth year.
    @classmethod
    def fromBirthYear(cls, name, year):
        return cls(name, date.today().year - year)
     
    # a static method to check if a Person is adult or not.
    @staticmethod
    def isAdult(age):
     return age > 18
 
person1 = Person('Samar', 19)
person2 = Person.fromBirthYear('Sahil', 1998)
person3 = Person.fromBirthYear('Rupali', 1995)
person4 = Person.fromBirthYear('Sandeepa',1994)
person5 = Person('Palak', 21)
print (person1.age)
print (person2.age)
print (person3.age)
print (person4.age)
print (person5.age) 
# print the result
print (Person.isAdult(22))
