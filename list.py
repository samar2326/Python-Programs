list=['n','v','d','m','w','n']
print(list[0])
print(list[2])

new_list=list
print("new list:",new_list)
print("old list:",list)

list.append(7)
print(list)
list.extend([4,14,17])
print(list)

count= list.count('n')
print("the count of n is:",count)

del list[3]
print(list)

index= list.index('n')
print("the index of n is:",index)