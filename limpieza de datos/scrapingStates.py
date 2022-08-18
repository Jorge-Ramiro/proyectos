from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import re

def init_scrapper(headless = True):
    
    # Inicializar el webdriver
    options = webdriver.ChromeOptions()

    if headless: options.add_argument('headless')

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    URL = "https://es.wikipedia.org/wiki/Estado_de_los_Estados_Unidos#Lista_de_estados"
    driver.get(URL) # Hace la petición de la url y mostranosla

    return driver


def get_state(slp_time):
    
    driver = init_scrapper()
    time.sleep(2*slp_time)
    states_abrev = {}
    tbody = driver.find_elements(By.TAG_NAME, "tbody")[1]
    for tr in tbody.find_elements(By.TAG_NAME, 'tr'):
        state = tr.find_elements(By.TAG_NAME, 'td')[0].text
        abrev = tr.find_elements(By.TAG_NAME, 'td')[3].text
        states_abrev[abrev] = re.sub(r'[0-9]+', '', state)
    
    return states_abrev


if __name__ == '__main__':
    slp_time = 4
    states = get_state(slp_time)
    print(states)