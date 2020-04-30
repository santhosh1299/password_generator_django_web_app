from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.
def home(request):
    return(render(request,'generator/home.html'))
def password(request):

    characters=list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('number'):
        characters.extend(list('123456789'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()_+'))
    thepassword=""
    length=request.GET.get('length',11)
    for x in range(int(length)):
        thepassword+=random.choice(characters)
    return(render(request,'generator/password.html',{'password':thepassword}))

def about(request):
    return(render(request,'generator/about.html'))
    ##hey
