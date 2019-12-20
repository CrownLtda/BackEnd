"""Crown URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from Crown import views as local_views
from posts import views as posts_views

#librerias para la ruta estatica y muestra de imagenes
from django.conf import settings
from django.conf.urls.static import static

#importacion para rest framework
from rest_framework import routers
from licitaciones import views as licitaciones_views
from users import views as user_views

#registro de Routers
router = routers.DefaultRouter()
router.register(r'lici', licitaciones_views.LicitacionViewSet)
router.register(r'usersAPI', user_views.UserViewSet)
router.register(r'groupsAPI', user_views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API..

urlpatterns = [

    #ROUTER PARA API REST
    #path('', include(router.urls)),
    path('', user_views.home, name = 'home'),
    path ('hello_world', local_views.hello_world),
    path ('hi', local_views.hi),
    path ('posts/', posts_views.list_posts),


    #URLs correspondientes al logueo
    path('users/login', user_views.login_view, name = 'login'),
    path('users/logout', user_views.logout_view, name = 'logout'),
    path('users/signup', user_views.signup, name = 'signup'),
    
    #URL temporal para el home
    path('home', user_views.home, name = 'home'),
    path('profile', user_views.profile, name = 'profile'),


    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

