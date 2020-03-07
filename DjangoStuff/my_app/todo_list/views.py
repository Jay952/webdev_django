from django.shortcuts import render

def home(request):
	return render(request, 'home.html',{}),

def Jay(request):

    return render(request, 'about.html',{})


