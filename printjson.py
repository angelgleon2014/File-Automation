import json

def cargar_json(file_path):
    try:
        with open(file_path, 'rb') as f:
            contenido = f.read().decode('utf-8', errors='ignore')
        data = json.loads(contenido)
        return data
    except json.JSONDecodeError as e:
        print(f"Error al decodificar JSON: {e}")
        return None

file_path = 'D:\\ProyectoDjango\\POS3\\pospython\\Data\\data.json'
usuarios = cargar_json(file_path)

if usuarios:
    for usuario in usuarios:
        print(f"Usuario: {usuario['name']} {usuario['lastname']}, Email: {usuario['email']}, Fecha de nacimiento: {usuario['BIRTHDAY']}, Fecha de inicio: {usuario['acc_startdate']}, Fecha de fin: {usuario['acc_enddate']}, Número de tarjeta: {usuario['CardNo']}, ID de usuario: {usuario['USERID']}, Dirección: {usuario['street']}, Fecha de registro: {usuario['HIREDDAY']}")
