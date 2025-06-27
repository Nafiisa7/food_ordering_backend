from django.db import models
from django.conf import settings
from Menu.models import FoodItem

class CartItem(models.Model):
    user      = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    food      = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    quantity  = models.PositiveIntegerField(default=1)
    added_at  = models.DateTimeField(auto_now_add=True)

class Order(models.Model):
    STATUS_CHOICES = [
        ("PENDING", "Pending"),
        ("PROCESSING", "On process"),
        ("DELIVERED", "Delivered"),
    ]
    user       = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items      = models.ManyToManyField(CartItem)
    status     = models.CharField(max_length=12, choices=STATUS_CHOICES, default="PENDING")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def total_price(self):
        return sum(ci.food.price * ci.quantity for ci in self.items.all())