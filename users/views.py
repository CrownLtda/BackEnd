from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

#Decoradores
from django.contrib.auth.decorators import login_required
#Modelos
from django.contrib.auth.models import User, Group
from users.models import Profile

#Exepciones
from django.db.utils import IntegrityError

# rest
from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import UserSerializer, GroupSerializer



def home (request):
    """
    Vista TEMPORAL para dashboard
    """
    return render (request, 'home/index.html')

def profile (request):
    """
    Vista TEMPORAL para perfil de usuario
    """
    return render (request, 'profile/profile.html')

@login_required
def logout_view (request):
    print ('LOGOUT')
    logout(request)
    return redirect ('login')

def login_view(request):
    """
    Vista para el logueo a la aplicacion
    """
    if request.method == 'POST':
        print ('*' * 10)
        print (request.POST)
        username = request.POST['username']
        password = request.POST ['password']

        user = authenticate(request, username = username, password = password)
        print (user)

        if user:
            login(request, user)
            return redirect ('home')
        else:
            return render (
                request, 
                'users/login.html', 
                {'error': 'Usuario o Contraseña Incorrecto'}
            )
        print ('*' * 10)
    return render (request, 'users/login.html')


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

    def get_paginated_response(self, data):
           return Response(data)


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

def signup (request):
    
    if request.method == 'POST':
        username = request.POST ['username']
        passwd = request.POST['passwd']
        passwd_confirmation =  request.POST ['passwd_confirmation']

        if passwd != passwd_confirmation:
            return render (request, 'users/signup.html', {'error':'Las contraseñas no coinciden'})
        
        try:
            user = User.objects.create_user(username=username, password=passwd)
        except IntegrityError:
            return render(request, 'users/signup.html', {'error': 'El usuario ya existe'})

        #Linea de creacion del usuario
        user = User.objects.create_user(username=username, password= passwd)

        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']

        profile = Profile(user=user)
        profile.save()
        user.save()
    return render (request, 'users/signup.html')