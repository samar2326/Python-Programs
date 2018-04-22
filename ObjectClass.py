"""
WAP to demonstrate working of classes and objects
"""
class Student:
    
   def __init__(self, rollno, name):
       
      self.rollno = rollno  
      self.name = name  
   def displayStudent(self):  
      print ("rollno:" , self.rollno,  ", name: ", self.name)  
emp1 = Student(1613313069, "Prashant kumar")  
emp2 = Student(1613313081, "Sahil Garg")  
emp3 = Student(1613313066, "Palak")
emp4 = Student(1613313079, "Rupali Singh")
emp5 = Student(1613313083, "Sandeepa")
emp6 = Student(2326051098, "Samraj Mishra")
emp7 = Student(2610199800,   "Rajnish Mishra")
emp1.displayStudent()  
emp2.displayStudent() 
emp3.displayStudent()
emp4.displayStudent()
emp5.displayStudent()
emp6.displayStudent()
emp7.displayStudent()
