from django.views.generic import ListView

from djraft.stories.models import Story


class Home(ListView):

    model = Story
    template_name = "pages/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["trendings"] = (
            context["object_list"].filter(likes__users__gte=3).distinct()[:4]
        )
        return context


landing_home_view = Home.as_view()
