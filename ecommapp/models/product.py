from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    # class Meta:
    #     # with this we are making base Product class as abstract
    #     abstract = True

class DairyProduct(Product):
    expiration_date = models.DateField(auto_now=False)
    dairy_type = models.CharField(max_length=50, default="Dairy")
    class Meta:
        db_table = 'dairy_products'


