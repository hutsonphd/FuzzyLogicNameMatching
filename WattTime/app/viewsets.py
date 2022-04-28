import csv

from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import *
from .serializers import *

fs = FileSystemStorage(location='tmp/')

# Viewsets
class EntsoViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing Product.
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

        return Response("Successfully uploaded the data")


class GppdViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing Product.
    """
    queryset = Gppd.objects.all()
    serializer_class = GppdSerializer

class PlattsViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing Product.
    """
    queryset = Platts.objects.all()
    serializer_class = PlattsSerializer