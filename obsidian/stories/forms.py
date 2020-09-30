# import httplib2
import mimetypes

from django import forms
from stories.models import Story


VALID_IMAGE_EXTENSION = [
    ".jpg",
    ".jpeg",
    ".png",
]

VALID_MIME_TYPE = [
    "image",
]


# def valid_url_extension(url, extension_list=VALID_IMAGE_EXTENSION):
#     return any([url.endswith(e) for e in extension_list])


# def valid_mime_type(url, mimetype_list=VALID_MIME_TYPE):
#     mimetype, encoding = mimetypes.guess_type(url)
#     if mimetype:
#         return any([mimetype.startswith(m) for m in mimetype_list])
#     else:
#         return False


# def image_exists(domain, path):
#     try:
#         conn = httplib2.HTTPConnection(domain)
#         conn.requesst("HEAD", path)
#         response = conn.getresponse()
#         conn.close()
#     except:
#         return False

#     return response.status == 200


class StoryForm(forms.ModelForm):
    class Meta:
        model = Story
        exclude = ("slug", "author")

    def __init__(self, *args, **kwargs):
        super(StoryForm, self).__init__(*args, **kwargs)
