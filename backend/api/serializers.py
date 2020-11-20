from rest_framework import serializers
from ..models import Product, Service, Certificate

class productSerializer(serializers.ModelSerializer):
	class Meta:
		model = Product
		fields = ['modelNumber', 'productName', 'cellTechnology', 'cellManufacturer', 'numberOfCells', 'cellsInSeries', 'seriesStrings', 'numberOfDiodes', 'productLength', 'productWidth', 'productWeight', 'superstateType', 'superstateManufacturer', 'substrateType', 'substrateManufacturer', 'frameType', 'frameAdhesive', 'encapsulateType', 'encapsulantManufacturer', 'junctionType', 'junctionManufacturer']

class serviceSerializer(serializers.ModelSerializer):
	class Meta:
		model = Service
		fields = ['serviceID', 'serviceName', 'description', 'fiRequired', 'fiFrequency', 'standard']

class certificateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Certificate
		fields = ['certNumber', 'ID', 'user', 'reportNumber', 'issueDate', 'standard', 'location', 'model']