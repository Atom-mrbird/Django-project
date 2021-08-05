from django.middleware.csrf import get_token
from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.decorators import action

from .models import Joke, Ips
import requests
from rest_framework.views import APIView
from .serializers import JokeSerializer
from rest_framework.response import Response

def starting_page(request):
	return render(request,"index.html")

def joke_page(request):
	return render(request, "jokes.html")

def create_page(request):
	responses = requests.get('https://api.yomomma.info')
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
	if c.save or Ips.objects.create(**to_db) == True:
		return render(request,"index.html")
		return render(request, "create.html")

def connect_api(request):
	response = requests.get('http://18.194.157.25:8000/apicalls')
	pic = response.json()
	context ={
		'name':pic
	}
	return render(request, "connect_api.html",context)

class NotFoundException (Exception):
    pass

class jokelist(APIView):

	def get_object(self,pk):
		qs = Joke.objects.filter(id=pk)
		if qs.count() == 1:
			return qs.first()
		return Joke.objects.filter(id=self.request.POST)

	def get(self, request):
		products = Joke.objects.all()
		serializer = JokeSerializer(products, many=True)
		return Response(serializer.data)

	def post(self, request):

		serializer = JokeSerializer(data=request.data)
		if (serializer.is_valid()):
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class JokeDetailView(APIView):

	@action(methods=['post'], detail=False)
	def post(self, request):
		url = {'api/id'}
		header = {'id': f'joke{get_token()}'}
		response = requests.get(url, headers=header)
		serializer = JokeSerializer(response)
		return Response(serializer.data)

	@action(methods=['delete'], detail=False)
	def delete(self):
		url = {'api/id'}
		header = {'id':f'joke{get_token()}'}
		response = requests.delete(url,headers=header)
		return Response(response.request,status=status.HTTP_204_NO_CONTENT)
