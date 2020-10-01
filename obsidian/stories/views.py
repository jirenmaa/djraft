from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from stories.models import Story

class ArticleList(LoginRequiredMixin, ListView):
    model = Story
