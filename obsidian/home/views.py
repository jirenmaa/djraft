from django.shortcuts import render
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from django.db.models.aggregates import Count

from random import randint

from articles.models import Article

class HomeView(View):
    def get_context_data(self, **kwargs):
        random_top_article = 5
        articles = [Article.objects.random() for _ in range(random_top_article)]
        return articles

    def get(self, *args, **kwargs):
        global template_name

        contexts = {"articles": self.get_context_data}
        return render(self.request, "pages/home.html", context=contexts)


home_view = HomeView.as_view()
