from django.shortcuts import render
from django.http import HttpResponse
from .models import Book

def index(request):
	context =  {
		"name": "Sebastin Santy",
		"bitsId": "2015A8PS0357G"
	}
	return render(request, "home.html", context)

def name(request, name):
	context =  {
		"name": name,
		"bitsId": "2015A8PS0357G"
	}
	return render(request, "home.html", context)

def allbooks(request):
	books = Book.objects.all()
	context = {
		"book": books
	}
	return render(request, "books.html", context)