import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '51b9cb0653299e8f51ec820cee8012dc'
HEADER = {'Content-Type' : 'application/json', 'trainer_token':TOKEN} 

# Создание покемона

body_create = {
    "name": "Ностромо",
    "photo_id": 3
}

response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create) 
print(response_create.text)

# Изменить имя покемону

body_rename = {
    "pokemon_id": "271339",
    "name": "Ностромон",
    "photo_id": 3
}
response_rename = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_rename)
print(response_rename.text)

# Поймать покемона в покебол

body_capture = {
    "pokemon_id": "271339",
}

response_capture = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_capture)
print(response_capture.text)







