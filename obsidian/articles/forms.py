import httplib2
import mimetypes

from django import forms
from articles.models import Article


VALID_IMAGE_EXTENSION = [
    ".jpg",
    ".jpeg",
    ".png",
    ".gif",
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


class ArticleForm(forms.Form):
    # class Meta:
    #     model = Article
    #     exclude = ()
        # exclude = ('slug', 'author')

    def __init__(self, *args, **kwargs):
        # self.author = kwargs.pop("author")
        super(ArticleForm, self).__init__(*args, **kwargs)

    article_title = forms.CharField(max_length=100, required=True)
    article_cover = forms.URLField(required=True)
    article_descr = forms.CharField(required=False)
    article_body = forms.CharField()
    article_tags = forms.CharField(required=False)
