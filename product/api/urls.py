from django.urls import path, include
from product.api.views import CategoryView, ProductView, CategoryDetails

urlpatterns = [
    path('category/', CategoryView.as_view(), name='category'),
    path('category/<int:pk>/', CategoryDetails.as_view(), name='category'),
    
    path('products/', ProductView.as_view(), name='products'),
]
