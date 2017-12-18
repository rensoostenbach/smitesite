from django import forms
from .models import HunterBuild

class HunterForm(forms.ModelForm):

    class Meta:
        model = HunterBuild
        fields = ('title', 'text')
