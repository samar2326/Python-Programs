class person:
  def __init__(self,first,last):
    self.first = first
    self.last = last
  def name(self):
    return self.first + " " + self.last

class employee(person):
  def __init__(self,first,last,empnum):
    person.__init__(self,first,last)
    self.empnumber = empnum
  def getemployee(self):
    return self.name() + ", " + self.empnumber


a = person("Prashant","Kumar")
b = employee("SAhil","Garg","2326")

print("Using class 'person' :",a.name())
print("Inheritance from class 'person' :",b.getemployee())
