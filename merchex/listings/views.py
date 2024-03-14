from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band


def hello(request):
    bands = Band.objects.all()
    return HttpResponse(f"""
        <h1>Hello Django!</h1>
        <p>Mes groupes préférés sont :</p>
        <ul>
            <li>{bands[0].name} - {bands[3].title}</li>
            <li>{bands[1].name} - {bands[4].title}</li>
            <li>{bands[2].name} - {bands[5].title}</li>
            <li>{bands[10].name} - {bands[9].title}</li>
        </ul>
    """)

def about(request):
    return HttpResponse('<h1>A propos</h1> <p>Nous adorons merch !</p>')

def listings(request):
    return HttpResponse("<h1>Listings</h1> <p>voici la liste d'annonce :</p>")

def contact(request):
    return HttpResponse('<h1>Contact</h1> <p>création de contact</p>')
