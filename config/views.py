from django.views.generic import CreateView, ListView

from djraft.stories.models import Story


class Home(ListView):

    model = Story
    template_name = "pages/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["uncover"] = Story.objects.only_uncover_article()
        context["object_list"] = self.get_queryset().exclude(cover='');
        return context



landing_home_view = Home.as_view()

