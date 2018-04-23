#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"
print " Login Here"
print """
<html>
<head></head>
<body>
<form action="dal.py" method="post"></br></br>
   UName
  <input  type ="text" name="name"/><br/><br/>
 Password
  <input  type ="password" name ="password"/><br/><br/>
  <input  type ="submit" value="Insert"/>
 </form>

<form action="fetchall1.py" method="post"></br></br>
   <input  type ="submit" vlaue ="select"/>
 </ form>

<form action="delete.py" method="post"></br></br>
Enter Name for delete:
  <input  type ="text" name="delname"/><br/><br/>
   <input  type ="submit" value ="delete"/>
 </form>

</body>
</html>
"""