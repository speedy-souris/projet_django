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


def band_update(request, id):
    band = Band.objects.get(id=id)
    if request.method == 'POST':
        form = BandForm(request.POST, instance=band)
        if form.is_valid():
            # mettre à jour le groupe existant dans la base de données
            form.save()
            # rediriger vers la page détaillée du groupe que nous venons de mettre à jour
            return redirect('band-detail', band.id)
    else:
        form = BandForm(instance=band)  # on pré-remplir le formulaire avec un groupe existant
    return render(request,
                  'listings/band_update.html',
                  {'form': form})


def band_delete(request, id):
    band = Band.objects.get(id=id)
    if request.method == 'POST':
        # supprimer le groupe de la base de données
        band.delete()
        # rediriger vers la liste des groupes
        return redirect('band-list')
    return render(request,
                  'listings/band_delete.html',
                  {'band': band})


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


def article_update(request, id):
    article = Article.objects.get(id=id)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            # mettre à jour le groupe existant dans la base de données
            form.save()
            # rediriger vers la page détaillée du groupe que nous venons de mettre à jour
            return redirect('article-detail', article.id)
    else:
        form = ArticleForm(instance=article)  # on pré-remplir le formulaire avec un groupe existant
    return render(request,
                  'listings/article_update.html',
                  {'form': form})





def article_list(request):
    articles = Article.objects.all()
    return render(request,
                  'listings/article_list.html',
                  {'articles': articles})


def article_delete(request, id):
    article = Article.objects.get(id=id)
    if request.method == 'POST':
        # supprimer le groupe de la base de données
        article.delete()
        # rediriger vers la liste des groupes
        return redirect('article-list')
    return render(request,
                  'listings/article_delete.html',
                  {'article': article})


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
