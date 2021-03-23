from django import forms
from .models import Reviews


class ReviewsForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'type': 'text', 'id': 'name', 'class': 'form-control',
                                           'required': 'required'}),
            'email': forms.EmailInput(attrs={'type': 'email', 'id': 'email', 'class': 'form-control',
                                             'required': 'required'}),
            'message': forms.Textarea(attrs={'name': 'message', 'id': 'message', 'class': 'form-control',
                                             'rows': '4', 'required': 'required'})
        }
