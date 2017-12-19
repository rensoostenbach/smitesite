from django import forms
from .models import WarriorBuild

class WarriorForm(forms.ModelForm):

    class Meta:
        model = WarriorBuild
        fields = ('title', 'text')
