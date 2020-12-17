from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import DetailView, UpdateView
from django.shortcuts import HttpResponseRedirect, get_object_or_404

from django.core.exceptions import PermissionDenied
from django.utils.translation import gettext_lazy as _
from django.urls import reverse

from djraft.stories.models import Story

User = get_user_model()


class UserDetailView(LoginRequiredMixin, DetailView):

    model = User
    slug_field = "username"
    slug_url_kwarg = "username"

    def get_object(self, *args, **kwargs):
        if self.request.user.username != self.kwargs["username"]:
            obj = get_object_or_404(User, username=self.kwargs["username"])
            return obj

        super().get_object(*args, **kwargs)

    def get_context_data(self, **kwargs):
        user = get_object_or_404(User, username=self.kwargs["username"])
        context = super().get_context_data(**kwargs)
        context["stories"] = Story.objects.filter(author=user)

        return context


user_detail_view = UserDetailView.as_view()


class UserUpdateView(LoginRequiredMixin, UpdateView):

    model = User
    fields = ["name"]

    def get_success_url(self):
        return reverse("users:detail", kwargs={"username": self.request.user.username})

    def get_object(self):
        return User.objects.get(username=self.request.user.username)

    def form_valid(self, form):
        messages.add_message(
            self.request, messages.INFO, _("Infos successfully updated")
        )
        return super().form_valid(form)


user_update_view = UserUpdateView.as_view()


# user related story or article

class UserStoryDetailView(DetailView):

    model = Story
    template_name = "stories/article_detail.html"


user_story_detail_view = UserStoryDetailView.as_view()


@login_required
def user_story_delete(request, username, slug):
    if request.user.username == username:
        story = get_object_or_404(Story, author=request.user, slug=slug)

        story.delete()
        url = reverse("me:stories")
        return HttpResponseRedirect(url)
    raise PermissionDenied()
