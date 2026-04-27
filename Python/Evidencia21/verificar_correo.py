from funciones import *

configurar_logging()

args = obtener_argumentos()
clave = obtener_api_key()

response = consultar_brechas(args.correo, clave)
brechas = obtener_detalles_brechas(response, args.correo)

generar_csv(brechas, clave, args.correo)