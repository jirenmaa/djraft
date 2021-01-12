import requests
from django.core.files.base import ContentFile


def get_default_avatar(uname: str):
    image_url  = f"https://ui-avatars.com/api/?name={uname}&background=random&font-size=0.33&format=svg"
    image_name = f"{uname}.svg"

    response = requests.get(image_url)
    if response.status_code == 200:
        return image_name, ContentFile(response.content)
