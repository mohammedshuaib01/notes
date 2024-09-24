from django import forms
from notesapp.models import Notes

class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ["title"]

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',  # Ensure this matches your CSS if used
                'placeholder': 'Enter Notes'  # Optional placeholder for better UX
            }),
        }