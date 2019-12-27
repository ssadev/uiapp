from django.shortcuts import render, HttpResponse
from .models import blogs
# Create your views here.


def index(requests):
	data = blogs.objects.all()
	# print(data)
	return render(requests, 'index.html', {'blogs': data})