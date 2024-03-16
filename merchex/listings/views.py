from django.shortcuts import render
from listings.models import Band
from listings.models import Article
from listings.models import Contact


def band_list(request):
    bands = Band.objects.all()
    return render(request,
                  'listings/band_list.html',
                  {'bands': bands})


def band_detail(request, id):
    band = Band.objects.get(id=id)
    return render(request,
                  'listings/band_detail.html',
                  {'band': band})


def about(request):
    return render(request, 'listings/about.html')


def article_list(request):
    articles = Article.objects.all()
    return render(request,
                  'listings/article_list.html',
                  {'articles': articles})


def article_detail(request, id):
    article = Article.objects.get(id=id)
    return render(request,
                  'listings/article_detail.html',
                  {'article': article})


def contact(request):
    contacts = Contact.objects.all()
    return render(request,
                  'listings/contact.html',
                  {'contacts': contacts})
