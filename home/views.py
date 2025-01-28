from django.http import HttpResponse
from django.shortcuts import render, redirect
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.

from .models import *

@login_required(login_url='/login/')
def index(request):
  return render(request, 'index.html')


def google_login(request):
  return render(request, 'login.html')


def logout_view(request):
  logout(request)
  return redirect('/login')