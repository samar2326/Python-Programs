#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"


import MySQLdb
 
#import sys


connection = MySQLdb.connect("127.0.0.1","root","","logindb",3306)
 
cursor = connection.cursor ()
try: 
 cursor.execute ("delete from register where password=niet@123")
 
 
 cursor.close ()
 
 connection.close ()
 print "Record deleted Successfully!!!"
except:
 print "Error: unable to delete data"
 
#sys.exit()