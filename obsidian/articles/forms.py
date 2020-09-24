import httplib2
import mimetypes

from django import forms
from articles.models import Article


VALID_IMAGE_EXTENSION = [
    ".jpg",
    ".jpeg",
    ".png",
]

VALID_MIME_TYPE = [
    "image",
]


def valid_url_extension(url, extension_list=VALID_IMAGE_EXTENSION):
    return any([url.endswith(e) for e in extension_list])


def valid_mime_type(url, mimetype_list=VALID_MIME_TYPE):
    mimetype, encoding = mimetypes.guess_type(url)
    if mimetype:
        return any([mimetype.startswith(m) for m in mimetype_list])
    else:
        return False


def image_exists(domain, path):
    try:
        conn = httplib2.HTTPConnection(domain)
        conn.requesst("HEAD", path)
        response = conn.getresponse()
        conn.close()
    except:
        return False

    return response.status == 200


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        exclude = ("slug", "author", "cover_2", "cover")

    def __init__(self, *args, **kwargs):
        super(ArticleForm, self).__init__(*args, **kwargs)

    title = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder": "There Is No Utopia",
                "autofocus": "off",
                "class": "appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline",
            }
        ),
    )
    imgcover = forms.ImageField(
        required=True,
        help_text="Your article image cover",
        widget=forms.FileInput(),
    )
    description = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline",
            }
        ),
    )
    body = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline",
            }
        ),
    )
    tags = forms.CharField(required=False)
