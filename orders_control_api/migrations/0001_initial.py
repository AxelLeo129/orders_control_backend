# Generated by Django 3.1.5 on 2021-02-03 22:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_comprador', models.CharField(max_length=50)),
                ('total', models.DecimalField(decimal_places=2, max_digits=8)),
                ('fecha_creacion', models.DateField(auto_now_add=True)),
                ('fecha_actualizacion', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=8)),
                ('fecha_creacion', models.DateField(auto_now_add=True)),
                ('fecha_actualizacion', models.DateField(auto_now=True)),
                ('vendedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Producto_compra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('precio', models.DecimalField(decimal_places=2, max_digits=8)),
                ('fecha_creacion', models.DateField(auto_now_add=True)),
                ('fecha_actualizacion', models.DateField(auto_now=True)),
                ('compra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders_control_api.compra')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders_control_api.producto')),
            ],
        ),
    ]
