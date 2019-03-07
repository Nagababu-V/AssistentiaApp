from __future__ import unicode_literals

from django.db import models

# Create your models here.
Dep_Choices=((1,'CSE'),(2,'ECE'),(3,'EIE'),('4','MECH'),('5','CIV'),)
Year_Choices=((1,'I'),(2,'II'),(3,'III'),(4,'IV'),)
Sec_Choices=((1,'1'),(2,'2'),(3,'3'),(4,'4'),)

class MyModel(models.Model):
	year=models.CharField(max_length=6,choices=Year_Choices,default=None)
	department=models.CharField(max_length=6,choices=Dep_Choices,default=None)
	section=models.CharField(max_length=6,choices=Sec_Choices,default=None)
