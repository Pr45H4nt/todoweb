from django import forms
from .models import ListModel , Tasks

class ListForm(forms.ModelForm):
    class Meta:
        model = ListModel
        fields = "__all__"

class Tasks(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ('__all__')