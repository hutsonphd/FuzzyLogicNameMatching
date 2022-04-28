import uuid
from xmlrpc.client import Boolean 
from django.db import models
from django.db.models.fields import BooleanField, DateTimeField, CharField, UUIDField, TextField, DecimalField
from django.db.models import JSONField

class Gppd(models.Model):
	id= UUIDField(default=uuid.uuid4,primary_key=True,editable=False)
	gppd_plant_id= CharField(max_length=1024, default=None, null=True)
	plant_name= CharField(max_length=1024, default=None, null=True)
	latitude= CharField(max_length=1024, default=None, null=True)
	longitude= CharField(max_length=1024, default=None, null=True)
	platts_plant_id= CharField(max_length=1024, default=None, null=True)
	country= CharField(max_length=1024, default=None, null=True)
	country_long= CharField(max_length=1024, default=None, null=True)
	plant_capacity= CharField(max_length=1024, default=None, null=True)
	plant_primary_fuel= CharField(max_length=1024, default=None, null=True)
	commissioning_year= CharField(max_length=1024, default=None, null=True)
	owner= CharField(max_length=1024, default=None, null=True)
	mapped = BooleanField(default=False)
	createdAt= DateTimeField(auto_now_add=True)
	updatedAt= DateTimeField(auto_now=True)

	class Meta:
		db_table = "gppd"
		verbose_name_plural= "Gppd"
		ordering= ['plant_name']
	
	def __str__(self):
		return(self.plant_name)

class Entso(models.Model):
	id= UUIDField(default=uuid.uuid4,primary_key=True,editable=False)
	entso_unit_id= CharField(max_length=1024, default=None, null=True)
	unit_capacity= CharField(max_length=1024, default=None, null=True)
	unit_fuel= CharField(max_length=1024, default=None, null=True)
	country= CharField(max_length=1024, default=None, null=True)
	unit_name= CharField(max_length=1024, default=None, null=True)
	plant_name= CharField(max_length=1024, default=None, null=True)
	plant_capacity= CharField(max_length=1024, default=None, null=True)
	mapped = BooleanField(default=False)
	createdAt= DateTimeField(auto_now_add=True)
	updatedAt= DateTimeField(auto_now=True)

	class Meta:
		db_table = "entso"
		verbose_name_plural= "Entso"
		ordering= ['plant_name']
	
	def __str__(self):
		return(self.plant_name)

class Platt(models.Model):
	id= UUIDField(default=uuid.uuid4,primary_key=True,editable=False)
	platts_plant_id= CharField(max_length=1024, default=None, null=True)
	platts_unit_id= CharField(max_length=1024, default=None, null=True)
	plant_name= CharField(max_length=1024, default=None, null=True)
	unit_name= CharField(max_length=1024, default=None, null=True)
	owner= CharField(max_length=1024, default=None, null=True)
	unit_capacity= CharField(max_length=1024, default=None, null=True)
	year_commissioned= CharField(max_length=1024, default=None, null=True)
	unit_fuel= CharField(max_length=1024, default=None, null=True)
	city= CharField(max_length=1024, default=None, null=True)
	state= CharField(max_length=1024, default=None, null=True)
	region= CharField(max_length=1024, default=None, null=True)
	country= CharField(max_length=1024, default=None, null=True)
	subregion= CharField(max_length=1024, default=None, null=True)
	mapped = BooleanField(default=False)
	createdAt= DateTimeField(auto_now_add=True)
	updatedAt= DateTimeField(auto_now=True)

	class Meta:
		db_table = "platt"
		verbose_name_plural= "Platts"
		ordering= ['plant_name']
	
	def __str__(self):
		return(self.plant_name)

class Mapping(models.Model):
	id= UUIDField(default=uuid.uuid4,primary_key=True,editable=False)
	entso_unit_id= CharField(max_length=1024, default=None, null=True)
	platts_unit_id= CharField(max_length=1024, default=None, null=True)
	gppd_plant_id= CharField(max_length=1024, default=None, null=True)
	createdAt= DateTimeField(auto_now_add=True)
	updatedAt= DateTimeField(auto_now=True)

	class Meta:
		db_table = "mapping"
		verbose_name_plural= "mappings"
		ordering= ['-updatedAt']
	
	def __str__(self):
		return(self.entso_unit_id)
