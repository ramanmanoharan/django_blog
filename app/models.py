from django.db import models

# Create your models here.
class App(models.Model):
	name= models.CharField(max_length=50)
	title= models.CharField(max_length=100)
	description= models.TextField()
	about= models.TextField()
	image= models.ImageField(upload_to='app/')


	def __str__(self):
		return str(self.id)


class Slider(models.Model):
	name= models.CharField(max_length=50)
	title= models.CharField(max_length=100)
	description= models.TextField()
	about= models.TextField()
	image= models.ImageField(upload_to='slider/')


	def __str__(self):
		return str(self.id)

class About(models.Model):
	title = models.CharField(max_length=100)
	shortdescription = models.CharField(max_length=100)
	description = models.TextField()
	image = models.ImageField(upload_to='aboutmedia/')

class Team(models.Model):
	title = models.CharField(max_length=100)
	designiation = models.CharField(max_length=100)
	email = models.EmailField()
	phone = models.CharField(max_length=12)
	description = models.TextField()
	image = models.ImageField(upload_to='media/aboutmedia')

class Client(models.Model):
	title = models.CharField(max_length=100)
	location = models.CharField(max_length=100)
	email = models.EmailField()
	phone = models.CharField(max_length=12)
	description = models.TextField()
	image = models.ImageField(upload_to='clients/')