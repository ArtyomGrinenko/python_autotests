import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '51b9cb0653299e8f51ec820cee8012dc'
HEADER = {'Content-Type' : 'application/json', 'trainer_token':TOKEN}
TRAINER_ID = 23560

def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200
