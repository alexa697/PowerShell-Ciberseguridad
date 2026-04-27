import os
import getpass
import requests
import time
import logging
import csv


# =========================
# API KEY
# =========================
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


# =========================
# LOGGING
# =========================
logging.basicConfig(
    filename="registro.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


# =========================
# CONSULTA API
# =========================
correo = input("Ingresa el correo electrónico a consultar: ")

url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{correo}"

headers = {
    "hibp-api-key": clave,
    "User-Agent": "Evidencia20/1.0",
    "Accept": "application/json"
}

response = requests.get(url, headers=headers)


# =========================
# MANEJO DE RESPUESTA
# =========================
if response.status_code == 200:
    brechas = response.json()

    if brechas:
        logging.info(
            f"Consulta exitosa para {correo}. "
            f"Brechas encontradas: {len(brechas)}"
        )
    else:
        logging.info(
            f"Consulta exitosa para {correo}. "
            "No se encontraron brechas."
        )

elif response.status_code == 404:
    brechas = []
    logging.info(
        f"Consulta exitosa para {correo}. "
        "No se encontraron brechas."
    )

elif response.status_code == 401:
    brechas = []
    logging.error("Error 401: API key inválida o no autorizada.")

else:
    brechas = []
    logging.error(
        f"Error inesperado. Código de estado: {response.status_code}"
    )


# =========================
# CSV (solo si hay lista válida)
# =========================
if isinstance(brechas, list):
    with open("reporte.csv", "w", newline='', encoding="utf-8") as archivo_csv:
        writer = csv.writer(archivo_csv)

        writer.writerow([
            "Title", "Domain", "BreachDate",
            "DataClasses", "IsVerified", "IsSensitive"
        ])

        for brecha in brechas[:3]:
            time.sleep(10)

            writer.writerow([
                brecha.get("Title"),
                brecha.get("Domain"),
                brecha.get("BreachDate"),
                ", ".join(brecha.get("DataClasses", [])),
                brecha.get("IsVerified"),
                brecha.get("IsSensitive")
            ])