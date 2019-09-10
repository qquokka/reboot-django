from django.shortcuts import render, redirect
from .models import Articles

# Create your views here.
def index(request):
    context = {
        'articles': Articles.objects.all()
    }
    return render(request, 'articles/index.html', context)


def new(request):
    return render(request, 'articles/new.html')


def create(request):
    article = Articles()
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()
    return redirect(f'/articles/{article.pk}')


def detail(request, article_pk):
    context = {
        'article': Articles.objects.get(pk=article_pk)
    }
    return render(request, 'articles/detail.html', context)


def delete(request, article_pk):
    article = Articles.objects.get(pk=article_pk)
    article.delete()
    return redirect('/articles/')


def edit(request, article_pk):
    context = {
        'article': Articles.objects.get(pk=article_pk)
    }
    return render(request, 'articles/edit.html', context)


def update(request, article_pk):
    article = Articles.objects.get(pk=article_pk)
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()
    return redirect(f'/articles/{article.pk}/')