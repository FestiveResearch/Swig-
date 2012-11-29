from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
	user = models.OneToOneField(User)

class OrderItem(models.Model):
	ORDER_ITEM_TYPE_CHOICES = (
		('B', 'Beer'),
		('W', 'Wine'),
		('L', 'Liquor'),
		('O', 'Other'),
	)
	item_type = models.CharField(max_length=2, choices=ORDER_ITEM_TYPE_CHOICES)
	price = models.DecimalField(max_digits=7, decimal_places=2)
	name = models.CharField(max_length=70)
	
