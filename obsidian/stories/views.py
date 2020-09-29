from django.shortcuts import render
from django.view.generic import ListView

from stories.models import Story

class ArticleList(ListView):
    model = Story
