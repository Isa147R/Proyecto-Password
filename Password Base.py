import random
import string

def generar_contraseña(longitud, caracteres):
    # Define los tipos de caracteres disponibles
    tipos_caracteres = {
        "mayusculas": string.ascii_uppercase,
        "minusculas": string.ascii_lowercase,
        "numeros": string.digits,
        "simbolos": string.punctuation
    }

    # Combina los tipos de caracteres seleccionados por el usuario
    caracteres_disponibles = ""
    for tipo in caracteres:
        caracteres_disponibles += tipos_caracteres.get(tipo, '')

    # Genera la contraseña aleatoria
    contraseña = ''.join(random.choice(caracteres_disponibles) for _ in range(longitud))
    return contraseña

# Solicita la longitud de la contraseña al usuario
longitud = int(input("Longitud de la contraseña: "))

# Solicita los tipos de caracteres al usuario
print("Tipos de caracteres disponibles:")
print("1. Mayúsculas")
print("2. Minúsculas")
print("3. Números")
print("4. Símbolos")
opciones = {
    "1": "mayusculas",
    "2": "minusculas",
    "3": "numeros",
    "4": "simbolos"
}
seleccion = input("Selecciona los tipos de caracteres (separa por comas): ")
caracteres = [opciones.get(opcion) for opcion in seleccion.split(',')]

# Genera la contraseña
contraseña_generada = generar_contraseña(longitud, caracteres)

# Muestra la contraseña generada
print("Contraseña generada:", contraseña_generada)

