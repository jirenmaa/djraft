from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView, RedirectView, UpdateView, ListView, CreateView

from stories.models import Story
from stories.forms import StoryForm

User = get_user_model()


class UserDetailView(LoginRequiredMixin, DetailView):

    model = User
    slug_field = "username"
    slug_url_kwarg = "username"


class UserInfoView(LoginRequiredMixin, UpdateView):

    model = User
    updated_username = ""
    fields = ["name", "username"]

    def get_success_url(self):
        return reverse("users:detail", kwargs={"username": updated_username})

    def get_object(self):
        return User.objects.get(username=self.request.user.username)

    def form_valid(self, form):
        global updated_username

        self.object = form.save(commit=False)
        updated_username = form.cleaned_data["username"]

        messages.add_message(
            self.request, messages.INFO, _("Infos successfully updated")
        )
        return super().form_valid(form)


class UserRedirectView(LoginRequiredMixin, RedirectView):

    permanent = False

    def get_redirect_url(self):
        return reverse("users:detail", kwargs={"username": self.request.user.username})


class UserStoriesView(LoginRequiredMixin, ListView):

    model = User
    slug_field = "username"
    template_name_suffix = "_stories"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        author = User.objects.get(pk=self.request.user.id)
        stories = Story.objects.filter(author=author)

        data['stories'] = stories
        return data


class UserNewStoryView(LoginRequiredMixin, CreateView):
    template_name = "stories/story_form.html"
    form_class = StoryForm

    def get_success_url(self):
        return reverse("users:detail", kwargs={"username": self.request.user.username})

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user

        return super().form_valid(form)


user_detail_view = UserDetailView.as_view()
user_info_view = UserInfoView.as_view()
user_redirect_view = UserRedirectView.as_view()
user_stories_view = UserStoriesView.as_view()
user_new_stories_view = UserNewStoryView.as_view()
