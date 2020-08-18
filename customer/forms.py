from django.forms import ModelForm
from .models import CustomerProfile


class ProfileForm(ModelForm):
    pass
    # class Meta:
    #     model = CustomerProfile
    #     fields = ['phone_number', 'gender']
    #     labels = {
    #         'phone_number': 'شماره تلفن',
    #         'gender': 'جنسیت'
    #     }
