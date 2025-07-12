import requests

API_KEY = "9db573cc-e062-40b5-b09b-63cb81695fe2"

def obtener_coordenadas(ciudad):
    url = "https://graphhopper.com/api/1/geocode"
    params = {
        "q": ciudad,
        "locale": "es",
        "limit": 1,
        "key": API_KEY
    }
    response = requests.get(url, params=params)
    if response.status_code != 200:
        print("Error al obtener coordenadas:", response.text)
        return None

    resultados = response.json()["hits"]
    if not resultados:
        print("No se encontraron resultados para:", ciudad)
        return None

    punto = resultados[0]
    return f"{punto['point']['lat']},{punto['point']['lng']}"

def calcular_ruta(origen, destino, medio):
    coord_origen = obtener_coordenadas(origen)
    coord_destino = obtener_coordenadas(destino)

    if not coord_origen or not coord_destino:
        return

    url = "https://graphhopper.com/api/1/route"
    params = {
        "point": [coord_origen, coord_destino],
        "vehicle": medio,
        "locale": "es",
        "instructions": "true",
        "calc_points": "true",
        "key": API_KEY
    }

    response = requests.get(url, params=params)
    if response.status_code != 200:
        print("Error en la consulta:", response.text)
        return

    data = response.json()
    path = data["paths"][0]

    distancia_km = path["distance"] / 1000
    distancia_mi = distancia_km * 0.621371
    duracion_min = path["time"] / 60000
    instrucciones = path["instructions"]

    print(f"Distancia: {distancia_km:.2f} km / {distancia_mi:.2f} mi")
    print(f"Duración estimada: {duracion_min:.2f} minutos")
    print("Narrativa del viaje:")
    for paso in instrucciones:
        print("-", paso['text'])

# Bucle principal
while True:
    origen = input("Ingrese la ciudad de origen en Chile (o 's' para salir): ")
    if origen.lower() == 's':
        break

    destino = input("Ingrese la ciudad de destino en Perú (o 's' para salir): ")
    if destino.lower() == 's':
        break

    medio = input("Ingrese el medio de transporte (car, bike, foot): ").lower()
    if medio not in ["car", "bike", "foot"]:
        print("Medio de transporte no válido. Intente con: car, bike, foot.")
        continue

    calcular_ruta(origen, destino, medio)
    print("")
