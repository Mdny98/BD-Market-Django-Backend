from rest_framework import serializers

from content.models import (Product, SubCategory, Brand, Attribute, Feedback,
    ProductAttr)
from accounts.models import Customer, User


class BrandSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'

class CatSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SubCategory
        fields = '__all__'

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

class CustomerSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Customer
        fields = '__all__'

