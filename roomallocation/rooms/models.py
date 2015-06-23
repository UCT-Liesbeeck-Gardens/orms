from django.db import models

class Floor(models.Model):
	floor = models.IntegerField(unique=True)

	def __unicode__(self):
		return self.floor


class FlatType(models.Model):
	flat_type = models.CharField(max_length=20, unique=True)

	def __unicode__(self):
		return self.flat_type


class Flat(models.Model):
	"""building/flat model"""
	flat_floor = models.ForeignKey(Floor)
	flat_type = models.ForeignKey(FlatType)
	flat_number = models.CharField(max_length=10, unique=True)
	additional_info = models.CharField(max_length=100)

	def __unicode__(self):
		return self.flat_number

class Student(models.Model):
	"""student model"""
	student_number	= models.CharField(max_length=20, unique=True)
	name = models.CharField(max_length=30)
	gender = models.CharField(max_length=10)
	mobile_number = models.CharField(max_length=20)
	email_address = models.CharField(max_length=100)

	def __unicode__(sefl):
		return self.student_number

class Application(models.Model):
	"""student applicants model"""
	flat_number = models.ForeignKey(Flat)
	student = models.ForeignKey(Student)
	date_of_application = models.DateTimeField('date applied')

	def __unicode__(self):
		return self.student

class Approval(models.Model):
	"""applications approval model"""
	flat_number = models.ForeignKey(Flat)
	student = models.ForeignKey(Student)
	date_of_approval = models.DateTimeField('date approved')

	def __unicode__(self):
		return self.student

class Decline(models.Model):
	"""applications declines model"""
	flat_number = models.ForeignKey(Flat)
	student = models.ForeignKey(Student)
	date_of_approval = models.DateTimeField('date declined')

	def __unicode__(self):
		return self.student