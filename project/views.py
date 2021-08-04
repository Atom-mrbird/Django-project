from django.http import HttpResponseRedirect
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

class NotFoundException (Exception):
    pass

class jokelist(APIView):

	def get_object(self,pk):
		qs = Joke.objects.filter(joke=pk)
		if qs.count() == 1:
			return qs.first()
		return Joke.objects.filter(joke=self.request.POST)

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

	@action(methods=['delete'], detail=False)
	def delete(self, pk):
		todo = get_object_or_404(Joke, joke=pk)
		todo.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

class JokeDetailView(APIView):

	def get(self, request, pk):
		todo = get_object_or_404(Joke, joke=pk)
		serializer = JokeSerializer(todo)
		return Response(serializer.data)

	@action(methods=['delete'], detail=False)
	def delete(self, pk):
		todo = get_object_or_404(Joke, joke=pk)
		todo.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)
