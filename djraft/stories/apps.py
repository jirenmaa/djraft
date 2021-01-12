from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class StoriesConfig(AppConfig):
    name = 'djraft.stories'
    verbose_name = _("Stories")

    def ready(self):
        import djraft.stories.signals
