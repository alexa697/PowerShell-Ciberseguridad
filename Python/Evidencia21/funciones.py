import os
import getpass
import requests
import logging
import csv
import argparse


# =========================
# 1. API KEY
# =========================
def obtener_api_key():
    if not os.path.exists("apikey.txt"):
        print("No se encontró el archivo apikey.txt.")
        clave = getpass.getpass("Ingresa tu API key: ")

        with open("apikey.txt", "w") as archivo:
            archivo.write(clave.strip())

        print("API key guardada correctamente.")
    else:
        with open("apikey.txt", "r") as archivo:
            clave = archivo.read().strip()

        print("API key cargada desde el archivo.")

    return clave


# =========================
# 2. ARGPARSE
# =========================
def obtener_argumentos():
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--correo", help="Correo electrónico")

    args = parser.parse_args()

    if not args.correo:
        args.correo = input("Ingresa el correo: ")

    return args


# =========================
# 3. CONSULTAR BRECHAS
# =========================
def consultar_brechas(correo, clave):
    url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{correo}"

    headers = {
        "hibp-api-key": clave,
        "User-Agent": "Evidencia20/1.0",
        "Accept": "application/json"
    }

    response = requests.get(url, headers=headers)

    return response


# =========================
# 4. DETALLE DE BRECHAS
# =========================
def obtener_detalles_brechas(response, correo):
    if response.status_code == 200:
        brechas = response.json()

        logging.info(
            f"Consulta exitosa para {correo}. "
            f"Brechas encontradas: {len(brechas)}"
        )
        return brechas

    if response.status_code == 404:
        logging.info(
            f"Consulta exitosa para {correo}. "
            "No se encontraron brechas."
        )
        return []

    if response.status_code == 401:
        logging.error("Error 401: API key inválida.")
        return []

    logging.error(
        f"Error inesperado. Código de estado: {response.status_code}"
    )
    return []


# =========================
# 5. GENERAR CSV
# =========================
def generar_csv(brechas, clave, correo):
    archivo_existe = os.path.exists("reporte.csv")
    
    with open("reporte.csv", "a", newline='', encoding="utf-8") as archivo_csv:
        writer = csv.writer(archivo_csv)
        
        if not archivo_existe:
            writer.writerow([
                "Correo","Title", "Domain", "BreachDate",
                "DataClasses", "IsVerified", "IsSensitive"
                ])
        
        for brecha in brechas[:3]:
            nombre = brecha.get("Name") or brecha.get("Title")

        detalle = obtener_detalle_brecha(nombre, clave)

        if detalle:
                writer.writerow([
                    detalle.get("Title", "N/A"),
                    detalle.get("Domain", "N/A"),
                    detalle.get("BreachDate", "N/A"),
                    ", ".join(detalle.get("DataClasses", [])),
                    detalle.get("IsVerified", "N/A"),
                    detalle.get("IsSensitive", "N/A")
                ])
  
# =========================
# 6. LOGGING
# =========================
def configurar_logging():
    logging.basicConfig(
        filename="registro.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

#7. Funcion para obtener info de todas las brechas
def obtener_detalle_brecha(nombre, clave):
    url = f"https://haveibeenpwned.com/api/v3/breach/{nombre}"

    headers = {
        "hibp-api-key": clave,
        "User-Agent": "Evidencia20/1.0",
        "Accept": "application/json"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()

    return None
