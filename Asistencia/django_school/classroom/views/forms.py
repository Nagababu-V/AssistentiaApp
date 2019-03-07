import re
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.forms import ModelForm
from  .models import MyModel


class DetailsForm(ModelForm):
	class Meta:
		model=MyModel
		fields=['year','department','section']
