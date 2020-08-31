from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm
from django.db import transaction
from .models import User,Customer,Supplier
from Supplier.models import ProductSupplier
from content.models import Product

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


# class CreateStockForm(UserCreationForm):
#     "product_name"
#     "product_description"
#     "product_image"
# 	"subcategory_id"
#     "brand_id"
#     "attribute"
    
    
    
    
    
    
#     class Meta(UserCreationForm.Meta):
#         model = product


class ConfrimForm(ModelForm):
    # supplier_id = forms.CharField(required=True)
    # product_id = forms.CharField(required=True)
    # stock = forms.IntegerField(required=True)
    # unit_price = forms.FloatField(required=True)
    class Meta:
        model = ProductSupplier
        fields = ['product_id', 'unit_price', 'stock']
        


    # @transaction.atomic
    # def save(self):
    #     productSupplier = super().save(commit=False)
    #     productSupplier.supplier_id = self.cleaned_data.get()
    #     productSupplier.product_id = self.cleaned_data.get('product_id')
    #     productSupplier.stock = self.cleaned_data.get('stock')
    #     productSupplier.unit_price = self.cleaned_data.get('unit_price')


    #     productSupplier.save()
        
    #     return productSupplier