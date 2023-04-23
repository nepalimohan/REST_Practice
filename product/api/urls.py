from django.urls import path, include
from product.api.views import *

urlpatterns = [
    path('category/', CategoryMixins.as_view(), name='category_list'),
    path('category/<int:pk>/', CategoryDetails.as_view(), name='category'),
    
    path('products/', ProductListGenericView.as_view(), name='products'),
    path('products/<int:pk>/', ProductDetailsGenericViews.as_view(), name='product-details'),
]
