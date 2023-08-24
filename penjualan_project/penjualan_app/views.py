from django.shortcuts import render
from rest_framework import viewsets
from .models import Customer, Petugas, Barang, Transaksi
from .serializers import CustomerSerializer, PetugasSerializer, BarangSerializer, TransaksiSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime

from rest_framework.decorators import api_view
from rest_framework.reverse import reverse

# Create your views here.
@api_view(['GET'])
def api_root(request, format=None):
  return Response({
    'customer': reverse('customer-list', request=request, format=format),
    'barang': reverse('barang-list', request=request, format=format),
    'petugas': reverse('petugas-list', request=request, format=format),
  })

class CustomerViewSet(viewsets.ModelViewSet):
  queryset = Customer.objects.all()
  serializer_class = CustomerSerializer
  
class PetugasViewSet(viewsets.ModelViewSet):
  queryset = Petugas.objects.all()
  serializer_class = PetugasSerializer
  
class BarangViewSet(viewsets.ModelViewSet):
  queryset = Barang.objects.all()
  serializer_class = BarangSerializer
  
class TransaksiViewSet(viewsets.ModelViewSet):
  queryset = Transaksi.objects.all()
  serializer_class = TransaksiSerializer