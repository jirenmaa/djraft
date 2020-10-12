from django.http import request
from django.shortcuts import render

from stories.models import Story


def home(request):
    if request.method == "GET":
        articles = Story.objects.all()
        return render(request, "pages/home.html", context={"articles": articles})
