from __future__ import unicode_literals
from django.contrib.auth.models import AbstractUser
from django.db import models

from django.forms import ModelForm
from django.utils.html import escape, mark_safe



class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)


class Subject(models.Model):
    name = models.CharField(max_length=30)
    color = models.CharField(max_length=7, default='#007bff')

    def __str__(self):
        return self.name

    def get_html_badge(self):
        name = escape(self.name)
        color = escape(self.color)
        html = '<span class="badge badge-primary" style="background-color: %s">%s</span>' % (color, name)
        return mark_safe(html)


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.user.username


Dep_Choices=((1,'CSE'),(2,'ECE'),(3,'EIE'),('4','MECH'),('5','CIV'),)
Year_Choices=((1,'I'),(2,'II'),(3,'III'),(4,'IV'),)
Sec_Choices=((1,'1'),(2,'2'),(3,'3'),(4,'4'),)

class MyModel(models.Model):
	year=models.CharField(max_length=6,choices=Year_Choices,default=None)
	department=models.CharField(max_length=6,choices=Dep_Choices,default=None)
	section=models.CharField(max_length=6,choices=Sec_Choices,default=None)

class DetailsForm(ModelForm):

	class Meta:
		model=MyModel
		fields=['year','department','section']

class Event(models.Model):
     name = models.CharField('Event Name', max_length=120)
     event_date = models.DateTimeField('Event Date')
     venue = models.CharField(max_length=120)
     manager = models.CharField(max_length = 60)
     description = models.TextField(blank=True)

class ClassToStudent_Mapping(models.Model):
    ClassId = models.TextField('Class ID')
    RollNo = models.TextField('Roll Number')

    def __str__(self):
        return self.ClassId

    def __str__(self):
        return self.RollNo

class ClassToSub_Mapping(models.Model):
    ClassId = models.TextField('Class ID')
    Subject1 = models.TextField('Subject-1')
    Subject2 = models.TextField('Subject-2')
    Subject3 = models.TextField('Subject-3')
    Subject4 = models.TextField('Subject-4')
    Subject5 = models.TextField('Subject-5')
    Subject6 = models.TextField('Subject-6')
    Subject7 = models.TextField('Subject-7')
    Subject8 = models.TextField('Subject-8')
    Subject9 = models.TextField('Subject-9')
    Subject10 = models.TextField('Subject-10')
    Subject11 = models.TextField('Subject-11')
    Subject12 = models.TextField('Subject-12')


class CumulativeAttendance(models.Model):
    RollNo = models.TextField('Roll Number')
    Subject1 = models.IntegerField('Subject-1')
    Subject2 = models.IntegerField('Subject-2')
    Subject3 = models.IntegerField('Subject-3')
    Subject4 = models.IntegerField('Subject-4')
    Subject5 = models.IntegerField('Subject-5')
    Subject6 = models.IntegerField('Subject-6')
    Subject7 = models.IntegerField('Subject-7')
    Subject8 = models.IntegerField('Subject-8')
    Subject9 = models.IntegerField('Subject-9')
    Subject10 = models.IntegerField('Subject-10')
    Subject11 = models.IntegerField('Subject-11')
    Subject12 = models.IntegerField('Subject-12')


class DailyAttendance(models.Model):
    RollNo = models.TextField('Roll Number')
    Date_c = models.DateField('Date')
    Subject1 = models.IntegerField('Subject-1')
    Subject2 = models.IntegerField('Subject-2')
    Subject3 = models.IntegerField('Subject-3')
    Subject4 = models.IntegerField('Subject-4')
    Subject5 = models.IntegerField('Subject-5')
    Subject6 = models.IntegerField('Subject-6')
    Subject7 = models.IntegerField('Subject-7')
    Subject8 = models.IntegerField('Subject-8')
    Subject9 = models.IntegerField('Subject-9')
    Subject10 = models.IntegerField('Subject-10')
    Subject11 = models.IntegerField('Subject-11')
    Subject12 = models.IntegerField('Subject-12')


class DidClassHappenOnDate(models.Model):
    ClassId = models.TextField('Class ID')
    Date_c = models.DateField('Date')
    Subject1 = models.IntegerField('Subject-1')
    Subject2 = models.IntegerField('Subject-2')
    Subject3 = models.IntegerField('Subject-3')
    Subject4 = models.IntegerField('Subject-4')
    Subject5 = models.IntegerField('Subject-5')
    Subject6 = models.IntegerField('Subject-6')
    Subject7 = models.IntegerField('Subject-7')
    Subject8 = models.IntegerField('Subject-8')
    Subject9 = models.IntegerField('Subject-9')
    Subject10 = models.IntegerField('Subject-10')
    Subject11 = models.IntegerField('Subject-11')
    Subject12 = models.IntegerField('Subject-12')

class ProfToSub_Mapping(models.Model):
    ClassId = models.TextField('Class ID')
    Professor = models.TextField('Professor')
    SubjectId = models.IntegerField('Subject Id')


class profToSub(models.Model):
    roll = models.TextField('Roll No')
    prof = models.TextField('Professor')
    subId = models.IntegerField('Subject Id')
