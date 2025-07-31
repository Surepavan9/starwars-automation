import requests

BASE_URL = "https://swapi.info/api/films"


def test_movies_count_should_be_6():
    response = requests.get(BASE_URL)
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 6


def test_director_of_3rd_movie():
    response = requests.get(BASE_URL)
    data = response.json()
    third_movie = data[2]
    assert third_movie["director"] == "Richard Marquand"


def test_producers_of_5th_movie_not_expected():
    response = requests.get(BASE_URL)
    data = response.json()
    fifth_movie = data[4]
    assert fifth_movie["producer"] != "Gary Kurtz, George Lucas"
