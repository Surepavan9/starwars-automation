import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MoviePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "http://localhost:3000/"

    def open(self):
        self.driver.get(self.url)

    def sort_by_title(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@class='pl-2 pr-5 px-3']"))
        ).click()

    def get_last_movie_title(self):
        return self.driver.find_elements(By.XPATH, "//a[@class='underline font-medium']")[-1].text

    def view_movie(self, title):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f"//a[text()='{title}']"))
        ).click()

    def get_species_list(self):
        time.sleep(10)
        species_section = self.driver.find_element(By.XPATH, "/html/body/section/main/div[2]/div[3]/ul")
        return [el.text.strip() for el in species_section.find_elements(By.TAG_NAME, "li")]

    def get_planets_list(self):
        planets_section = self.driver.find_element(By.XPATH, "//*[@class='border-2 border-white rounded px-5 pt-3 m-5'][2]//ul")
        return [el.text.strip() for el in planets_section.find_elements(By.TAG_NAME, "li")]

