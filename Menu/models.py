from django.db import models
class FoodItem(models.Model):
    name        = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    price       = models.DecimalField(max_digits=8, decimal_places=2)
    image       = models.ImageField(upload_to="foods/")
    is_active   = models.BooleanField(default=True)

    def _str_(self):
        return self.name 
