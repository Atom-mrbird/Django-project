from django.shortcuts import render
from .models import Joke, Ips
import requests

def starting_page(request):
	return render(request,"index.html")

def joke_page(request):
	return render(request, "jokes.html")

def create_page(request):
	responses = requests.get('https://api.yomomma.info/')
	tasks = responses.json()
	my_jokes = tasks
	rand_jokes = my_jokes['joke']
	c = Joke(joke=rand_jokes)
	c.save()

	response = requests.get('https://api.ipify.org?format=json')
	task = response.json()
	my_ip = task['ip']
	to_db = {'title':'ip', 'ip': my_ip}
	Ips.objects.create(**to_db)

	return render(request, "create.html")