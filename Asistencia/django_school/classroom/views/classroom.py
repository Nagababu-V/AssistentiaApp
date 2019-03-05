from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, render_to_response
from django.utils import timezone
import datetime
from classroom.models import User
from django.template import RequestContext, loader
from django.template import Template, Context
from django.template.defaulttags import register

class SignUpView(TemplateView):
    template_name = 'registration/signup.html'


def home(request):
    if request.user.is_authenticated:
        if request.user.is_teacher:
            return render(request, 'classroom/teachers/LecturerLogin.html')
        else:
            return render(request, 'classroom/students/StudentLogin.html')
    return render(request, 'classroom/home.html')


def index(request):
        now = timezone.now()
        users = User.objects.all()
        return render(request, 'classroom/display.html', {'users': users})

def Details(request):
        now = timezone.now()
        users = User.objects.all()
        return render(request, 'classroom/GetAttendnaceDetails.html', {'users': users})

def ClassDetails(request):
        return render(request, 'classroom/GetClassDetails.html')

def GetClassDetailsToMark(request):
        return render(request, 'classroom/ClassDetailsToMark.html')

def MarkAttendance(request):
        now = timezone.now()
        users = User.objects.all()
        return render(request, 'classroom/MarkAttendance.html', {'users': users})

def AllStudents(request):
        now = timezone.now()
        users = User.objects.all()
        return render(request, 'classroom/AllStudentDetails.html', {'users': users})


def IndividualStudent(request):
        now = timezone.now()
        users = User.objects.all()
        return render(request, 'classroom/IndividualStudentDetails.html', {'users': users})
