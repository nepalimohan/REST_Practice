from rest_framework import serializers

from product.models import Category, Product

#if in models blank=True here it will be allow_blank=True
#also required=False for blank and null True

# class CategorySerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     category = serializers.CharField(max_length=100, allow_blank=True)
#     parent = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), required=False, read_only=False)
    
#     def create(self, validated_data):
#         return Category.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         """
#         Update and return an existing `Snippet` instance, given the validated data.
#         """
#         instance.category = validated_data.get('category', instance.category)
#         if instance.parent is not None:
#             print('abc')
#             instance.parent = validated_data.get('parent', instance.parent)
#         instance.save()
#         return instance

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
    
    # def update(self, instance, validated_data):
    #     subcategories_data = validated_data.pop('subcategory', None)
    #     for key, value in validated_data.items():
    #         setattr(instance, key, value)
    #     instance.save()
    #     if subcategories_data:
    #         for subcategory_data in subcategories_data:
    #             if 'id' in subcategory_data:
    #                 subcategory = Category.objects.get(id=subcategory_data['id'])
    #                 Category.objects.filter(id=subcategory_data['id']).update(**subcategory_data)
    #             else:
    #                 Category.objects.create(parent=instance, **subcategory_data)
    #     return instance
    
    
    
class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=200)
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    price = serializers.DecimalField(max_digits=8, decimal_places=2)
    color = serializers.ChoiceField(choices=(
        ('Blue', 'Blue'),
        ('Black', 'Black'),
        ('Green', 'Green'),
        ('White', 'White'),
    ))
    
    stock = serializers.IntegerField()
    # image = serializers.FileField()
    description = serializers.CharField(max_length=255)
    
    def create(self, validated_data):
        return Product.objects.create(**validated_data)
    
    
    
    
    
#using model serializer for category
# class CategorySerializer(serializers.ModelSerializer):
#     subcategory = serializers.SerializerMethodField()
    
#     class Meta:
#         model = Category
#         fields = '__all__'
        
#     def get_subcategory(self, obj):
#         if obj.subcategory.all():
#             return CategorySerializer(obj.subcategory.all(), many=True).data
#         else:
#             return None
        
#     def validate(self, data):
#         # Add validation logic here
#         return data
    
#     def create(self, validated_data):
#         subcategories_data = validated_data.pop('subcategory', None)
#         category = Category.objects.create(**validated_data)
#         if subcategories_data:
#             for subcategory_data in subcategories_data:
#                 Category.objects.create(parent=category, **subcategory_data)
#         return category
    
#     def update(self, instance, validated_data):
#         subcategories_data = validated_data.pop('subcategory', None)
#         for key, value in validated_data.items():
#             setattr(instance, key, value)
#         instance.save()
#         if subcategories_data:
#             for subcategory_data in subcategories_data:
#                 if 'id' in subcategory_data:
#                     subcategory = Category.objects.get(id=subcategory_data['id'])
#                     Category.objects.filter(id=subcategory_data['id']).update(**subcategory_data)
#                 else:
#                     Category.objects.create(parent=instance, **subcategory_data)
#         return instance
