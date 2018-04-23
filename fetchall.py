#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"
import cgi
import MySQLdb
data = cgi.FieldStorage()
print "Hi0"
con=MySQLdb.connect("127.0.0.1","root","","logindb",3306)
print "Hi1"
cur = con.cursor()
Sel_sql = "SELECT * FROM LOGIN
print "Hi2"
#try:
cur.execute(sel_sql)
results = cur.fetchall()
for row in results:
print row[0],row[1]


db.close()
print "query execute successfully!!!"


