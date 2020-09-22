from django.shortcuts import render
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, View

from articles.models import Article
from articles.forms import ArticleForm


class ArticleLists(ListView):
    model = Article

    def get_context_data(self, **kwargs):
        articles = Article.objects.all()
        contexts = {"articles": articles}
        return contexts


articles_list_view = ArticleLists.as_view()


class ArticleCreate(LoginRequiredMixin, CreateView):
    success_url = "/"
    template_name = "articles/article_form.html"
    form_class = ArticleForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()

        return reverse("articles:articles")


articles_create_view = ArticleCreate.as_view()
