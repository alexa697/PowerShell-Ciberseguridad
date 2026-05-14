import os
import stat
import base64
import getpass
import shodan


def obtener_api_key():
    ruta = os.path.expanduser("~/.shodan_key")
    if os.path.exists(ruta):
        with open(ruta, "rb") as f:
            encoded = f.read().strip()
        return base64.b64decode(encoded).decode("utf-8")
    else:
        key = getpass.getpass("Ingresa tu Shodan API Key: ")
        encoded = base64.b64encode(key.encode("utf-8"))
        with open(ruta, "wb") as f:
            f.write(encoded)
        try:
            os.chmod(ruta, stat.S_IREAD | stat.S_IWRITE)
        except Exception:
            pass
        print(f"Clave guardada en: {ruta}")
        return key


def main():
    API_KEY = obtener_api_key()
    api = shodan.Shodan(API_KEY)

    consulta = 'port:25 country:MX "250 OK" "220" -smtp.auth -smtp.starttls'
    print(f"\n🔍 Ejecutando búsqueda: {consulta}\n")

    try:
        resultados = api.search(consulta)
        total = resultados.get("total", 0)
        print(f"Resultados encontrados: {total}\n")

        with open("smtp_spoofable_mx.txt", "w", encoding="utf-8") as out:
            for match in resultados.get("matches", []):
                ip = match.get("ip_str")
                org = match.get("org", "Desconocida")
                banner = match.get("data", "").strip().replace("\n", " ")
                linea = f"{ip} | {org} | {banner[:80]}..."
                print(" -", linea)
                out.write(linea + "\n")

        print("\nResultados guardados en smtp_spoofable_mx.txt")

    except shodan.APIError as e:
        print(f"Error en la consulta a Shodan: {e}")

if __name__ == "__main__":
    main()
