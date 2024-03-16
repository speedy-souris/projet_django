from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class Band(models.Model):
    class Genre(models.TextChoices):
        HIP_HOP = 'HH'
        SYNTH_POP = 'SP'
        ALTERNATIVE_ROCK = 'AR'

    name = models.fields.CharField(max_length=100)
    genre = models.fields.CharField(choices=Genre.choices, max_length=5)
    biography = models.fields.CharField(max_length=1000)
    year_formed = models.fields.IntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(2024)]
    )
    active = models.fields.BooleanField(default=True)
    official_homepage = models.fields.URLField(null=True, blank=True)

    def __str__(self):
        return f'{self.name}'


class Article(models.Model):
    class Type(models.TextChoices):
        RECORD ="RE"
        CLOTHING = "CL"
        POSTER = "PO"
        MISCELLANEOUS = "MI"

    title = models.fields.CharField(max_length=100)
    date = models.fields.DateField()
    types = models.fields.CharField(choices=Type.choices, max_length=5)
    description = models.fields.CharField(max_length=1000)
    sold = models.fields.BooleanField(default=False)

class Contact(models.Model):
    first_name = models.fields.CharField(max_length=30)
    email = models.fields.EmailField()
