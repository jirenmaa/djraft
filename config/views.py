from django.shortcuts import render

from stories.models import Story


def home(request):
    if request.method == "GET":
        # web_main_articles = Story.objects.exclude(cover="")[:22]
        web_main_articles = Story.objects.random()
        print(type(web_main_articles), web_main_articles.description)
        web_explore_articles = Story.objects.exclude(
            cover__exact="", description__isnull=False
        )

        return render(
            request, "pages/home.html",
            context={
                "web_main_articles": web_main_articles,
                "web_explore_articles": web_explore_articles
            }
        )
