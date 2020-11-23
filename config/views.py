from django.shortcuts import render

from stories.models import Story


def home(request):
    if request.method == "GET":
        # filter articles only with cover image
        web_main_articles = Story.objects.get_excover_queryset()[:18]

        # filter article that doesn't have the cover image but have description
        web_explore_articles = Story.objects.exclude(
            cover__regex='.', description__isnull=False
        )
        # randomize explored articles
        list_explore_articles = []
        if web_explore_articles.exists() or web_main_articles.exists():
            for _ in range(4):
                list_explore_articles.append(Story.objects.random(web_explore_articles))
        else:
            list_explore_articles = web_explore_articles

        return render(
            request, "pages/home.html",
            context={
                "web_main_articles": web_main_articles,
                "web_explore_articles": web_explore_articles
            }
        )
