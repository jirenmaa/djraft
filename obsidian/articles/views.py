from django.shortcuts import render
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, View

from PIL import Image

from articles.models import Article
from articles.forms import ArticleForm
from articles import firebase


class ArticleLists(ListView):
    model = Article

    def get_context_data(self, **kwargs):
        articles = Article.objects.all()
        contexts = {"articles": articles}
        return contexts


class ArticleCreate(LoginRequiredMixin, CreateView):
    success_url = "/articles"
    template_name = "articles/article_form.html"
    form_class = ArticleForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        # print(form.cleaned_data['imgcover'], type(form.cleaned_data['imgcover']))
        self.object.author = self.request.user
        self.object.cover = firebase.firebase_image_url(form.cleaned_data['imgcover'])
        return super().form_valid(form)


articles_list_view = ArticleLists.as_view()
articles_create_view = ArticleCreate.as_view()
