from django import forms
from django.forms import ModelForm
from . import models
from .models import Center,Registrations,District


class DonorRegistration(ModelForm):
    class Meta:
        model = models.Registrations
        fields = '__all__'
        widgets = {'name': forms.TextInput(
            attrs={'class': 'form-control', 'required': 'True', 'placeholder': 'Enter Your Name'}),
            'gender': forms.Select(
            attrs={'class': 'form-control', 'required': 'True'}),
            'age': forms.TextInput(
            attrs={'class': 'form-control', 'required': 'True', 'placeholder': 'Enter Your age'}),
            'email': forms.EmailInput(
            attrs={'class': 'form-control', 'required': 'True', 'placeholder': 'Enter Your E-mail'}),
            'address': forms.Textarea(
             attrs={'class': 'form-control', 'required': 'True', 'placeholder': 'Enter Your Home Address'}),
            'district': forms.Select(
            attrs={'class': 'form-control', 'required':'True',}),
            'center': forms.Select(
            attrs={'class': 'form-control', 'required': 'True',}),
            'blood_group': forms.Select(
            attrs={'class': 'form-control', 'required': 'True'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['center'].queryset =Center.objects.none()

        if 'district' in self.data:
            try:
                district_id = int(self.data.get('district'))
                self.fields['center'].queryset = Center.objects.filter(district_id=district_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['center'].queryset = self.instance.district.center_set.order_by('name')


