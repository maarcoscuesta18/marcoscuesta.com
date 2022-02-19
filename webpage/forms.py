from django import forms

from . import models

'''class ClientForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ClientForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['address'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['email'].widget.attrs = {
            'class': 'form-control col-md-6',
            'step': 'any',
            'min': '1',
        }
        self.fields['telephone'].widget.attrs = {
            'class': 'form-control col-md-6',
            'step': 'any',
            'min': '1',
        }

    class Meta:
        model = Client
        fields = ('name', 'address', 'email','telephone')
'''
class ContactForm(forms.ModelForm):
    class Meta:
        model = models.Contact
        fields = '__all__'
            
class PasswordGeneratorForm(forms.ModelForm):
    class Meta:
        model = models.Password
        fields = '__all__'
        widgets = {
            'length': forms.TextInput(attrs={'style': ' border-radius: 30px;'}),
            }