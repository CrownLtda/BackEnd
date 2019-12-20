""" CREACION DE MODELOS
        AGENCIA
        PROFILE
 """


from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
#django-countries 5.5 A Django application that provides country choices for use with forms.
from django_countries.fields import CountryField


class Empresa (models.Model):
    """
    Informacion General
    """
    #codigo unico de la empresa, automatizado en FRONT END
    codigo = models.CharField(max_length=6,primary_key=True,blank = False,help_text="El codigo de la empresa debe contener 6 digitos Ejemplo: LPZ001",unique = True)
    nombre = models.CharField(max_length=50,blank=False,unique = True)
    descripcion = models.TextField (max_length= 100, blank = True)
    logo = models.ImageField(
        upload_to='users/logo', 
        blank=True, 
        null=True
    )

    """
    Informacion de Creacion Solo Lectura
    """
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (self.nombre)


class Agencia (models.Model):

    """
    Informacion General
    """
    #Many-to-one relationship
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    codigo = models.CharField(max_length=6,primary_key=True,blank = False,help_text="El codigo de la agencia debe contener 6 digitos Ejemplo: LPZ001",unique = True)
    nombre = models.CharField(max_length=50,blank=False,unique = True)
    descripcion = models.CharField (max_length= 100, blank = True)
    foto = models.ImageField(
        upload_to='users/agencias', 
        blank=True, 
        null=True
    )

    """
    Direccion
    """
    pais = CountryField()
    CIUDADES= (
    ('LAPAZ','La Paz'),
    ('SANTACRUZ','Santa Cruz'),
    ('COCHABAMBA', 'Cochabamba'),
    ('ORURO', 'Oruro'),
    ('POTOSI', 'Potosi'),
    ('TARIJA', 'Tarija'),
    ('SUCRE', 'Sucre'),
    ('BENI', 'Beni'),
    ('PANDO', 'Pando')
    )
    ciudad = models.CharField(max_length=20,blank=False, choices= CIUDADES)
    direccion = models.CharField (max_length= 150, blank = True)
    lat = models.CharField(max_length = 50,blank = True)
    lng = models.CharField(max_length = 50,blank = True)

    """
    Contacto
    """
    telefono = models.IntegerField(blank = True, null = True)
    telefono2 = models.IntegerField(blank = True, null = True)
    responsable = models.ForeignKey(User, on_delete=models.CASCADE,blank=False)
    """
    Informacion de Creacion Solo Lectura
    """
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s %s" % (self.nombre, self.ciudad)




class Profile (models.Model):   
    """Proxy model that extends the base data with other information"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    GENEROS = (
    ('M', 'Masculino'),
    ('F', 'Femenino')
    )
    genero = models.CharField(max_length=30, choices= GENEROS, default='M')
    nacimiento = models.DateField(default = '1985-01-01', blank = False)


    picture = models.ImageField(
        upload_to='users/fotosperfil', 
        blank=True, 
        null=True
    )
    segundo_nombre = models.CharField(blank = True, max_length=20)
    segundo_apellido = models.CharField(blank = True, max_length=20) 


    """
    En esta seccion se modelan los datos del documento unico de identidad
    """
    DOCUMENTOS = (
    ('CI', 'Cedula de Identidad'),
    ('PE', 'Carnet de Extranjero'),
    ('PAS', 'Pasaporte'),
    ('CD','Cedula de Identidad Duplicada')
    )
    documento = models.CharField(blank = False, max_length=30, choices= DOCUMENTOS, default='CI')
    ci = models.IntegerField(primary_key=True, blank = False,unique = True)
    ciextend = models.CharField(blank = True, max_length=10)
    DEPARTAMENTOS = (
    ('LPZ', 'La Paz'),
    ('SCZ', 'Santa Cruz'),
    ('CBA', 'Cochabamba'),
    ('TJA', 'Tarija'),
    ('CHQ', 'Chuquisaca'),
    ('ORU', 'Oruro'),
    ('PSI', 'Potosi'),
    ('BNI', 'Beni'),
    ('PND', 'Pando')
    )
    expedido = models.CharField(blank = False, max_length=20, choices= DEPARTAMENTOS)

    """
    En esta seccion se modelan los datos de la direccion 
    """
    ciudad = models.CharField(blank = False, max_length=20, choices= DEPARTAMENTOS)
    direccion = models.CharField (max_length= 300, blank = False)
    lat = models.CharField(max_length = 50, blank = True)
    lng = models.CharField(max_length = 50, blank = True)


    """
    En esta seccion se modelan los datos de la contacto 
    """

    cel_corp = models.IntegerField(null=True, blank = True)
    tel_corp = models.IntegerField(null=True,blank = True)
    interno = models.IntegerField(null=True,blank = True)

    cel_per = models.IntegerField(null=True,blank = True)
    tel_per = models.IntegerField(null=True,blank = True)

    nom_emer = models.CharField(blank = True, max_length=10)
    tel_emer = models.IntegerField(null=True,blank = True)


    """
    Informacion Laboral
    """

    CARGOS = (
    ('GERENTE', 'Gerente'),
    ('SUBGERENTE', 'Sub Gerente'),
    ('JEFE', 'Jefe'),
    ('RESPONSABLE', 'Responsable'),
    ('ANALISTA', 'Analista'),
    ('EJECUTIVO', 'Ejecutivo'),
    ('ASISTENTE', 'Asistente'),
    ('MECANICO', 'Mecanico'),
    ('MENSAJERO', 'Mensajero'),
    ('PASANTE', 'Pasante')
    )
    cargo = models.CharField(max_length=30, choices= CARGOS)
    AREAS = (
    ('VENTAS', 'Ventas'),
    ('FINANZAS', 'Finanzas'),
    ('CARTERA', 'Cartera'),
    ('MARKETING', 'Marketing'),
    ('CONTABILIDAD', 'Contabilidad'),
    ('RRHH', 'Recursos Humanos'),
    ('SISTEMAS', 'Sistemas'),
    ('SERVICIOS', 'Servicios'),
    ('TALLER', 'Taller'),
    ('LICITACIONES', 'Licitaciones'),
    ('IMPORTACIONES', 'Importaciones'),
    ('LEGAL', 'Legal'),
    ('AGENCIAINTERNA', 'Agencia Interna')
    )
    area = models.CharField(max_length=30, choices= AREAS)
    ESTADOS = (
    ('ACTIVO', 'Activo'),
    ('BAJA', 'Baja'),
    ('BAJATEMP', 'Baja Temporal')
    )
    estado = models.CharField(max_length=15, choices= ESTADOS)
    #relacion con modelo agencia
    agencia = models.ForeignKey(Agencia, on_delete=models.CASCADE,blank=False)
    
    
    """
    Informacion de Creacion Solo Lectura
    """
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username




