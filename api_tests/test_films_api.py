import requests
import pytest

BASE_URL = "https://swapi.dev/api/films/"

def test_films_count():
    response = requests.get(BASE_URL)
    assert response.status_code == 200
    data = response.json()
    assert data["count"] == 6

def test_film_director_names():
    response = requests.get(BASE_URL)
    films = response.json().get("results", [])
    for film in films:
        assert film["director"] == "George Lucas"

def test_producer_list_includes():
    response = requests.get(BASE_URL)
    films = response.json().get("results", [])
    for film in films:
        assert "Gary Kurtz" in film["producer"]

def test_invalid_planet_in_film():  # Negative case
    response = requests.get(BASE_URL)
    film = response.json()["results"][0]
    assert "InvalidPlanet" not in film.get("planets", [])
