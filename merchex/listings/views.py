from django.shortcuts import render
from listings.models import Band
from listings.models import Article
from listings.models import Contact


def hello(request):
    bands = Band.objects.all()
    return render(request, 
    'listings/hello.html',
    {'bands': bands})

def about(request):
    return render(request, 'listings/about.html')

def listings(request):
    articles = Article.objects.all()
    return render(request,
    'listings/listings.html',
    {'articles': articles})

def contact(request):
    contacts = Contact.objects.all()
    return render(request,
    'listings/contact.html',
    {'contacts': contacts})
