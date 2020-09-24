from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.shortcuts import render
from django.views.generic import DetailView, RedirectView, UpdateView, ListView

from articles.models import Article

User = get_user_model()


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    slug_field = "username"
    slug_url_kwarg = "username"

    def get_context_data(self, **kwargs):
        context = {}
        if self.object:
            context["object"] = self.object
            context["stories"] = Article.objects.filter(author=self.request.user.id)
            context_object_name = self.get_context_object_name(self.object)
            if context_object_name:
                context[context_object_name] = self.object
        context.update(kwargs)
        return super().get_context_data(**context)


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    fields = ["name", "image"]

    def get_success_url(self):
        return reverse("users:detail", kwargs={"username": self.request.user.username})

    def get_object(self):
        return User.objects.get(username=self.request.user.username)

    def form_valid(self, form):
        messages.add_message(
            self.request, messages.INFO, _("Infos successfully updated")
        )
        return super().form_valid(form)


class UserRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse("users:detail", kwargs={"username": self.request.user.username})


class UserStoryDetailView(DetailView):
    model = Article


class UserStoriesView(ListView):
    model = User
    slug_field = "username"
    template_name_suffix = "_stories"

    def get_context_data(self, **kwargs):
        stories = Article.objects.filter(author=self.request.user.id)
        contexts = {"stories": stories}
        return contexts


user_detail_view = UserDetailView.as_view()
user_update_view = UserUpdateView.as_view()
user_redirect_view = UserRedirectView.as_view()
user_story_view = UserStoryDetailView.as_view()
user_stories_view = UserStoriesView.as_view()