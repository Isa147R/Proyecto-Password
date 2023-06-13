import random
import string
import tkinter as tk
import tkinter.messagebox as messagebox

# Importar módulo adicional para copiar al portapapeles
import pyperclip

def generar_contraseña(longitud, caracteres):
    tipos_caracteres = {
        "mayusculas": string.ascii_uppercase,
        "minusculas": string.ascii_lowercase,
        "numeros": string.digits,
        "simbolos": string.punctuation
    }

    caracteres_disponibles = ""
    for tipo in caracteres:
        caracteres_disponibles += tipos_caracteres.get(tipo, '')

    contraseña = ''.join(random.choice(caracteres_disponibles) for _ in range(longitud))
    return contraseña

def generar_contraseña_interfaz():
    # Obtener los valores de los widgets de entrada
    longitud = int(entry_longitud.get())

    # Verificar los botones seleccionados
    caracteres = []
    if var_mayusculas.get() == 1:
        caracteres.append("mayusculas")
    if var_minusculas.get() == 1:
        caracteres.append("minusculas")
    if var_numeros.get() == 1:
        caracteres.append("numeros")
    if var_simbolos.get() == 1:
        caracteres.append("simbolos")

    # Generar la contraseña
    contraseña_generada = generar_contraseña(longitud, caracteres)

    # Actualizar la etiqueta con la contraseña generada
    etiqueta_contraseña.config(text="Contraseña generada: " + contraseña_generada)

    # Copiar al portapapeles
    pyperclip.copy(contraseña_generada)
    messagebox.showinfo("Generador de Contraseñas", "Contraseña copiada al portapapeles")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Generador de Contraseñas")

# Crear los widgets
etiqueta_longitud = tk.Label(ventana, text="Longitud de la contraseña:")
etiqueta_longitud.pack()

entry_longitud = tk.Entry(ventana)
entry_longitud.pack()

etiqueta_caracteres = tk.Label(ventana, text="Selecciona los tipos de caracteres:")
etiqueta_caracteres.pack()

var_mayusculas = tk.IntVar()
var_minusculas = tk.IntVar()
var_numeros = tk.IntVar()
var_simbolos = tk.IntVar()

check_mayusculas = tk.Checkbutton(ventana, text="Mayúsculas", variable=var_mayusculas)
check_mayusculas.pack()

check_minusculas = tk.Checkbutton(ventana, text="Minúsculas", variable=var_minusculas)
check_minusculas.pack()

check_numeros = tk.Checkbutton(ventana, text="Números", variable=var_numeros)
check_numeros.pack()

check_simbolos = tk.Checkbutton(ventana, text="Símbolos", variable=var_simbolos)
check_simbolos.pack()

boton_generar = tk.Button(ventana, text="Generar Contraseña", command=generar_contraseña_interfaz)
boton_generar.pack()

etiqueta_contraseña = tk.Label(ventana, text="")
etiqueta_contraseña.pack()

# Iniciar el bucle de eventos de la ventana
ventana.mainloop()
