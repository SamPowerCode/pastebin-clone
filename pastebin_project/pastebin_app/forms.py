from django import forms
from .models import Paste, Language

class PasteForm(forms.ModelForm):
    language = forms.ModelChoiceField(queryset=Language.objects.all())

    class Meta:
        model = Paste
        fields = ['title', 'content', 'language']
