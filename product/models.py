from django.db import models

# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=100, null=True)
    parent =models.ForeignKey("self", related_name='subcategory', on_delete=models.CASCADE,null=True,blank=True)
    
    def __str__(self):
        return self.category
    

class Product(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8,decimal_places=2)
    # size = models.ForeignKey(Size,on_delete=models.CASCADE)
    
    color = models.CharField(max_length=100, choices=(
        ('Blue', 'Blue'),
        ('Black', 'Black'),
        ('Green', 'Green'),
        ('White', 'White'),
    ))
    
    stock = models.IntegerField()
    image = models.FileField(upload_to='productimage')
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    
   
    def __str__(self):
        return self.name