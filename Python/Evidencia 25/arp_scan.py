from scapy.all import (srp, Ether, ARP)


# Define el rango de IPs de tu red local

rango_red = "192.168.1.0/24"



# Construye el paquete ARP dentro de un paquete Ethernet

paquete = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=rango_red)



print(f"Escaneando red local: {rango_red}")

respuestas, _ = srp(paquete, timeout=3, verbose=0)



# Procesa las respuestas

hosts = []

for _, respuesta in respuestas:

    ip = respuesta.psrc

    mac = respuesta.hwsrc

    hosts.append((ip, mac))

    print(f"Host encontrado → IP: {ip} | MAC: {mac}")



# Guarda los resultados en un archivo

with open("arp_hosts.txt", "w") as archivo:

    for ip, mac in hosts:

        archivo.write(f"{ip},{mac}\n")



print("Resultados guardados en arp_hosts.txt")
