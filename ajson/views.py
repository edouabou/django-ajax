from django.shortcuts import render, redirect,HttpResponse
from .models import Profile
from django.http import JsonResponse

def viewdata(request):
    return render(request,'ajson/index.html')

def getdata(request):
    profiles = Profile.objects.all()
    context = {"profiles":list(profiles.values())}
    return JsonResponse(context)

def create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        about = request.POST.get('about')
        data = Profile(name=name,email=email,about=about)
        data.save()
        return HttpResponse("données sauvegardées")
    
    return render(request,'ajson/form.html')