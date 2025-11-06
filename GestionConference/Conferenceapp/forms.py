from django import forms
from .models import Conference

class ConferenceForm(forms.ModelForm):
    class Meta:
        model = Conference
        fields = ['name', 'theme', 'description', 'location', 'start_date', 'end_date']
        labels = {
            'name': 'Nom de la conférence',
            'theme': 'Thème',
            'description': 'Description',
            'location': 'Lieu de la conférence',
            'start_date': 'Date de début',
            'end_date': 'Date de fin',
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Nom de la conférence'}),
            'theme': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'placeholder': 'Description', 'rows': 4}),
            'location': forms.TextInput(attrs={'placeholder': 'Lieu de la conférence'}),
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }
