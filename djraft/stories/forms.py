from django import forms
from .models import Story

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
                "class": "appearance-none w-full h-full py-2 px-3 mb-4 text-gray-900 text-4xl leading-tight focus:outline-none",
            }
        ),
    )

    description = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "What is this about...",
                "class": "appearance-none w-full py-2 px-3 mb-4 text-gray-900 text-lg leading-tight focus:outline-none",
            }
        )
    )

    cover = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                "placeholder": "Media image",
                "class": "appearance-none py-2 px-3 mb-4 text-gray-900 leading-tight focus:outline-none",
            }
        )
    )

    body = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "placeholder": "Tell your story...",
                "onkeyup": "AutoGrowTextArea(this)",
                "style": "overflow:hidden",
                "class": "appearance-none w-full py-2 px-3 mb-4 text-gray-700 text-lg leading-tight focus:outline-none",
            }
        )
    )
