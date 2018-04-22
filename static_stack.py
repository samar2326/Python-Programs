"""
Wap to impliment stack
 """
class stack:
  def __init__(self):
    self.items = []
  def push(self, item):
    self.items.append(item)
  def pop(self):
    if not self.isEmpty():
      return self.items.pop()
  def isEmpty(self):
    return(self.items == [])
  def displaystack(self):
    print("New_stack:",self.items)

s=stack()
s.push("hello")
s.push("fruit")
s.push("flower")
s.push("Mango")
s.displaystack()
print("Deleted_item:",s.pop())
print("Deleted_item:",s.pop())
s.displaystack()
