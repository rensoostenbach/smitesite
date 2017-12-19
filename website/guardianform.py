from django import forms
from .models import GuardianBuild

class GuardianForm(forms.ModelForm):

    class Meta:
        model = GuardianBuild
        fields = ('title', 'text')
