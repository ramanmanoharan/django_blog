from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from app.models import About
from app.models import Team
from app.models import Client
def index(request):
	key= About.objects.all()
	keys = Client.objects.all()
	# return HttpResponse("Hello World")
	return render(request, "index.html", {'data':key, 'clients':keys})

def about(request):
	key = Team.objects.all()
	return render(request, "about.html", {'data':key})

def portfolio(request):
	return render(request, "portfolio.html", {})

def contact(request):
	return render(request, "contact.html", {})