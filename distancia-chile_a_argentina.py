def obtener_distancia_duracion(ciudad_origen, ciudad_destino):
    # Distancias aproximadas entre Santiago de Chile y algunas ciudades de Argentina
    distancias = {
        ('santiago', 'buenos aires'): {'distancia_km': 1150, 'duracion': '1 día'},
        ('santiago', 'mendoza'): {'distancia_km': 360, 'duracion': '5 horas'},
        ('santiago', 'bariloche'): {'distancia_km': 1100, 'duracion': '13 horas'}
    }
    
    # Convertimos las ciudades a minúsculas para ser insensibles a mayúsculas/minúsculas
    ciudad_origen = ciudad_origen.lower()
    ciudad_destino = ciudad_destino.lower()
    
    # Buscamos la distancia y duración aproximada en la base de datos simulada
    clave = (ciudad_origen, ciudad_destino)
    if clave in distancias:
        distancia_km = distancias[clave]['distancia_km']
        duracion = distancias[clave]['duracion']
        distancia_millas = distancia_km * 0.621371  # 1 kilómetro = 0.621371 millas
        return distancia_millas, distancia_km, duracion
    else:
        return None, None, None

def main():
    print("Bienvenido al sistema de cálculo de viaje.")
    while True:
        ciudad_origen = input("Ingrese la ciudad de origen (Santiago): ").strip().lower()
        ciudad_destino = input("Ingrese la ciudad de destino (Buenos Aires, Mendoza, Bariloche): ").strip().lower()
        
        if ciudad_origen == 's' or ciudad_destino == 's':
            print("Saliendo del programa...")
            break
        
        distancia_millas, distancia_km, duracion = obtener_distancia_duracion(ciudad_origen, ciudad_destino)
        
        if distancia_km and duracion:
            print(f"\nLa distancia entre {ciudad_origen.capitalize()} y {ciudad_destino.capitalize()} es:")
            print(f"{distancia_millas:.2f} millas")
            print(f"{distancia_km} kilómetros")
            print(f"La duración estimada del viaje es de {duracion}.")
            
            # Narrativa del viaje
            print(f"\nNarrativa del viaje desde {ciudad_origen.capitalize()} a {ciudad_destino.capitalize()}:")
            print(f"Saldrás desde {ciudad_origen.capitalize()} y llegarás a {ciudad_destino.capitalize()} después de {duracion} de viaje.")
            
            # Opciones de medio de transporte
            print("\nOpciones de medio de transporte:")
            print("1. Avión")
            print("2. Automóvil")
            print("3. Autobús")
        
        else:
            print("No se pudo obtener la información para las ciudades ingresadas. Inténtelo de nuevo.")
        
        print("\n---\n")

if __name__ == "__main__":
    main()

