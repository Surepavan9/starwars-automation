import time

import pytest
from selenium import webdriver
from pages.movie_page import MoviePage


class TestMoviePageUI:

    @pytest.fixture()
    def driver(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        yield driver
        driver.quit()

    def test_sort_movies_and_validate_last_title(self, driver):
        page = MoviePage(driver)
        page.open()
        page.sort_by_title()
        assert page.get_last_movie_title() == "The Phantom Menace"

    def test_species_list_has_wookie(self, driver):
        page = MoviePage(driver)
        page.open()
        page.view_movie("The Empire Strikes Back")
        species = page.get_species_list()
        assert "Wookie" in species

    def test_planet_camino_not_in_phantom_menace(self, driver):
        page = MoviePage(driver)
        page.open()
        page.view_movie("The Phantom Menace")
        time.sleep(5)
        planets = page.get_planets_list()
        assert "Camino" not in planets
