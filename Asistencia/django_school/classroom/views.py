
from django.shortcuts import render
from login.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout,authenticate,login
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response,redirect
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.urls import reverse_lazy
from login.forms import RegistrationForm
from django.views.generic import TemplateView,CreateView



@login_required
def GetClassDetails(request):
    model=MyModel
    form_class=DetailsForm
    return render_to_response(
    'GetClassDetails.html',
    { 'user': request.user ,'form':DetailsForm}
    )
