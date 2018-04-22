#__________________ method 1 _____________________#
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
    print("Queue:",self.items)

q=queue()
print("Inserting elements in queue:")
q.enqueue("mango")
q.displayqueue()
q.enqueue("banana")
q.displayqueue()
q.enqueue("grapes")
q.displayqueue()
q.enqueue("orange")
q.displayqueue()
q.enqueue("guava")
q.displayqueue()
print("Deleting elements in queue:")
print("Deleted item:",q.dequeue())
q.displayqueue()
print("Deleted item:",q.dequeue())
q.displayqueue()
print("\n\n\n")

