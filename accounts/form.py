from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db import transaction
from .models import User,Customer,Supplier

class CustomerSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)
    email = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User
    
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_customer = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.email = self.cleaned_data.get('email')
        
        user.save()
        customer = Customer.objects.create(user=user)
        customer.phone_number=self.cleaned_data.get('phone_number')
        # customer.gender=self.cleaned_data.get('gender')
        customer.save()
        return user

class SupplierSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)
    company_name = forms.CharField(required=True)
    email = forms.CharField(required=True)
    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_supplier = True
        user.is_staff = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.email = self.cleaned_data.get('email')
        user.save()
        supplier = Supplier.objects.create(user=user)
        supplier.phone_number=self.cleaned_data.get('phone_number')
        supplier.company_name=self.cleaned_data.get('company_name')
        supplier.save()
        return user
    

from django.contrib.auth.forms import UserCreationForm


class ProfileForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		user = kwargs.pop('user')

		super(ProfileForm, self).__init__(*args, **kwargs)

		self.fields['username'].help_text = None
		
		if not user.is_superuser:
			self.fields['username'].disabled = True
			

	class Meta:
		model = User
		fields = ['username', 'email', 'first_name', 'last_name',]

