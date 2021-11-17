from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(OrderCreateForm, self).__init__(*args, **kwargs)
        self.fields['buying_type'].choices = [('', 'Тип доставки'), ] + list(
            self.fields['buying_type'].choices)[1:]

    class Meta:
        model = Order
        fields = [
            'first_name',
            'last_name',
            'phone',
            'email',
            'address',
            'buying_type',
            'comment'
        ]
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control',
                                                 'placeholder': 'Имя',
                                                 'required': 'true'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control',
                                                'placeholder': 'Фамилия',
                                                'required': 'true'}),
            'phone': forms.TextInput(attrs={'class': 'form-control',
                                            'placeholder': 'Телефон',
                                            'id': 'phone-number',
                                            'required': 'true'}),
            'email': forms.EmailInput(attrs={'class': 'form-control',
                                             'placeholder': 'Email',
                                             'required': 'true'}),
            'address': forms.TextInput(attrs={'class': 'form-control',
                                              'placeholder': 'Адрес',
                                              'required': 'true'}),
            'buying_type': forms.Select(attrs={'class': 'form-control'}),
            'comment': forms.Textarea(attrs={'class': 'form-control',
                                             'id': 'message',
                                             'name': 'message',
                                             'placeholder': 'Комментарии к заказу',
                                             'rows': '2'})
        }
