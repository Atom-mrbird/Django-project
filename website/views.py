from django.shortcuts import render

from .models import Content,Post
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
    responses = requests.get('https://api.yomomma.info/')
    tasks = responses.json()
    my_jokes = tasks
    rand_jokes = my_jokes['joke']
    c = Content(name=rand_jokes)
    c.save()
    response = requests.get('https://api.ipify.org?format=json')
    task = response.json()
    my_ip = task
    ip = my_ip['ip']
    b = Post(name=ip)
    b.save()
    return render(request, "create.html")

def create(request):
    print("hello")
    response = requests.get('https://api.ipify.org?format=json')
    task = response.json()
    my_ip = task
    ip = my_ip['ip']
    b = Post(name=ip)
    b.save()
    return render(request, "create.html")