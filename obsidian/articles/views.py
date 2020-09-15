from django.shortcuts import render
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, View

from articles.models import Article


class ArticleLists(LoginRequiredMixin, ListView):
    model = Article

    def get_context_data(self, **kwargs):
        articles = Article.objects.all()
        contexts = {
            "articles": articles
        }

        for i in articles:
            print(i.author.image)

        return contexts



articles_view = ArticleLists.as_view()