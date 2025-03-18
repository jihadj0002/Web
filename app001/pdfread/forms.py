from django import forms
from .models import Books

class PDFform(forms.ModelForm):
    class Meta:
        model = Books
        fields = ['title', 'description', 'pdf', 'reading']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter book title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter book description'}),
            'pdf': forms.FileInput(attrs={'class': 'form-control'}),
            'reading': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter reading status'}),
        }