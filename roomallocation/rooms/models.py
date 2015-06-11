from django.db import models

class Floor(models.Model):
	floor = models.IntegerField()

	def __unicode__(self):
		return self.floor

class Flat(models.Model):
	"""building/flat model"""
	flat_floor = models.ForeignKey(Floor)
	flat_number = models.CharField(max_length=10)
	room_number = models.CharField(max_length=10)
	flat_type = models.CharField(max_length=10)
	additional_info = models.CharField(max_length=100)

	def __unicode__(self):
		return self.flat_number

class Application(models.Model):
	"""student applicants model"""
	flat_number = models.CharField(max_length=10)
	name = models.CharField(max_length=20)
	student_number = models.CharField(max_length=10)
	mobile_number = models.CharField(max_length=20)
	email_address = models.CharField(max_length=20)
	gender = models.CharField(max_length=10)
	data_of_application = models.DateTimeField('date applied')

	def __unicode__(self):
		return self.student_number