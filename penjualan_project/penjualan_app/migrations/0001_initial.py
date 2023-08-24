# Generated by Django 4.2.4 on 2023-08-20 10:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Barang',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('barang_stok', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_nama', models.CharField(max_length=100)),
                ('customer_gender', models.IntegerField(choices=[(1, 'Not Choices'), (2, 'Laki-laki'), (3, 'Perempuan')], default=1)),
                ('customer_email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Petugas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('petugas_nama', models.CharField(max_length=100)),
                ('petugas_gender', models.IntegerField(choices=[(1, 'Not Choices'), (2, 'Laki-laki'), (3, 'Perempuan')], default=1)),
                ('petugas_email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Transaksi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_harga', models.DecimalField(decimal_places=2, max_digits=10)),
                ('barang_relasi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='penjualan_app.barang')),
                ('customer_relasi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='penjualan_app.customer')),
            ],
        ),
    ]
