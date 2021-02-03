from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Producto, Compra, Producto_compra
from django.contrib.auth.models import User
from .serializers import ProductoSerializer, CompraSerializer, Producto_compraSerializer, UserSerializer

class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permissions = permissions.AllowAny

class ProductoView(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permissions = permissions.IsAuthenticatedOrReadOnly

class CompraView(viewsets.ModelViewSet):
    queryset = Compra.objects.all()
    serializer_class = CompraSerializer
    permissions = permissions.IsAuthenticatedOrReadOnly

class Producto_compraView(viewsets.ModelViewSet):
    queryset = Producto_compra.objects.all()
    serializer_class = Producto_compraSerializer
    permissions = permissions.IsAuthenticatedOrReadOnly