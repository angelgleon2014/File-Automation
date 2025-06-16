import chardet

def detectar_codificacion(file_path):
    with open(file_path, 'rb') as f:
        raw_data = f.read()
        resultado = chardet.detect(raw_data)
        print(f"Codificación detectada: {resultado['encoding']}")
        return resultado['encoding']

# Cambia la ruta a la de tu archivo JSON
# file_path = 'D:\\ProyectoDjango\\POS3\\pospython\\Data\\nuevo61.json'
file_path = 'D:\\ProyectoDjango\\POS3\\pospython\\Data\\data.json'
detectar_codificacion(file_path)
