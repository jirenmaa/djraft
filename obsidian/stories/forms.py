# import httplib2
import mimetypes

from django import forms
from .models import Story


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
        self.fields["title"].required = False
        self.fields["description"].required = False
        self.fields["cover"].required = False
        self.fields["body"].required = False


    title = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Title",
                "required": False,
                "autofocus": "off",
                "autocomplete": "off",
                "class": "appearance-none w-full h-full py-2 px-3 mb-4 text-gray-900 text-6xl leading-tight focus:outline-none",
            }
        ),
    )

    description = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "What is this about...",
                "class": "appearance-none w-full py-2 px-3 mb-4 text-gray-700 text-xl leading-tight focus:outline-none",
            }
        )
    )

    cover = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                "placeholder": "Media image",
                "class": "appearance-none py-2 px-3 mb-4 text-gray-700 leading-tight focus:outline-none",
            }
        )
    )

    body = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "placeholder": "Tell your story...",
                "onkeyup": "AutoGrowTextArea(this)",
                "style": "overflow:hidden",
                "class": "appearance-none w-full py-2 px-3 mb-4 text-gray-700 text-xl leading-tight focus:outline-none",
            }
        )
    )
