from django.contrib import admin
from users.models import Profile
from users.models import Agencia
from users.models import Empresa

# Register your models here.
"""Forma basica de poner la aplicacion al Admin"""
# admin.site.register(Profile)



@admin.register(Empresa)
class EmpresaAdmin (admin.ModelAdmin):
    fieldsets = (

        ('Informacion General', { 
            "fields": (
            ('codigo','nombre'),
            ('descripcion','logo'),
            )
        }),
    )
    """Campos de Solo Lectura"""
    readonly_fields = ('created','modified')





@admin.register(Agencia)
class AgenciaAdmin (admin.ModelAdmin):

    fieldsets = (

        ('Informacion General', { 
            "fields": (
            ('empresa','codigo','nombre'),
            ('descripcion','foto'),
            )
        }),

        ('Direccion', {
            "fields": (
            ('pais','ciudad',),
            ('direccion','lat','lng'),
            )
        }),

        ('Contacto', {
            "fields": (
            ('telefono','telefono2','responsable'),
            )
        }),

        ('Metadata', {
            "fields": (
            ('created','modified'),
            )
        }),
    )

    """Campos de Solo Lectura"""
    readonly_fields = ('created','modified')
    



@admin.register(Profile)
class ProfileAdmin (admin.ModelAdmin):

    """EJEMPLOS 

        ('Opciones Avanzadas', {
            'classes': ('collapse',),
            'fields': ('website','phone_number'),
        }),
    """

    """Campos que apareceran en el listado"""
    list_display = ('pk', 'picture','user','area')
    list_display_links = ('pk','user')
    list_editable = ('area','picture')


    """Filtros de Busqueda en el listado"""
    search_fields = (
        'user__email',
        'user__username',
        'user__first_name',
        'user__last_name',
    )
    list_filter = ('created','modified', 'user__is_active', 'user__is_staff')



    fieldsets = (

        ('Perfil', {
            "fields": (
            ('user','genero','nacimiento','picture'),
            ('segundo_nombre','segundo_apellido'),
            )
        }),

        ('Documento de Identidad', {
            "fields": (
            ('documento','ci','ciextend','expedido'),
            )
        }),

        ('Direccion', {
            "fields": (
            ('ciudad','direccion'),
            ('lat','lng')
            )
        }),

        ('Contacto ', {
            "fields": (
            ('cel_corp','tel_corp','interno'),
            ('cel_per','tel_per')
            )
        }),

        ('Persona de Contacto en Caso de Emergencia', {
            'classes': ('collapse',),
            'fields':  ('nom_emer','tel_emer')
        }),


        ('Informacion Laboral', {
            "fields": (
            ('cargo','area','estado','agencia')
            )
        }),

        ('Metadata', {
            "fields": (
            ('created','modified'),
            )
        }),
    )

    """Campos de Solo Lectura"""
    readonly_fields = ('created','modified')
    