import requests

URL = 'https://api.pokemonbattle.me:9104'
header = {
    "Content-Type": "application/json",
    "trainer_token": "5d30e4bb6f6aedf31c4ce25287cb629e"
}

body = {
    "name": "generate",
    "photo": "generate"
}

response=requests.post(url =f'{URL}/pokemons', json=body, headers=header, timeout=5)
print(f'Статус код: {response.status_code}. Сообщение: {response.text}')

body_rqst_name = {
    "pokemon_id": "28402",
    "name": "New Name",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
}

response=requests.put(url =f'{URL}/pokemons', json=body_rqst_name, headers=header, timeout=5)
print(f'Статус код: {response.status_code}. Сообщение: {response.text}')

body_rqst_add = {
    "pokemon_id": "28408"
}

response=requests.post(url =f'{URL}/trainers/add_pokeball', json=body_rqst_add, headers=header, timeout=5)
print(f'Статус код: {response.status_code}. Сообщение: {response.text}')


response=requests.get(url =f'{URL}/trainers', params={'trainer_id': 3869}, headers=header, timeout=5)
print(f'Статус код: {response.status_code}. Сообщение: {response.text}')