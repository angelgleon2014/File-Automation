import json
import os
from django.utils.timezone import make_aware
from datetime import datetime
from django.contrib.auth.hashers import make_password

# Configurar Django
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "<tu_proyecto>.settings")  # Reemplaza <tu_proyecto> con el nombre de tu proyecto Django
django.setup()

# Importar el modelo correspondiente
from atlasfitnessclub.models import User  # Reemplaza "User" con el nombre real de tu modelo si es diferente

def process_json(json_path):
    # Cargar el archivo JSON
    with open(json_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    for record in data:
        try:
            # Extraer datos del JSON
            card_no = record["CardNo"]
            name = record["name"]
            lastname = record["lastname"]
            email = record["email"]
            acc_startdate = record["acc_startdate"]

            # Preparar campos del modelo
            password = make_password(card_no)  # Hashear la contraseña usando PBKDF2
            date_joined = make_aware(datetime.strptime(acc_startdate[:-9], "%Y-%m-%d"))  # Parsear la fecha
            full_name = f"{name} {lastname}"  # Concatenar nombre y apellido

            # Crear o actualizar el registro en la base de datos
            user, created = User.objects.update_or_create(
                email=email,
                defaults={
                    "password": password,
                    "last_login": None,
                    "is_superuser": False,
                    "names": full_name,
                    "image": "",  # Campo en blanco
                    "is_active": True,
                    "is_staff": False,
                    "date_joined": date_joined,
                    "is_change_password": False,
                    "email_reset_token": None,
                },
            )

            if created:
                print(f"Usuario creado: {email}")
            else:
                print(f"Usuario actualizado: {email}")

        except KeyError as e:
            print(f"Error: Falta la clave {e} en el registro {record}")
        except Exception as e:
            print(f"Error procesando el registro {record}: {e}")

# Ruta al archivo JSON
json_path = r"D:\\ProyectoDjango\\POS3\\pospython\\Data\\data.json"

# Ejecutar el procesamiento del JSON
process_json(json_path)