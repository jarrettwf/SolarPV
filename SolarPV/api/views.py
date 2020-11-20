from rest_framework import generics
from ..models import Product, Certificate, Service
from .serializers import productSerializer, certificateSerializer, serviceSerializer

class productListView(generics.ListAPIView):
	queryset = Product.objects.all()
	serializer_class = productSerializer

class productDetailView(generics.RetrieveAPIView):
	queryset = Product.objects.all()
	serializer_class = productSerializer

class certificateListView(generics.ListAPIView):
	queryset = Certificate.objects.all()
	serializer_class = certificateSerializer

class certificateDetailView(generics.RetrieveAPIView):
	queryset = Certificate.objects.all()
	serializer_class = certificateSerializer

class serviceListView(generics.ListAPIView):
	queryset = Service.objects.all()
	serializer_class = serviceSerializer

class serviceDetailView(generics.RetrieveAPIView):
	queryset = Service.objects.all()
	serializer_class = serviceSerializer

