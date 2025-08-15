import re

#colección de url's ej: "https://drive.google.com/file/d/1qNn227KlbPsbN92jbXZW6O9U2rzwbhlc/view?usp=sharing", importante poner "," al final de cada array, todas van dentro de los corchetes []
urls = [
    #ingresa tus url's aquí
]

ids = []
invalidas = []

for url in urls:
    match = re.search(r'/d/([^/]+)/', url)
    if match:
        ids.append(match.group(1))
    else:
        invalidas.append(url)

# validación de longitud
if ids:
    longitudes = {len(i) for i in ids}
    if len(longitudes) == 1:
        print(f"Todos los IDs tienen {longitudes.pop()} caracteres")
    else:
        print("No todos los IDs tienen la misma longitud")
        for i in ids:
            print(f"{i} → {len(i)} caracteres")

# mostrar url's que no cumplen con el formato (encontradas)
if invalidas:
    print("\n URLs que no cumplen el formato esperado:")
    for url in invalidas:
        print(url)

print("\nIDs extraídos:", ids)

#revisa la consola para obtener tus urls 
