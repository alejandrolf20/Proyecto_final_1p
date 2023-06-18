import requests
import json

print("Bienvenido a la API de la NBA.")
print("Este es el ejercicio 1, que mostrará el top de equipos de la NBA.")
print("¡Comencemos!")
print("------------------------------------------------------------")

url = 'https://api-nba-v1.p.rapidapi.com/teams'
headers = {
    'x-rapidapi-host': 'api-nba-v1.p.rapidapi.com',
    'x-rapidapi-key': 'e1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p'
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    teams = data['api']['teams']
    
    print("Top de equipos de la NBA:")
    for team in teams:
        team_id = team['teamId']
        team_name = team['fullName']
        print(f"Equipo ID: {team_id}, Nombre: {team_name}")
else:
    print(f"Error al obtener los equipos. Código de error: {response.status_code} - {response.text}")

print("¡Eso es todo! Gracias por utilizar la API de la NBA.")