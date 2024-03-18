from django.shortcuts import render
from listings.models import Band
from listings.models import Article
from listings.forms import BandForm, ArticleForm, ContactUsForm
from django.core.mail import send_mail
from django.shortcuts import redirect


def band_list(request):
    bands = Band.objects.all()
    return render(request,
                  'listings/band_list.html',
                  {'bands': bands})


def band_create(request):
    if request.method == 'POST':
        form = BandForm(request.POST)
        if form.is_valid():
            # créer une nouvelle « Band » et la sauvegarder dans la db
            band = form.save()
            # redirige vers la page de détail du groupe que nous venons de créer
            # nous pouvons fournir les arguments du motif url comme arguments à la fonction de redirection
            return redirect('band-detail', band.id)

    else:
        form = BandForm()

    return render(request,
                  'listings/band_create.html',
                  {'form': form})


def band_detail(request, id):
    band = Band.objects.get(id=id)
    return render(request,
                  'listings/band_detail.html',
                  {'band': band})


def about(request):
    return render(request, 'listings/about.html')


def article_create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            # créer une nouvelle « Band » et la sauvegarder dans la db
            article = form.save()
            # redirige vers la page de détail du groupe que nous venons de créer
            # nous pouvons fournir les arguments du motif url comme arguments à la fonction de redirection
            return redirect('article-detail', article.id)

    else:
        form = ArticleForm()

    return render(request,
                  'listings/article_create.html',
                  {'form': form})


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
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            send_mail(
                subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via MerchEx Contact Us form',
                message=form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list=['admin@merchex.xyz'],
            )
            #return redirect("email-envoye")
    else:
        form = ContactUsForm()
    return render(request,
                  'listings/contact.html',
                  {'form': form})
