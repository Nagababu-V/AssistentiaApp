from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, render_to_response
from django.utils import timezone
import datetime
from classroom.models import User
from django.template import RequestContext, loader
from django.template import Template, Context
from django.template.defaulttags import register
from classroom.models import MyModel
from classroom.models import DetailsForm
from classroom.forms import PostForm
from django.http import HttpResponseRedirect
from classroom.Python import MarkAttendanceCode

from classroom.forms import PostForm
"""================================================"""
from subprocess import call
from classroom.forms import PostForm
import os
from shutil import rmtree
import subprocess
import face_recognition
import pickle
import cv2
from matplotlib import pyplot as plt
import sqlite3

"""-----------------------------------------"""

#globalVals

#set Raspi IP
raspiIP = "192.168.0.2"

#setTrainingParams

#Set other parameters
raspiPass = "aditya123*"
raspiUser = "pi"
tmpDirRpi="/home/pi/Assistentia/RaspberryPiCode/tmp/"
codeDirRpi="/home/pi/Assistentia/RaspberryPiCode/"
tmpDirLocal="tmp/"
serverPass = "aditya123*"
serverUser = "aditya"
classDir = "/home/aditya/tmp/Asistencia/django_school/classroom/Python/classes/"
pickleName = "training.pickle"

#sqlitePath
sqlite3Path = '/home/aditya/tmp/mar-6-eve/Asistencia/django_school/db.sqlite3'
"""-----------------------------------------"""
"""================================================"""

var1 = ''
cid1=''
sid1=''
usrname=''



class SignUpView(TemplateView):
    template_name = 'registration/signup.html'

def home(request):
    if request.user.is_authenticated:
        if request.user.is_teacher:
            usrname = request.user.username
            return render(request, 'classroom/teachers/LecturerLogin.html')
        else:
            return render(request, 'classroom/students/StudentLogin.html')
    return render(request, 'classroom/home.html')



def MarkAttendance(request):
        now = timezone.now()
        users = User.objects.all()
        return render(request, 'classroom/MarkAttendance.html', {'users': users})



class test_code:
    def code(self,classId, UsrName):
        var1 = classId
        print(UsrName)
        print(classId)

    def code1(self, studentID):
        sid1=studentID
        print(sid1)

var='student-3'
sid1=var


def OneStudent(request):
        return render(request, 'classroom/OneStudent.html')


def index(request):
        now = timezone.now()
        users = User.objects.all()
        return render(request, 'classroom/display.html', {'users': users})

def Details(request):
        now = timezone.now()
        users = User.objects.all()
        return render(request, 'classroom/GetAttendnaceDetails.html', {'users': users})

def TClassDetails(request):
        return render(request, 'classroom/TGetClassDetails.html')

def GClassDetails(request):
        return render(request, 'classroom/GGetClassDetails.html')

def GPrint(request):
        return render(request, 'classroom/Gprint.html')

def TPrint(request):
        return render(request, 'classroom/Tprint.html')

def GetClassDetailsToMark(request):
        return render(request, 'classroom/ClassDetailsToMark.html')




def AllStudents(request):
        now = timezone.now()
        users = User.objects.filter(id = 5, username=var)
        return render(request, 'classroom/AllStudentDetails.html', {'users': users})


def IndividualStudent(request):
        now = timezone.now()
        users = User.objects.filter(username = sid1)
        return render(request, 'classroom/IndividualStudentDetails.html', {'users': users})

@login_required
def GetClassDetails(request):
    model=MyModel
    form_class=DetailsForm
    return render_to_response(
    'GetClassDetails.html',
    )

def index1(request):
    if request.method=="GET":
        py_obj=MarkAttendanceCode.test_code()
        py_obj.code()
        return render(request, 'classroom/MarkAttendance.html')

def Tpost_form_upload(request):
    if request.method == 'GET':
        form = PostForm()
    else:
        # A POST request: Handle Form Upload
        form = PostForm(request.POST) # Bind data from request.POST into a PostForm
        usrname = request.user.username
        #print(usrname)
        # If data is valid, proceeds to create a new post and redirect the user
        if form.is_valid():
            classID = form.cleaned_data['classID']
            py_obj=test_code()
            py_obj.code(classID, usrname)

            #return HttpResponseRedirect(reverse('post_detail',
                                                #kwargs={'post_id': post.id}))
    return render(request, 'classroom/TGetClassDetails.html', {
        'form': form,
    })


def PrintOneStudent(request):
    if request.method == 'GET':
        form = PostForm()
    else:
        # A POST request: Handle Form Upload
        form = PostForm(request.POST) # Bind data from request.POST into a PostForm

        # If data is valid, proceeds to create a new post and redirect the user
        if form.is_valid():
            studentID = form.cleaned_data['classID']
            py_obj=test_code()
            py_obj.code1(studentID)

            #return HttpResponseRedirect(reverse('post_detail',
                                                #kwargs={'post_id': post.id}))
    return render(request, 'classroom/OneStudent.html', {
        'form': form,
    })



def Gpost_form_upload(request):
    if request.method == 'GET':
        form = PostForm()
    else:
        # A POST request: Handle Form Upload
        form = PostForm(request.POST) # Bind data from request.POST into a PostForm

        # If data is valid, proceeds to create a new post and redirect the user
        if form.is_valid():
            classID = form.cleaned_data['classID']
            py_obj=MarkAttendanceCode.test_code()
            py_obj.code(classID)

            #return HttpResponseRedirect(reverse('post_detail',
                                                #kwargs={'post_id': post.id}))
    return render(request, 'classroom/GGetClassDetails.html', {
        'form': form,
    })
