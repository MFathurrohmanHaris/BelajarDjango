from rest_framework import serializers
from .models import Customer, Petugas, Barang, Transaksi

class CustomerSerializer(serializers.ModelSerializer):
  class Meta:
    model = Customer
    fields = ['id', 'customer_nama', 'customer_tanggal_lahir', 'customer_gender', 'customer_email']
    
class PetugasSerializer(serializers.ModelSerializer):
  class Meta:
    model = Petugas
    fields = '__all__'
    
class BarangSerializer(serializers.ModelSerializer):
  class Meta:
    model = Barang
    fields = ['id', 'barang_nama', 'barang_merk', 'harga', 'barang_stok']

class TransaksiSerializer(serializers.ModelSerializer):
  petugas_relasi = PetugasSerializer()
  customer_relasi = CustomerSerializer()
  barang_relasi = BarangSerializer()
  
  class Meta:
    model = Transaksi
    fields = ['id', 'transaksi_tgl', 'transaksi_qty', 'total_harga', 'petugas_relasi', 'customer_relasi', 'barang_relasi']