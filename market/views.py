from django.shortcuts import render , HttpResponse ,redirect


# Create your views here.

def google(request):
    return render (request,'google.html' )
def Homenew(request):
    return render (request,'index.html' )
def computers(request):
    return render (request,'computers.html' )
def Router(request):
    return render (request,'Router.html' )
