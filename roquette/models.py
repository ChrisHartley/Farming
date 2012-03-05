from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
#import django.contrib.auth.models
from django.contrib.auth.models import User

class Farm(models.Model):
	name = models.CharField(max_length=100)
	def __unicode__(self):
        	return self.name

class Activity(models.Model):
	parent = models.ForeignKey('self', null=True, blank=True)
	name = models.CharField(max_length=100)
	clear = models.BooleanField()
	def __unicode__(self):
        	return self.name

class Photo(models.Model):
	farm = models.ForeignKey(Farm)
	description = models.CharField(max_length=100)
	image = models.ImageField(upload_to='photos/%Y/%m/%d')
	def __unicode__(self):
        	return self.description

class Unit(models.Model):
	farm = models.ForeignKey(Farm)
	name = models.CharField(max_length=10)
	def __unicode__(self):
		return self.name

class Plant(models.Model):
	farm = models.ForeignKey(Farm)
	parent = models.ForeignKey('self', null=True, blank=True)
# 	parent = TreeForeignKey('self', null=True, blank=True, related_name='children')
	name = models.CharField(max_length=100)
	description = models.CharField(max_length=1024, blank=True)
	photos = models.ManyToManyField(Photo, null=True, blank=True)
	units = models.ForeignKey(Unit)
	def __unicode__(self):
        	return self.name

class Location(models.Model):
	farm = models.ForeignKey(Farm)
	parent = models.ForeignKey('self', null=True, blank=True)
	name = models.CharField(max_length=100)
	size = models.IntegerField()
	photos = models.ManyToManyField(Photo, null=True, blank=True)
	def __unicode__(self):
        	return self.name

class Worker(models.Model):
	farm = models.ForeignKey(Farm)
	name = models.CharField(max_length=100)
	email = models.CharField(max_length=100, blank=True)
	phone = models.CharField(max_length=100, blank=True)
	signed_waiver = models.BooleanField()
	notes = models.TextField(blank=True)
	photos = models.ManyToManyField(Photo, null=True, blank=True)
	username = models.ForeignKey(User, null=True)
#	username = models.CharField(max_length=100)
	def __unicode__(self):
        	return self.name

class farmingRecord(models.Model):
	farm = models.ForeignKey(Farm)
	timestamp = models.DateTimeField('datetime record created', auto_now_add=True) # (time first entered in db)
	start_time = models.DateTimeField('start time')
	end_time = models.DateTimeField('end time')
	activity = models.ForeignKey(Activity, null=True, blank=True)
	locations = models.ManyToManyField(Location, null=True, blank=True)
	plants = models.ManyToManyField(Plant, null=True, blank=True)
	workers = models.ManyToManyField(Worker, null=True, blank=True)
	quantity = models.IntegerField(null=True, blank=True)
	quantity_units = models.CharField(max_length=100, null=True, blank=True)
	notes = models.TextField(null=True, blank=True)
	photos = models.ManyToManyField(Photo, null=True, blank=True)
#	trackingCode = models.CharField(max_length=4, blank=True)
	def __unicode__(self):
        	return unicode(self.timestamp)












