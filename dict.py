"""
Wap to demonstarte dictionary and related functions"""
dict={'Roll no':'1613313069','Name':'Prashnat kumar','Course':'Bachelor of Technology','Branch':'I.T'}
print(dict)
dict1=dict.copy()
print("New dictionary is :",str(dict1))
print("value:",dict.items())
print("Start len:",len(dict))
dict.clear()
print("End len:",len(dict))
print(dict)
