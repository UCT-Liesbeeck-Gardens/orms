from django.db import models

class Flat(models.Model):
	"""building/flat model"""
	flat_floor = models.CharField(max_length=10)
	flat_number = models.CharField(max_length=10)
	room_number = models.CharField(max_length=10)
	flat_type = models.CharField(max_length=10)
	additional_info = models.CharField(max_length=100)

	def __unicode__(self):
		return self.flat_number

class Application(models.Model):
	"""student applicants model"""
	flat_number = model.CharField(max_length=10)
	student_number = model.CharField(max_length=10)
	mobile_number = model.CharField(max_length=20)
	email_address = model.CharField(max_length=20)
	gender = model.CharField(max_length=10)
	data_of_application = model.DateTimeField('date applied')

	def __unicode__(self):
		return self.student_number
		