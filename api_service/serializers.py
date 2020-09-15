from rest_framework import serializers

from content.models import (Product, SubCategory, Brand, Attribute, Feedback,
    ProductAttr)
from accounts.models import Customer, User, Supplier
from Supplier.models import ProductSupplier
from customer.models import CustomerAddress
from cart.models import Cart, OrderItem

class BrandSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'

class CatSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SubCategory
        fields = '__all__'
# class CatDetailSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = SubCategory
#         fields = '__all__'

# class CatListSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = SubCategory
#         fields = '__all__'
class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        
class AttributeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Attribute
        fields = '__all__'

class FeedbackSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Feedback
        fields = '__all__'

class ProductAttrSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = ProductAttr
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = '__all__'
        read_only_fields  = ('username', 'email')

class CustomerAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerAddress
        fields = '__all__'
        read_only_fields  = ('customer_id',)

class CustomerSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    # address = serializers.HyperlinkedRelatedField(view_name='customeraddress-detail',
    #                                     many=True, queryset=CustomerAddress.objects.all())
    address = CustomerAddressSerializer(many=True)
    class Meta:
        model = Customer
        fields = ['address', 'phone_number', 'user', 'city']

class SupplierSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Supplier
        fields = '__all__'

class ProductSupplierSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = ProductSupplier
        fields = '__all__'


class OrderItemSerializer(serializers.ModelSerializer):
    cart_id = serializers.CharField(max_length=50, required=False)
    class Meta:
        model = OrderItem
        fields = '__all__'
        # extra_kwargs = {'cart_id': {'required': False}}
        # validators = []
        # read_only_fields  = ('cart_id',)


class CartSerializer(serializers.HyperlinkedModelSerializer):
    order = OrderItemSerializer(many=True)
    class Meta:
        model = Cart
        fields = ['url', 'customer_id', 'total_price', 'status', 'adresses', 'order']

class AddToCartSerializer(serializers.ModelSerializer):
    # product_supplier_id = serializers.CharField(max_length=100, required=True, help_text="please write only one color")
    
    class Meta:
        model = OrderItem
        fields = ('product_supplier_id',)