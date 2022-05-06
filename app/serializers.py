from rest_framework import serializers
from .models import *

#Serializers
class EntsoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Entso
		fields = "__all__"

class GppdSerializer(serializers.ModelSerializer):
	class Meta:
		model = Gppd
		fields = "__all__"

class PlattsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Platt
		fields = "__all__"