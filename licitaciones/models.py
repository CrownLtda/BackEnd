
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
# Create your models here.

class Licitacion (models.Model):

    """
    Informacion General
    """
    nombre = models.CharField (max_length= 150, blank = True)
    convocatoria = models.ImageField(
        upload_to='licitaciones/convocatorias', 
        blank=True, 
        null=True
    )
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

    """
    Descripcion de la Solicitid
    """

    ITEMS= (
    ('CAMIONETA','Camioneta'),
    ('VAGONETA', 'Vagoneta'),
    ('AMBULANCIA', 'Ambulancia'),
    ('EXCAVADORA', 'Excavadora'),
    ('RETROEXCAVADORA','Retroexcavadora'),
    ('CARROBOMBERO', 'Carro Bombero'),
    ('CARROBASURERO', 'Carro Basurero'),
    ('MOTO', 'Moto')
    )
    item = models.CharField(max_length=20,blank=False, choices= ITEMS)
    cantidad = models.IntegerField(blank = False, null = False)
    MARCAS= (
    ('INDEFINIDO','Por Definir'),
    ('TOYOTA', 'Toyota'),
    ('HINO', 'Hino'),
    ('VOLVO', 'Volvo'),
    ('SINOTRUK','Sinotruk'),
    ('YAMAHA', 'Yamaha'),
    ('MAXUS', 'Maxus')
    )
    marca = models.CharField(max_length=20,blank=False, choices= MARCAS)
    monto_ref = models.IntegerField(blank = False, null = False)

    """
    Estado de la Solicitid
    """

    ESTADOS = (
    ('INDEFINIDO','Por Definir'),
    ('EVALUACION', 'En Evaluacion'),
    ('REUNION', 'Proxima Reunion'),
    ('PARTICIPACION', 'Se Participara')
    )
    estado = models.CharField(max_length=20,blank=False, choices= ESTADOS)
    presentacion = models.DateField(default = '2019-01-01', blank = False)
    observacion = models.TextField (max_length= 500, blank = True)
    responsable = models.ForeignKey(User, on_delete=models.CASCADE,blank=False)

    """
    Informacion de Creacion Solo Lectura
    """
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

"""
    class Meta:
        verbose_name = _("")
        verbose_name_plural = _("s")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})
)

"""



class Postulacion (models.Model):
    """
    Relacion 1 a n / Una Licitacion puede tener multiples postulaciones.
    """
    licitacion = models.ForeignKey(Licitacion, on_delete=models.CASCADE)
    presentacion = models.DateField(default = '2019-01-01', blank = False)
    observacion = models.TextField (max_length= 500, blank = True)
    """
    Informacion de Creacion Solo Lectura
    """
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.id
