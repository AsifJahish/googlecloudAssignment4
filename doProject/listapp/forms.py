from django import forms
from .models import ListItem

class ListItemForm(forms.ModelForm):
    class Meta:
        model = ListItem
        fields = ['title', 'description', 'completed']
