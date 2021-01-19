from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, ListView, UpdateView
from django.urls import reverse
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from .models import Story


class StoryListView(LoginRequiredMixin, ListView):
    """Show stories only to the user is entitled to."""

    model = Story
    template_name = "stories/story_users.html"

    def get_queryset(self):
        """Show stories only to the user is entitled to."""

        self.queryset = Story.objects.filter(author=self.request.user)
        return self.queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["most_liked"] = (
            context["object_list"].filter(likes__users__gte=1).distinct()[:3]
        )
        return context


story_list_view = StoryListView.as_view()


class StoryCreationView(LoginRequiredMixin, CreateView):

    model = Story
    template_name = "stories/story_form.html"
    fields = ["title", "description", "cover", "body"]

    def get_success_url(self):
        return reverse("users:detail", kwargs={"username": self.request.user.username})

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user

        return super().form_valid(form)


story_creation_view = StoryCreationView.as_view()


class StoryUpdateView(LoginRequiredMixin, UpdateView):

    model = Story
    fields = ["title", "description", "cover", "body"]
    template_name = "stories/story_edit.html"

    def get_success_url(self):
        return reverse("me:stories")

    def form_valid(self, form):
        return super().form_valid(form)


story_update_view = StoryUpdateView.as_view()


@login_required
def story_delete_view(request, slug):
    story = get_object_or_404(Story, author=request.user, slug=slug)
    story.delete()

    return HttpResponse(status=204)


def like(request, _id):
    article = get_object_or_404(Story, id=_id)
    article.likes.users.add(request.user)
    return HttpResponse(status=204)


def dislike(request, _id):
    article = get_object_or_404(Story, id=_id)
    article.likes.users.remove(request.user)
    return HttpResponse(status=204)
