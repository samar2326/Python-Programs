""" Program 4: WAP to display the Fibonacci sequence up to n-th term where n is provided by the user"""

n = int(input("Nos of terms: "))
n1 = 0
n2 = 1
count = 0
if n == 1:
   print("Fibonacci sequence upto",n)
   print(n1)
else:
   print("Fibonacci sequence upto",n)
   while count < n:
       print(" ")
       print(n1)
       temp = n1 + n2
       n1 = n2
       n2 = temp
       count += 1
