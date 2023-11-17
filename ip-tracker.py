import requests
import phonenumbers
from phonenumbers import geocoder, carrier
import os

os.system("clear")

print("")

print("  _____                           _  _                       ")
print(" /  __ \                         (_)| |                      ")
print(" | /  \/  ___   _ __ ___   _ __   _ | | ______   __ _  _ __  ")
print(" | |     / _ \ | '_ ` _ \ | '_ \ | || ||______| / _` || '__| ")
print(" | \__/\| (_) || | | | | || |_) || || |        | (_| || |    ")
print("  \____/ \___/ |_| |_| |_|| .__/ |_||_|         \__,_||_|    ")
print("                         | |                                ")
print("                         |_|                                ")
print("                                                            ")
print("              https://github.com/Compil-AR                  ")


def main():
    while True:
        print("\n1. Geolocalizar IP")
        print("2. Información de numero de telefono")
        print("3. Salir")
        
        opcion = input("Seleccione una opcion: ")
        
        if opcion == "1":
            geolocalizar_ip()
        elif opcion == "2":
            info_telefono()
        elif opcion == "3":
            break

def geolocalizar_ip():
    direccion_ip = input("Introduzca la direccion IP: ")
    datos = obtener_datos_ip(direccion_ip)
    for clave, valor in datos.items():
        print(f'{clave}: {valor}')

def obtener_datos_ip(ip):
    try:
        respuesta = requests.get(f'http://ip-api.com/json/{ip}')
        respuesta.raise_for_status()
        data = respuesta.json()
        return {
            'País': data.get('country', 'Desconocido'),
            'Ciudad': data.get('city', 'Desconocido'),
            'Latitud': data.get('lat', 'Desconocido'),
            'Longitud': data.get('lon', 'Desconocido')
        }
    except requests.RequestException:
        return {'Error': 'No se pudo obtener la información'}

def info_telefono():
    pais = input("Introduzca el codigo del país (sin +): ")
    numero = input("Introduzca el numero: ")
    datos = obtener_datos_telefono(pais, numero)
    for clave, valor in datos.items():
        print(f'{clave}: {valor}')

def obtener_datos_telefono(pais, numero):
    try:
        numero_completo = '+' + pais + numero
        telefono = phonenumbers.parse(numero_completo)
        return {
            'Numero valido': phonenumbers.is_valid_number(telefono),
            'Numero posible': phonenumbers.is_possible_number(telefono),
            'Numero formateado': phonenumbers.format_number(telefono, phonenumbers.PhoneNumberFormat.E164),
            'Geolocalizacion': geocoder.description_for_number(telefono, "es"),
            'Operador': carrier.name_for_number(telefono, "es")
        }
    except Exception as e:
        return {'Error': str(e)}

if __name__ == "__main__":
    main()
