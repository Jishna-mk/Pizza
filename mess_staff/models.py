from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class FoodItem(models.Model):
    food_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="foods", null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity_available = models.IntegerField(default=0)
    quantity_booked = models.IntegerField(default=0)
    booked_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='booked_items', null=True)
    status = models.CharField(max_length=20, default='Pending')
    


    

    def __str__(self):
        return self.name

    def book_item(self, quantity, user):
        if quantity <= self.quantity_available:
            self.quantity_available -= quantity
            self.quantity_booked += quantity
            self.booked_by = user  
            total_price = self.price * quantity
            self.save()
            return total_price, True
        return 0, False
    

from django.db import models
from django.utils import timezone

class AdminNotification(models.Model):
    title = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
