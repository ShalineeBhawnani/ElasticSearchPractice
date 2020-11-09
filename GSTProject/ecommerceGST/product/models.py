from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=150,db_index=True)
    hsn=models.CharField(max_length=30)
   
class Subcategory(models.Model):
    category = models.ForeignKey(Category,
                                 related_name='subcategory',on_delete=models.CASCADE)
    name = models.CharField(max_length=200,
                            db_index=True)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Subcategory,related_name='products',on_delete=models.CASCADE)
    product_name = models.CharField(max_length=150)
    quantity = models.IntegerField()
    cost_price = models.IntegerField()
    selling_price = models.IntegerField()

    def __str__(self):
        return self.product_name
  
    