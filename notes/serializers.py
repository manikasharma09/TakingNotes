from rest_framework import serializers
from .models import Notes
from django.contrib.auth.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model=User

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('username','password')		

class NotesSerializers(serializers.ModelSerializer):
	class Meta:
		model=Notes
		fields=('id','description','title')


