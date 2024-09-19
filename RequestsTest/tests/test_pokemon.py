import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
HEADER = {'Content-Type': 'application/json'}
TRAINER_ID = '5140'

def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200

def test_trainer_id():
    response_id = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response_id.json()['data'][0]['id'] == '5140'