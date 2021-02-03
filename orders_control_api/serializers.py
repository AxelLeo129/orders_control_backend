from rest_framework import serializers
from .models import Producto, Compra, Producto_compra
from django.contrib.auth.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
    
    class Meta:
        model = User
        fields = ('id', 'is_superuser', 'username', 'first_name', 'last_name', 'email', 'password')

class ProductoSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Producto
        fields = ('id', 'url', 'nombre', 'precio', 'vendedor', 'fecha_creacion', 'fecha_actualizacion')

class CompraSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Compra
        fields = ('id', 'url', 'nombre', 'total', 'fecha_creacion', 'fecha_actualizacion')

class Producto_compraSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Producto_compra
        fields = ('id', 'url', 'cantidad', 'precio', 'compra', 'producto', 'fecha_creacion', 'fecha_actualizacion')