from django.shortcuts import render

#Importacion del modelo de usuarios
from django.contrib.auth.models import User, Group
#Importacion del modelo de vistas
from rest_framework import viewsets
from licitaciones.serializers import LicitacionSerializer
from .models import Licitacion

class LicitacionViewSet (viewsets.ModelViewSet):
    """
    API endpoint que permite que las licitaciones sean vistas o editadas
    """
    queryset = Licitacion.objects.all()
    serializer_class = LicitacionSerializer
