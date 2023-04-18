from rest_framework.decorators import api_view
from rest_framework.views import APIView

from rest_framework import serializers
from product.models import Category, Product
from product.api.serializers import CategorySerializer, ProductSerializer
from rest_framework.response import Response

        
class CategoryView(APIView):
    def get(self, request):
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = CategorySerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
class CategoryDetails(APIView):
    def get(self, request, pk):
        category = Category.objects.get(pk=pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data)
        
    def put(self, request, pk):
        category = Category.objects.get(id=pk)
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            if category.parent == None:
                category.parent=None
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
class ProductView(APIView):
    def get(self, request):
        product = Product.objects.all().order_by('-created_at')
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    