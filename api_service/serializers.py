from rest_framework import serializers

from content.models import Product, SubCategory, Brand


class BrandSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


class CatSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SubCategory
        fields = '__all__'

class ProductSerializer(serializers.HyperlinkedModelSerializer):
# class ProductSerializer(serializers.ModelSerializer):

    # subcategory_id = serializers.RelatedField(source='category', read_only=True)
    # brand_id = serializers.RelatedField(source='brand', read_only=True)
    # attribute = serializers.RelatedField(source='attribute', read_only=True)

    class Meta:
        model = Product
        # fields = '__all__'
        fields = ['product_name', 'product_description', 'product_image', 'subcategory_id', 'brand_id']
        
        # subcategory_id = CatSerializer(many=True)
