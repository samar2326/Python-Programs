""" To get a string from a given string where all occurrences of its first char have
been changed to '$', except the first char itself."""
def change_char(str):
  str = input("enter a string: ")
  char = str[0]
  length = len(str)
  str = str.replace(char, '$')
  str = char + str[1:]

  return str

print(change_char('str'))

