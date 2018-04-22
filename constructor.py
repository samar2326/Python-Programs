"""
Wap to demonstrate constructor
"""
class student:
    name = ""
 
    def __init__(self, name):
        self.name = name
 
    def sayHello(self):
        print("Hello, my name is " + self.name)
 

Samar = student("Samar")
Sahil = student("Sahil")
Prabhat = student("Prabhat")
Samar.sayHello()
Sahil.sayHello()

