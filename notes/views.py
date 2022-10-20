from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import loader
# from .models import
from django.contrib.auth.forms import User
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required


def index(request):
    template = loader.get_template('index.html')
    context = {}
    return HttpResponse(template.render(context, request))


