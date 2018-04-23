#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"

import cgi
import MySQLdb

data = cgi.FieldStorage()
un=data.getvalue('name')
pwd= data.getvalue('password')
con=MySQLdb.connect("127.0.0.1","root","","logindb",3306)
ins_q = "insert into login(name,pswd) values('"+un+"','"+pwd+"')"
cur=con.cursor()
cur.execute(ins_q)
con.commit()
con.close()
print "!!login successed finally "

