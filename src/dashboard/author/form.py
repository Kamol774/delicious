from django import forms
from now.delicious.src.front.models import Author


class AuthorsForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(attrs={'class': 'form-control'}),
        }