import requests
import pytest

URL = 'https://api.pokemonbattle.me:9104'
header = {
    "Content-Type": "application/json",
    "trainer_token": "5d30e4bb6f6aedf31c4ce25287cb629e"
}

def test_get_trainers_level():
    """
    TEST-1 GET Trainers status
    """
    response=requests.get(url =f'{URL}/trainers', params={'level': 1}, headers=header, timeout=5)
    assert response.status_code == 200, 'Status code is NOT ok'
    

def test_get_trainers_id():
    """
    TEST-2 GET Trainers name
    """
    response=requests.get(url =f'{URL}/trainers', params={'trainer_id': 3869}, headers=header, timeout=5)
    assert response.json()['trainer_name'] == 'BIT'