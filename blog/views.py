# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from . import models
# Create your views here.

def index(request):

    articles = models.Article.objects.all()
    return render(request, 'blog/index.html', {'articles': articles})


def article_page(request, article_id):
    article = models.Article.objects.get(pk=article_id)
    return render(request, 'blog/articlepage.html', {'article': article})


def edit_page(request, article_id):
    if str(article_id) == '0':
        return render(request, 'blog/editpage.html')
    article = models.Article.objects.get(pk=article_id)
    return render(request, 'blog/editpage.html', {'article': article})


def edit_action(request):
    title = request.POST.get('title', 'TITLE')
    content = request.POST.get('content', 'CONTENT')
    articleid = request.POST.get('articleid', '0')

    if str(articleid) == '0':
        models.Article.objects.create(title=title,content=content)
    else:
         article = models.Article.objects.get(pk=articleid)
         article.title = title
         article.content = content
         article.save()
    articles = models.Article.objects.all()
    return render(request, 'blog/index.html', {'articles': articles})
