from django.shortcuts import render

from .models import Content
import requests

posts =[
    {
        'author': 'ataberk',
        'title': 'joke posts 1',
        'content': 'first post content',
        'date_posted': 'April 26, 2020'
    }
]

def starting_page(request):
    return render(request,"index.html")

def gallery(request):
    return render(request, "jokes.html")

def create_save_page(request):
    response = requests.get('https://api.ipify.org?format=json')
    task = response.json()
    my_ip =task
    ip = my_ip
    b = Content(name=ip)
    b.save()
    responses = requests.get('https://official-joke-api.appspot.com/random_joke')
    tasks = responses.json()
    my_jokes = tasks
    rand_jokes = my_jokes
    c = Content(name=rand_jokes)
    c.save()
    return render(request, "create.html")