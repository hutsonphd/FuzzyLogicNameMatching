import csv
from django.contrib import messages
from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect


from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import *
from .serializers import *
import app.name_matches as name_matches

fs = FileSystemStorage(location='tmp/')

# Viewsets
class EntsoViewSet(viewsets.ModelViewSet):
	"""
	A simple ViewSet for viewing and editing Entso.
	"""
	queryset = Entso.objects.all()
	serializer_class = EntsoSerializer

	@action(detail=False, methods=['POST'])
	def upload_data(self, request):
		"""Upload data from CSV"""
		file = request.FILES["file"]

		content = file.read()  # these are bytes
		file_content = ContentFile(content)
		file_name = fs.save(
			"_tmp.csv", file_content
		)
		tmp_file = fs.path(file_name)

		csv_file = open(tmp_file, errors="ignore")
		reader = csv.reader(csv_file)
		next(reader)
		
		entso_list = []
		for id_, row in enumerate(reader):
			(
				entso_unit_id,
				unit_capacity,
				unit_fuel,
				country,
				unit_name,
				plant_name,
				plant_capacity
			) = row
			entso_list.append(
				Entso(
					entso_unit_id=entso_unit_id,
					unit_capacity=unit_capacity,
					unit_fuel=unit_fuel,
					country=country,
					unit_name=unit_name,
					plant_name=plant_name,
					plant_capacity=plant_capacity,
				)
			)

		Entso.objects.bulk_create(entso_list)
		name_matches.mapEntso()
		name_matches.mapGppd()
		name_matches.mapPlatts()

		messages.success(request, 'Successfully uploaded Entso data')

		return redirect('app:home')


class GppdViewSet(viewsets.ModelViewSet):
	"""
	A simple ViewSet for viewing and editing Gppd.
	"""
	queryset = Gppd.objects.all()
	serializer_class = GppdSerializer

	@action(detail=False, methods=['POST'])
	def upload_data(self, request):
		"""Upload data from CSV"""
		file = request.FILES["file"]

		content = file.read()  # these are bytes
		file_content = ContentFile(content)
		file_name = fs.save(
			"_tmp.csv", file_content
		)
		tmp_file = fs.path(file_name)

		csv_file = open(tmp_file, errors="ignore")
		reader = csv.reader(csv_file)
		next(reader)
		
		gppd_list = []
		for id_, row in enumerate(reader):
			(
				gppd_plant_id,
				plant_name,
				latitude,
				longitude,
				platts_plant_id,
				country,
				country_long,
				plant_capacity,
				plant_primary_fuel,
				commissioning_year,
				owner
			) = row
			gppd_list.append(
				Gppd(
					gppd_plant_id=gppd_plant_id,
					plant_name=plant_name,
					latitude=latitude,
					longitude=longitude,
					platts_plant_id=platts_plant_id,
					country=country,
					country_long=country_long,
					plant_capacity=plant_capacity,
					plant_primary_fuel=plant_primary_fuel,
					commissioning_year=commissioning_year,
					owner=owner
				)
			)

		Gppd.objects.bulk_create(gppd_list)
		messages.success(request, 'Successfully uploaded Gppd data')

		return redirect('app:home')


class PlattsViewSet(viewsets.ModelViewSet):
	"""
	A simple ViewSet for viewing and editing Platt.
	"""
	queryset = Platt.objects.all()
	serializer_class = PlattsSerializer

	@action(detail=False, methods=['POST'])
	def upload_data(self, request):
		"""Upload data from CSV"""
		file = request.FILES["file"]

		content = file.read()  # these are bytes
		file_content = ContentFile(content)
		file_name = fs.save(
			"_tmp.csv", file_content
		)
		tmp_file = fs.path(file_name)

		csv_file = open(tmp_file, errors="ignore")
		reader = csv.reader(csv_file)
		next(reader)
		
		platt_list = []
		for id_, row in enumerate(reader):
			(
				platts_plant_id,
				platts_unit_id,
				plant_name,
				unit_name,
				owner,
				unit_capacity,
				year_commissioned,
				unit_fuel,
				city,
				state,
				region,
				country,
				subregion
			) = row
			platt_list.append(
				Platt(
					platts_plant_id=platts_plant_id,
					platts_unit_id=platts_unit_id,
					plant_name=plant_name,
					unit_name=unit_name,
					owner=owner,
					unit_capacity=unit_capacity,
					year_commissioned=year_commissioned,
					unit_fuel=unit_fuel,
					city=city,
					state=state,
					region=region,
					country=country,
					subregion=subregion
				)
			)

		Platt.objects.bulk_create(platt_list)
		messages.success(request, 'Successfully uploaded Platt data')

		return redirect('app:home')


