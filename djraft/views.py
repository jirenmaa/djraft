from django.views.generic import ListView
from django.conf import settings

from djraft.stories.models import Story


class Home(ListView):

    model = Story
    paginate_by = 10
    template_name = "pages/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["trendings"] = Story.objects.filter(likes__users__gte=1).distinct()[:4]
        return context


landing_home_view = Home.as_view()
