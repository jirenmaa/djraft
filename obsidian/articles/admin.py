from django.contrib import admin
from articles.models import (Article, Tag)

# Register your models here.
admin.site.register(Article)
admin.site.register(Tag)

