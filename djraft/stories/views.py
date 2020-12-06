from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.views.generic import CreateView, ListView, DetailView
from django.urls import reverse

from rest_framework.permissions import BasePermission

from .models import Story
from .forms import StoryCreationForm


class StoryPermission(BasePermission):
    """
    Allow access to a given `Access` if the user is entitled to.
    """
    def has_permission(self, request):
        pass

    def has_object_permission(self, request, view, obj):
        pass


class StoryListView(LoginRequiredMixin, StoryPermission, ListView):

    model = Story
    template_name = "stories/articles_from_user.html"

    def get_queryset(self):
        """Show stories only to the user is entitled to."""

        self.queryset = Story.objects.filter(author=self.request.user)
        return self.queryset


story_list_view = StoryListView.as_view()


class StoryCreationView(LoginRequiredMixin, CreateView):

    model = Story
    template_name = "stories/article_form.html"
    fields = ['title', 'description', 'cover', 'body']

    def get_success_url(self):
        return reverse("users:detail", kwargs={"username": self.request.user.username})

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user

        return super().form_valid(form)


story_creation_view = StoryCreationView.as_view()
