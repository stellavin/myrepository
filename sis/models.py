from django.db import models
#model include one class for each entity(table) in the database
# Create your models here.
class faculty(models.Model):
	#primary key is used to make the column unique
	#many to many relationship will result in creating a new table(entity)
	fid=models.CharField(max_length=9,primary_key=True)
	fname=models.CharField(max_length=40)
	
	def _unicode_(self):
		return u'%s,%s'%(self.fid,self.fname)

class course(models.Model):
	cnum=models.CharField(max_length=9,primary_key=True)
	cname=models.CharField(max_length=40)
	credit=models.IntegerField()
#each class impliments the _unicode_ function
# self is used to link or bind function to class
	def _unicode_(self):
		return u'%s,%s,%s'% (self.cnum, self.cname, self.credit)
		
class section(models.Model):
	snum=models.CharField(max_length=9, primary_key=True)
	cnum=models.ForeignKey(course, db_column='cnum')
	fid=models.ForeignKey(course, db_column='fid')
	semester=models.CharField (max_length=6)
	year=models.IntegerField()
	enrollment=models.IntegerField()
	capacity=models.IntegerField()
	
	def _unicode_(self):
		return u'%s,%s'%(self.snum,self.enrollment)
