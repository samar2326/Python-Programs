#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"
import cgi
import MySQLdb
data = cgi.FieldStorage()  
n=data.getvalue('name')
#print n 
#print n
fn=data.getvalue('fname') 
#print fn
g=data.getvalue('a') 
#print g
em=data.getvalue('email')
p=data.getvalue('password') 
con=MySQLdb.connect("127.0.0.1","root","","nietdb",3306)
query="insert into register(name,fname,gender,email,password) values ('"+n+"','"+fn+"','"+g+"','"+em+"','"+p+"')"
cur=con.cursor()
cur.execute(query)
con.commit()
con.close()
print "record submitted successfully"
#print p