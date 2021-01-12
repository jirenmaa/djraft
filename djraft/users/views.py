from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView, RedirectView, UpdateView

from djraft.stories.models import Story

User = get_user_model()


class UserDetailView(LoginRequiredMixin, DetailView):

    model = User
    slug_field = "username"
    slug_url_kwarg = "username"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["stories"] = Story.objects.filter(author__username=self.kwargs["username"])

        return context


user_detail_view = UserDetailView.as_view()


class UserSettingsView(LoginRequiredMixin, UpdateView):

    model = User
    fields = ["username", "bio", "avatar"]
    template_name = "users/user_settings.html"

    def get_success_url(self):
        return reverse("users:detail", kwargs={"username": self.request.user.username})

    def get_object(self):
        return User.objects.get(username=self.request.user.username)

    def form_valid(self, form):
        # messages.add_message(
        #     self.request, messages.INFO, _("Infos successfully updated")
        # )
        return super().form_valid(form)


user_settings_view = UserSettingsView.as_view()


class UserRedirectView(LoginRequiredMixin, RedirectView):

    permanent = False

    def get_redirect_url(self):
        return reverse("users:detail", kwargs={"username": self.request.user.username})


user_redirect_view = UserRedirectView.as_view()


class UserStoryDetailView(DetailView):

    model = Story
    template_name = "stories/article_detail.html"


user_story_detail_view = UserStoryDetailView.as_view()
