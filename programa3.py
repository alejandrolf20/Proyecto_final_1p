import requests
import json

print("Bienvenido a la API de la NBA.")
print("Este es el ejercicio 3, que mostrará los partidos programados para un equipo específico.")
print("¡Comencemos!")
print("------------------------------------------------------------")

team_id = input("Introduce el ID del equipo de la NBA: ")

url = f"https://api-nba-v1.p.rapidapi.com/games/{team_id}"
headers = {
    'x-rapidapi-host': 'api-nba-v1.p.rapidapi.com',
    'x-rapidapi-key': 'e1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p'
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    games = data['api']['games']
    
    print("Partidos programados:")
    for game in games:
        game_id = game['gameId']
        start_time = game['startTimeUTC']
        home_team = game['hTeam']['fullName']
        visitor_team = game['vTeam']['fullName']
        
        print(f"ID de juego: {game_id}")
        print(f"Fecha y hora de inicio: {start_time}")
        print(f"Equipo local: {home_team}")
        print(f"Equipo visitante: {visitor_team}")
        print("------------------------------------")
else:
    print(f"Error al obtener los partidos. Código de error: {response.status_code} - {response.text}")

print("¡Eso es todo! Gracias por utilizar la API de la NBA.")