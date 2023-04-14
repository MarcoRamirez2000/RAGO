from django.shortcuts import render, redirect
from django.apps import apps
# import pyodbc
from django.shortcuts import render
from django.http import JsonResponse
import requests
import json

from .models import *

# Create your views here.


# def index(request):
#     Fonos = []
#     return render(request, 'index.html', {'Fonos':Fonos})
import requests
import json

def signup(request):
    if request.method == 'POST':
        # Obtener los datos del formulario
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        re_password = request.POST.get('re_password')

        # Configurar las cabeceras de la solicitud
        headers = {
            'Content-Type': 'application/json'
        }

        # Definir el cuerpo de la solicitud
        data = {
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'password': password,
            're_password': re_password
        }

        try:
            # Enviar la solicitud POST a la API
            response = requests.post(
                'http://127.0.0.1:8000/auth/users/',
                headers=headers,
                data=json.dumps(data),
            )

            # Verificar el código de estado de la respuesta
            if response.status_code == 201:

                # Si la solicitud es exitosa, devolver una respuesta JSON con los datos del usuario
                return JsonResponse(response.json(), status=201)
            else:
                # Si hay un error en la solicitud, devolver una respuesta JSON con un mensaje de error
                return JsonResponse({'message': 'Error al crear la cuenta.'}, status=400)

        except:
            # Si hay un error en la conexión con el servidor, devolver una respuesta JSON con un mensaje de error
            return JsonResponse({'message': 'Error conectando con el servidor, intenta más tarde.'}, status=500)

    # Si la solicitud no es POST, renderizar la plantilla del formulario
    return render(request, 'signup.html')


def activate(request, uid, token):
    # Configurar las cabeceras de la solicitud
    headers = {
        'Content-Type': 'application/json'
    }

    # Definir el cuerpo de la solicitud
    data = {
        'uid': uid,
        'token': token,
    }

    try:
        # Enviar la solicitud POST a la API
        response = requests.post(
            'http://127.0.0.1:8000/auth/users/activation/',
            headers=headers,
            data=json.dumps(data),
        )

        # Verificar el código de estado de la respuesta
        if response.status_code == 204:
            # Si la solicitud es exitosa, devolver una respuesta JSON con un mensaje de éxito
            return JsonResponse({'message': 'Cuenta activada exitosamente.'}, status=200)
        else:
            # Si hay un error en la solicitud, devolver una respuesta JSON con un mensaje de error
            return JsonResponse({'message': 'Error al activar la cuenta.'}, status=400)

    except:
        # Si hay un error en la conexión con el servidor, devolver una respuesta JSON con un mensaje de error
        return JsonResponse({'message': 'Error conectando con el servidor, intenta más tarde.'}, status=500)



def login(request):
    if request.method == 'POST':
        # Obtener los datos del formulario
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Configurar las cabeceras de la solicitud
        headers = {
            'Content-Type': 'application/json'
        }

        # Definir el cuerpo de la solicitud
        data = {
            'email': email,
            'password': password
        }

        try:
            # Enviar la solicitud POST a la API
            response = requests.post(
                'http://127.0.0.1:8000/auth/jwt/create/',
                headers=headers,
                data=json.dumps(data),
            )

            # Verificar el código de estado de la respuesta
            if response.status_code == 200:
                data = response.json()
                access_token = data['access']
                refresh_token = data['refresh']
                
                context = {'access_token': access_token,'refresh_token':refresh_token}


                # Si la solicitud es exitosa, devolver una respuesta JSON con el token JWT
                return render(request, 'base.html',context)
            else:
                # Si hay un error en la solicitud, devolver una respuesta JSON con un mensaje de error
                return JsonResponse({'message': 'Error al iniciar sesión.'}, status=400)

        except:
            # Si hay un error en la conexión con el servidor, devolver una respuesta JSON con un mensaje de error
            return JsonResponse({'message': 'Error conectando con el servidor, intenta más tarde.'}, status=500)

    # Si la solicitud no es POST, renderizar la plantilla del formulario
    return render(request, 'login.html')