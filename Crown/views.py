"""
Vistas del Proyecto
"""
from django.http import HttpResponse
from datetime import datetime

def hello_world(request):
    return HttpResponse ('La hora del servidor es:{now}'.format(
        now=datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    ))

def hi (request):
    """
    debuger
    import pdb; pdb.set_trace()
    
    valores obtenidos desde la URL ej: 
    
    """
    
    numbers =request.GET['numbers']
    return HttpResponse (str(numbers))
