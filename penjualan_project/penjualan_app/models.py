from django.db import models
from datetime import date

# Create your models here.
class Customer(models.Model):
  customer_nama = models.CharField(max_length=100)
  customer_tanggal_lahir = models.DateField(null=True, blank=True)
  genders = (
    (1, "Not Choices"),
    (2, "Laki-laki"),
    (3, "Perempuan")
  )
  customer_gender = models.IntegerField(choices=genders, default=1)
  customer_email = models.EmailField(default='user@example.com')
  
class Petugas(models.Model):
  petugas_nama = models.CharField(max_length=100)
  petugas_tgl_lhr = models.DateField(default='1999-01-01')
  petugas_genders = (
    (1, "Not Choices"),
    (2, "Laki-laki"),
    (3, "Perempuan")
  )
  petugas_gender = models.IntegerField(choices=petugas_genders, default=1)
  petugas_email = models.EmailField(default='user@example.com')
  
class Barang(models.Model):
  barang_nama = models.CharField(max_length=100, null=True)
  barang_merk = models.CharField(max_length=100, default='Unknown')
  harga = models.IntegerField(default=0)
  barang_stok = models.IntegerField(default=0)
  
class Transaksi(models.Model):
  transaksi_tgl = models.DateField(null=True, blank=True)
  transaksi_qty = models.IntegerField(default=0)
  total_harga = models.DecimalField(max_digits=10, decimal_places=2)
  petugas_relasi = models.ForeignKey(Petugas, on_delete=models.CASCADE, default=1)
  customer_relasi = models.ForeignKey(Customer, on_delete=models.CASCADE, default=1)
  barang_relasi = models.ForeignKey(Barang, on_delete=models.CASCADE, default=1)