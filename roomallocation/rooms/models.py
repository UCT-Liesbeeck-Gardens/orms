from django.db import models

class Floor(models.Model):
	floor = models.IntegerField(unique=True)

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
	email_address = models.CharField(max_length=100)
	gender = models.CharField(max_length=10)
	date_of_application = models.DateTimeField('date applied')

	def __unicode__(self):
		return self.student_number

class Approval(models.Model):
	"""applications approval model"""
	flat_number = models.CharField(max_length=10)
	name = models.CharField(max_length=20)
	student_number = models.CharField(max_length=10)
	mobile_number = models.CharField(max_length=20)
	email_address = models.CharField(max_length=100)
	gender = models.CharField(max_length=10)
	date_of_approval = models.DateTimeField('date approved')

	def __unicode__(self):
		return self.student_number

class Decline(models.Model):
	"""applications declines model"""
	flat_number = models.CharField(max_length=10)
	name = models.CharField(max_length=20)
	student_number = models.CharField(max_length=10)
	mobile_number = models.CharField(max_length=20)
	email_address = models.CharField(max_length=100)
	gender = models.CharField(max_length=10)
	date_of_decline = models.DateTimeField('date declined')

	def __unicode__(self):
		return self.student_number