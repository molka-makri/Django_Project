from django import forms
from .models import Conference, Submission

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


class SubmissionForm(forms.ModelForm):
    class Meta:
        model = Submission
        fields = ['conference_id', 'title', 'abstract', 'keyword', 'paper']
        labels = {
            'conference_id': 'Conférence',
            'title': 'Titre de la soumission',
            'abstract': 'Résumé',
            'keyword': 'Mots-clés',
            'paper': 'Fichier PDF',
        }
        widgets = {
            'conference_id': forms.Select(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'placeholder': 'Titre de votre soumission', 'class': 'form-control'}),
            'abstract': forms.Textarea(attrs={'placeholder': 'Résumé de votre article...', 'rows': 5, 'class': 'form-control'}),
            'keyword': forms.TextInput(attrs={'placeholder': 'mot1, mot2, mot3...', 'class': 'form-control'}),
            'paper': forms.FileInput(attrs={'class': 'form-control', 'accept': '.pdf'}),
        }
        help_texts = {
            'keyword': 'Séparez les mots-clés par des virgules (maximum 10)',
            'paper': 'Seuls les fichiers PDF sont acceptés',
        }


class SubmissionUpdateForm(forms.ModelForm):
    """Formulaire pour la modification d'une soumission (sans conférence)"""
    
    class Meta:
        model = Submission
        fields = ['title', 'abstract', 'keyword', 'paper']  # Pas de conference_id pour la modification
        labels = {
            'title': 'Titre de la soumission',
            'abstract': 'Résumé',
            'keyword': 'Mots-clés', 
            'paper': 'Fichier PDF (optionnel)',
        }
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Titre de votre soumission', 
                'class': 'form-control'
            }),
            'abstract': forms.Textarea(attrs={
                'placeholder': 'Résumé de votre article...', 
                'rows': 5, 
                'class': 'form-control'
            }),
            'keyword': forms.TextInput(attrs={
                'placeholder': 'mot1, mot2, mot3...', 
                'class': 'form-control'
            }),
            'paper': forms.FileInput(attrs={
                'class': 'form-control', 
                'accept': '.pdf'
            }),
        }
        help_texts = {
            'title': 'Vous pouvez modifier le titre de votre soumission',
            'abstract': 'Mettez à jour le résumé de votre article',
            'keyword': 'Séparez les mots-clés par des virgules (maximum 10)',
            'paper': 'Téléchargez un nouveau fichier PDF ou laissez vide pour garder l\'actuel',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Rendre le champ paper optionnel pour la modification
        self.fields['paper'].required = False
