from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, render_to_response
from django.utils import timezone
import datetime
from classroom.models import User, Oncall
from django.template import RequestContext, loader
from django.template import Template, Context
from django.template.defaulttags import register

def index(request):
        now = timezone.now()
        users = User.objects.all()
        return render(request, 'classroom',{'users': users})

def getUsers(request):
        users = User.objects.all()
        name_list = []
        for x in users:
                name_list.append(x.first_name + ' ' + x.last_name)
        return name_list
