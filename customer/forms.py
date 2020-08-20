from django.forms import ModelForm
from .models import CustomerProfile


class ProfileForm(ModelForm):
    class Meta:
        model = CustomerProfile
        fields = ['phone', 'gender']
        labels = {
            'phone': 'شماره تلفن',
            'gender': 'جنسیت'
        }
