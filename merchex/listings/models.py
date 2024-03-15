from django.db import models

# Create your models here.
class Band(models.Model):
    name = models.fields.CharField(max_length=100)
    title = models.fields.CharField(max_length=100)

class Article(models.Model):
    title = models.fields.CharField(max_length=100)
    date = models.fields.DateField()

class Contact(models.Model):
    first_name = models.fields.CharField(max_length=30)
    email = models.fields.EmailField()
