from django.shortcuts import render
from . models import User

# Create your views here.
def index(request):
    return render(request,"myapp/index.html", {})

def navbar(request):
    return render(request, "myapp/navbar.html", {})

def userreg(request):

    return render(request, "myapp/userreg.html", {})

def insertuser(request):
      vustudent = request.POST['tustudent']
      vutamil = request.POST['tutamil']
      vusocial = request.POST['tusocial']
      vumaths = request.POST['tumaths']
      vuenglish = request.POST['tuenglish']

      us = User(ustudent = vustudent, ustamil = vutamil, ussocial = vusocial, usmaths = vumaths ,usenglish = vuenglish)
      us.save()
      return render(request, 'myapp/userreg.html', {})