# Program to demonstrate Composition in python
class A(object):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def addNums():
        self.b + self.c

class B(object):
    def __init__(self, d, e):
        self.d = d
        self.e = e
        self.A = A("my", 3, 20)

    def addAllNums(self):
        x = self.d + self.e + self.A.b + self.A.c
        return x

obj = B(19, 55)

print ("The addition value is" , obj.addAllNums())

