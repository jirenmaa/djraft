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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["stories"] = Story.objects.filter(author=self.request.user.id)
        return context


user_detail_view = UserDetailView.as_view()


class UserInfoView(LoginRequiredMixin, UpdateView):

    model = User
    fields = ["name", "username", "avatar"]

    def get_success_url(self):
        user = User.objects.get(id=self.request.user.id)
        return reverse("users:detail", kwargs={"username": user.username})

    def get_object(self):
        return User.objects.get(username=self.request.user.username)

    def form_valid(self, form):
        user = User.objects.get(id=self.request.user.id)
        if user.avatar:
            User.delete_old_avatar(user)    

        messages.add_message(
            self.request, messages.INFO, _("Info successfully updated")
        )
        return super().form_valid(form)


user_info_view = UserInfoView.as_view()


class UserRedirectView(LoginRequiredMixin, RedirectView):

    permanent = False

    def get_redirect_url(self):
        return reverse("users:detail", kwargs={"username": self.request.user.username})


user_redirect_view = UserRedirectView.as_view()


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


user_stories_view = UserStoriesView.as_view()


class UserStoryDetailView(DetailView):

    model = Story
    template_name_suffix = "_detail"


user_story_detail_view = UserStoryDetailView.as_view()


class UserNewStoryView(LoginRequiredMixin, CreateView):
    template_name = "stories/story_form.html"
    form_class = StoryForm

    def get_success_url(self):
        return reverse("users:detail", kwargs={"username": self.request.user.username})

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user

        return super().form_valid(form)


user_new_stories_view = UserNewStoryView.as_view()
