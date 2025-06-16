import chardet
def convertir_a_ISO(input_file, output_file):
    # Detectar codificación del archivo original
    with open(input_file, 'rb') as f:
        raw_data = f.read()
        resultado = chardet.detect(raw_data)
        encoding_detectada = resultado['encoding']
        print(f"Convirtiendo desde: {encoding_detectada}")

    # Leer archivo con la codificación detectada
    with open(input_file, 'r', encoding=encoding_detectada, errors='ignore') as f:
        contenido = f.read()

    # Guardar archivo convertido a UTF-8
    with open(output_file, 'w', encoding='ISO-8859-1') as f:
        f.write(contenido)
        print(f"Archivo convertido a ISO-8859-1: {output_file}")

input_file = 'D:\\ProyectoDjango\\POS3\\pospython\\Data\\data.json'
output_file = 'D:\\ProyectoDjango\\POS3\\pospython\\Data\\data_ISO-8859-1.json'
convertir_a_ISO(input_file, output_file)