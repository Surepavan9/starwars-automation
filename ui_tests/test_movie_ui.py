import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("http://localhost:3000")  # adjust if using a different port
    yield driver
    driver.quit()

def test_movie_titles_visible(driver):
    titles = driver.find_elements(By.CLASS_NAME, "movie-title")
    assert len(titles) >= 6

def test_movie_click_shows_details(driver):
    driver.find_elements(By.CLASS_NAME, "movie-title")[0].click()
    detail_title = driver.find_element(By.ID, "movie-detail-title").text
    assert "Episode" in detail_title
