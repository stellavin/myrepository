from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
import MySQLdb

##--------------------------------------------------------------------------------------------------------
def get_fname(request,fid):
	conn=MySQLdb.connect(host="localhost",user="stella",password="stl",db="sis")
	
	cursor=conn.cursor()
	cursor.execute("select fname from sis_faculty where fid='"+fid+"'")
	if cursor.rawcount==0:
		html="<html><body>There is no Faculty member with id %s.</body></html>" % fid
	else:
		
		row=cursor.fetchone()
		html="<html><body>The Faculty name is %s.</body></html>" % row[0]
	return HttpResponse(html)
##-------------------------------------------------------------------------------------------------------

	#Explicit html code and templates can be used in the same function


##------------------------------------------------------------------------------------------------------
def get_cname(request, cname):
	conn=MySQLdb.connect(host="localhost", user="stella", password="stl",db="sis")
	
	cursor=conn.cursor()
	cursor.execute ("select cname,credit from sis_course where cnum='"+cnum+"'")
	# this code is used to display the error message (explicit html code)
	if cursor.rawcount==0:
		html="<html><body> There is no course with number %s. </body></html>" % cnum
		
		# this code is used to display the result of successive search (template)
	else:
		row=cursor.fetchone()
		t=get-template('cname.html')
		c=Context({'cnum':cnum, 'cname':row[0], 'credit':row[1]}) 
		
		html=t.render(c)
	return HttpResponse(html)
#-------------------------------------------------------------------------------------------------------------
