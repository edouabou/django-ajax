from django.shortcuts import render
from .models import Profile

def viewdata(request):
    return render(request,'ajson/index.html')

def getdata(request):
    profiles = Profile.objects.all()
    context = {'profiles':profiles}
    return render(request,'ajson/index.html',context)
