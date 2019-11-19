

#Importacion de los serializadores de REST
from rest_framework import serializers  


#Importacion de modelos para la representacion de datos
from django.contrib.auth.models import User, Group
from django.db import models
from .models import Licitacion
from users import models 

class LicitacionSerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Licitacion
        fields =  ('nombre','convocatoria','ciudad', 'item', 'cantidad', 'marca', 'monto_ref', 'estado', 'presentacion', 'observacion')

