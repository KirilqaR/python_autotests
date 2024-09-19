import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '11bfd2181ef2dbba5ae2521183e58d06'
HEADER = {'Content-Type': 'application/json', 'trainer_token': TOKEN}

body_create = {
    "name": "ПайтозаврикТретий",
    "photo_id": -1
}

body_rename = {
    "pokemon_id": "72714",
    "name": "Даунбрейкер",
    "photo_id": 958
}

body_catch = {
    "pokemon_id": "72714"
}

'''response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)'''

# id_pokemon = response_create.json()['id'] - думал здесь сразу сделать замену имени, но Пайтон ругается, так как все переменные у нас заполняются до выполнения запросов :( 

'''response_rename = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_rename)
print(response_rename.text)'''

response_catch = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_catch)
print(response_catch.text)