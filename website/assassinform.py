from django import forms
from .models import AssassinBuild

class AssassinForm(forms.ModelForm):

    class Meta:
        model = AssassinBuild
        fields = ('title', 'text')
