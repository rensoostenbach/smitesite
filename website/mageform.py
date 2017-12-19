from django import forms
from .models import MageBuild

class MageForm(forms.ModelForm):

    class Meta:
        model = MageBuild
        fields = ('title', 'text')
