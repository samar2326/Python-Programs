class queue:
  def __init__(self):
    self.items = []
  def isEmpty(self):
    return self.items == []
  def enqueue(self,item):
    self.items.insert(0,item)
  def dequeue(self):
    return self.items.pop()
  def size(self):
    return len(self.items)
  def displayqueue(self):
    print("New_stack:",self.items)

q=queue()

q.enqueue("ramayana")
q.enqueue("karna")
q.enqueue("arjuna")
q.enqueue("mahabharta")
q.enqueue("radha")
q.displayqueue()

print("Deleted item:",q.dequeue())
print("Deleted item:",q.dequeue())
q.displayqueue()

