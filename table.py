#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"

import cgi

data = cgi.FieldStorage()  
n=data.getvalue('table')
for i in range(1,11):
    print(n,"x",i,"=",n*i)
    print "<br>"	