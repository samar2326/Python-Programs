#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"
print "register here"

print """
<html>
<head>
</head>
<body>
<form action="code.py"  method="post">

Name
<input   type="text"   name="name"/><br/><br/>
Fname
<input type="text"   name="fname"/><br/><br/>
Gender:
<input type="radio"   name="a"  value="male"/> Male
<input type="radio"   name="a"   value="female"/> FeMale
<br/><br/>
Email:
<input type="email"   name="email"   value=""/>
<br/></br/>
Password:
<input type="password"  name ="password"/>
<br/><br/>
<input type ="submit"  value="REGISTER"/>
</form>

</body>



</html>
"""