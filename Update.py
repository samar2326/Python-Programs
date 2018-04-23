#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"


import MySQLdb
 
#import sys


connection = MySQLdb.connect("127.0.0.1","root","","logindb",3306)
 
cursor = connection.cursor ()
try: 
 cursor.execute ("UPDATE login SET name = 'Somil Kumar Shukla' WHERE eid = 1250")
 
 
 cursor.close ()
 
 connection.close ()
 print "Record Updated Successfully!!!"
except:
 print "Error: unable to delete data"
 
#sys.exit()