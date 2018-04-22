
#Program to demonstrate Aggregation in python

class A(object):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def addNums():
         self.b + self.c

class B(object):
    def __init__(self, d, e, A):
        self.d = d
        self.e = e
        self.A = A

    def addAllNums(self):
        x = self.d + self.e + self.A.b + self.A.c
        return x

obj1 = A("my", 24, 46)
obj2 = B(51, 18, obj1)

print ("The addition of integer value is" , obj2.addAllNums())



