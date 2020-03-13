from django.db import models

# Create your models here.
class Products(models.Model):
	title = models.TextField()
	description = models.TextField()
	timeLength = models.TextField()
	summary = models.TextField("Hi cool")