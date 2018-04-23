#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"

import MySQLdb
 
#import sys
 
connection = MySQLdb.connect("127.0.0.1","root","","logindb",3306)
 
cursor = connection.cursor ()
try: 
 cursor.execute ("select * from login")
 
 data = cursor.fetchall ()
 print "The Selected Table data is:"
 print "<br><br>"
 for row in data:
 
  print row[0], row[1]
  print "<br>"

 cursor.close ()
 
 connection.close ()
except:
 print "Error: unable to fecth data"
 
#sys.exit()