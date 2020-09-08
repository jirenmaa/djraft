from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, View


class ArticleLists(LoginRequiredMixin, ListView):
    template_name = "articles/index.html"

    def get(self, request):
        context = {"data": "yes"}

        return render(request, self.template_name, context)

articles_view = ArticleLists.as_view()