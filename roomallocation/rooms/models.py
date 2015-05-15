from django.db import models

class flat(models.Model):
	flat_floor = models.CharField(max_length=10)
	flat_number = models.CharField(max_length=10)
	room_number = models.CharField(max_length=10)
	flat_type = models.CharField(max_length=10)
	additional_info = models.CharField(max_length=100)
