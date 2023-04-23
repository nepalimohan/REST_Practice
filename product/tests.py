from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from .models import Category, Product
from rest_framework.test import APITestCase

# Create your tests here.
class CatTest(APITestCase):
    def test_create_category(self):
        url = reverse('category_list')
        data = {'category': 'Electronics'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
       

# class CategoryTestCase(TestCase):
#     def test_create_category(self):
#         category_data = {'category': 'Electronics'}
#         response = self.client.post(reverse('category-list'), category_data)
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
# def test_create_product(self):
#     category = Category.objects.create(category='Electronics')
#     product_data = {
#         'name': 'Laptop',
#         'category': category.pk,
#         'price': '1500.00',
#         'color': 'Black',
#         'stock': 10,
#         'description': 'A high-performance laptop.'
#     }
#     response = self.client.post(reverse('product-list'), product_data)
#     self.assertEqual(response.status_code, status.HTTP_201_CREATED)

# def test_retrieve_category(self):
#     category = Category.objects.create(category='Electronics')
#     response = self.client.get(reverse('category-detail', kwargs={'pk': category.pk}))
#     self.assertEqual(response.status_code, status.HTTP_200_OK)
#     self.assertEqual(response.data['category'], category.category)

# def test_retrieve_product(self):
#     category = Category.objects.create(category='Electronics')
#     product = Product.objects.create(name='Laptop', category=category, price='1500.00', color='Black', stock=10, description='A high-performance laptop.')
#     response = self.client.get(reverse('product-detail', kwargs={'pk': product.id}))
#     self.assertEqual(response.status_code, status.HTTP_200_OK)
#     self.assertEqual(response.data['name'], product.name)

# def test_update_product(self):
#     category = Category.objects.create(category='Electronics')
#     product = Product.objects.create(name='Laptop', category=category, price='1500.00', color='Black', stock=10, description='A high-performance laptop.')
#     product_data = {
#         'name': 'Updated Laptop',
#         'price': '2000.00',
#         'stock': 5,
#     }
#     response = self.client.patch(reverse('product-detail', kwargs={'pk': product.id}), product_data)
#     self.assertEqual(response.status_code, status.HTTP_200_OK)
#     product.refresh_from_db()
#     self.assertEqual(product.name, 'Updated Laptop')
#     self.assertEqual(product.price, Decimal('2000.00'))
#     self.assertEqual(product.stock, 5)

# def test_delete_category(self):
#     category = Category.objects.create(category='Electronics')
#     response = self.client.delete(reverse('category-detail', kwargs={'pk': category.id}))
#     self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
#     self.assertFalse(Category.objects.filter(id=category.id).exists())


# def test_delete_product(self):
#     category = Category.objects.create(category='Electronics')
#     product = Product.objects.create(name='Laptop', category=category, price='1500.00', color='Black', stock=10, description='A high-performance laptop.')
#     response = self.client.delete(reverse('product-detail', kwargs={'pk': product.id}))
#     self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
#     self.assertFalse(Product.objects.filter(id=product.id).exists())
