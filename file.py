""" Wap to read and Write a file"""
file = open("friendship.txt","w")
file.write("A friend in need is a friend indeed\n")
file.write("Friends are really amazing\n")
file.write("Some friends become your lifeline\n")

# Read contents from a file :
file = open("friendship.txt")
temp = file.read()
print(temp)
