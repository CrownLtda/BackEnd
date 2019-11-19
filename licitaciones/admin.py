from django.contrib import admin
from licitaciones.models import Licitacion, Postulacion

# Register your models here.


@admin.register(Licitacion)
class LicitacionAdmin (admin.ModelAdmin):

    fieldsets = (

        ('Informacion General', {
            "fields": (
            ('nombre','convocatoria','ciudad'),
            )
        }),

        ('Descripcion', {
            "fields": (
            ('item','marca'),
            ('cantidad','monto_ref'),
            )
        }),

        ('Estado', {
            "fields": (
            ('estado','presentacion'),
            ('observacion','responsable'),
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


@admin.register(Postulacion)
class PostulacionAdmin (admin.ModelAdmin):
    fieldsets = (

        ('Informacion General', {
            "fields": (
            ('licitacion','presentacion','observacion'),
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


