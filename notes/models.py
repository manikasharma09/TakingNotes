from django.db import models
from django.contrib.auth.models import User


class Notes(models.Model):
	#owner=models.ForeignKey(User,on_delete=models.CASCADE)
	title=models.CharField(max_length=100)
	description=models.CharField(max_length=100)
	#updated=models.DateTimeField(auto_now_add=True)
	
	

	def __str__(self):
		return self.title