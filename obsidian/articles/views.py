from django.shortcuts import render
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, View

from articles.models import Article
from articles.forms import ArticleForm


class ArticleLists(LoginRequiredMixin, ListView):
    model = Article

    def get_context_data(self, **kwargs):
        articles = Article.objects.all()
        contexts = {"articles": articles}
        return contexts


articles_list_view = ArticleLists.as_view()


class ArticleCreate(LoginRequiredMixin, CreateView):
    model = Article
    fields = ('title', 'description')

    success_url = "/"
    # template_name = 'articles/article_form.html'
    # form_class = ArticleForm

    # def form_valid(self, form):
    #     self.object = form.save(commit=False)
    #     self.object.author = self.request.user
    #     self.object.save()

    #     return reverse("articles:articles")

    # def get(self, *args, **kwargs):
    #     form = ArticleForm(self.request.POST or None)

    # def post(self, *args, **kwargs):
    #     form = ArticleForm(self.request.POST or None)
    #     try:
    #         if form.is_valid():
    #             article = Article.objects.create(
    #                 title=form.cleaned_data.get("article_title"),
    #                 cover=form.cleaned_data.get("article_cover"),
    #                 description=form.cleaned_data.get("article_descr"),
    #                 body=form.cleaned_data.get("article_body"),
    #                 tags=form.cleaned_data.get("article_tags"),
    #             )
    #             eslug = article.save()
    #             return redirect(
    #                 "users:story",
    #                 kwargs={
    #                     "username": self.request.user.username,
    #                     "slug_article": eslug,
    #                 },
    #             )
    #     except Exception as ex:
    #         return ex


articles_create_view = ArticleCreate.as_view()
