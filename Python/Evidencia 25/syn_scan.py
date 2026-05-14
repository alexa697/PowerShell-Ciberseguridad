from scapy.all import IP, TCP, sr

import csv



# Lee las IPs desde el archivo generado por el escaneo ARP

with open("arp_hosts.txt") as archivo:

    hosts = [line.split(",")[0] for line in archivo]



# Define los puertos a escanear

puertos = [22, 80, 443]

resultados = []



print("Iniciando escaneo SYN de puertos…")

 

for ip in hosts:

    abiertos = []

    for puerto in puertos:

        paquete = IP(dst=ip) / TCP(dport=puerto, flags="S")

        respuesta, _ = sr(paquete, timeout=1, verbose=0)

        if respuesta:

            abiertos.append(puerto)



    print(f"{ip} → Puertos abiertos: {abiertos}")

    resultados.append((ip, abiertos))



# Guarda los resultados en un archivo CSV

with open("syn_scan.csv", "w", newline="") as archivo:

    writer = csv.writer(archivo)

    writer.writerow(["IP"] + [str(p) for p in puertos])



    for ip, abiertos in resultados:

        fila = [ip] + [("Sí" if p in abiertos else "No") for p in puertos]

        writer.writerow(fila)



print("Resultados guardados en syn_scan.csv")