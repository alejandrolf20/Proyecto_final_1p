import requests
import json

print("Bienvenido a la API de la NBA.")
print("Este es el ejercicio 2, que mostrará información sobre un jugador específico.")
print("¡Comencemos!")
print("------------------------------------------------------------")

player_id = input("Introduce el ID del jugador de la NBA: ")

url = f"https://api-nba-v1.p.rapidapi.com/players/{player_id}"
headers = {
    'x-rapidapi-host': 'api-nba-v1.p.rapidapi.com',
    'x-rapidapi-key': 'e1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p'
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    player = data['api']['players'][0]
    
    player_name = player['firstName'] + " " + player['lastName']
    team_name = player['teamName']
    position = player['position']
    height_feet = player['heightFeet']
    height_inches = player['heightInches']
    
    print("Información del jugador:")
    print(f"Nombre: {player_name}")
    print(f"Equipo: {team_name}")
    print(f"Posición: {position}")
    print(f"Altura: {height_feet} pies {height_inches} pulgadas")
else:
    print(f"Error al obtener información del jugador. Código de error: {response.status_code} - {response.text}")

print("¡Eso es todo! Gracias por utilizar la API de la NBA.")