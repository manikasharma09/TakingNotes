from rest_framework import generics
from . import serializers
from .models import Notes
from datetime import datetime
from django.shortcuts import render
from django.contrib.auth.models import User
# REST Framework
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
# Provider OAuth2
from coreapi import Client
# notes App
from .serializers import RegistrationSerializer
from .serializers import UserSerializer, NotesSerializers
from .models import *


class NoteList(generics.ListCreateAPIView):
	queryset=Notes.objects.all()
	serializer_class=serializers.NotesSerializers

class NoteLists(generics.RetrieveUpdateDestroyAPIView):
	queryset=Notes.objects.all()
	serializer_class=serializers.NotesSerializers

class RegistrationView(APIView):
	permission_classes=()
	def post(self,request):
		serializer=RegistrationSerializer(data=request.data)
		if serializer.is_valid():
			data=serializer.data
			u=User.objects.create(username=data['username'])
			u.set_password(data['password'])
			u.save()
			name = u.username
			client = Client(user=u, name=name, url='' + name,\
            	client_id=name, client_secret='', client_type=1)
			client.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
