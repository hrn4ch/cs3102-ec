from django import forms
from .models import Suggestion


class SuggestionForm(forms.ModelForm):
    name = forms.CharField
    suggestion = forms.CharField

    class Meta:
        model = Suggestion
        fields = ('suggestion',)
