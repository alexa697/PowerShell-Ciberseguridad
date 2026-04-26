import os
import getpass

# Verificar si existe el archivo
if not os.path.exists("apikey.txt"):
    print("No se encontró el archivo apikey.txt.")
    
    # Pedir la API key sin mostrarla
    clave = getpass.getpass("Ingresa tu API key: ")
    
    # Guardarla en el archivo
    with open("apikey.txt", "w") as archivo:
        archivo.write(clave.strip())
    
    print("API key guardada correctamente.")

else:
    # Si el archivo ya existe, leer la clave
    with open("apikey.txt", "r") as archivo:
        clave = archivo.read().strip()
    
    print("API key cargada desde el archivo.")
