import requests
from django.core.files.base import ContentFile


def get_default_avatar(uname: str):
    im_urls = f"https://ui-avatars.com/api/?name={uname}&background=random&font-size=0.33&format=svg"
    im_name = f"{uname}.svg"

    response = requests.get(im_urls)
    if response.status_code == 200:
        return im_name, ContentFile(response.content)
