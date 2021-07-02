from django import forms
from now.delicious.src.front.models import Followers


class FollowersForm(forms.ModelForm):
    class Meta:
        model = Followers
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(attrs={'class': 'form-control'}),
        }