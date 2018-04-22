#_________________________ method 1 __________________________#
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
    print("Stack:",self.items)

s=stack()
s.push("sita")
s.displaystack()
s.push("gita")
s.displaystack()
s.push("ram")
s.displaystack()
s.push("shyam")
s.displaystack()
print("Deleted_item:",s.pop())
s.displaystack()
print("Deleted_item:",s.pop())
s.displaystack()
print("\n\n\n")


