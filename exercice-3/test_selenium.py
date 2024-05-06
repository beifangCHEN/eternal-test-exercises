from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep
import sys

import ws_util

BASE_URL = f"http://localhost:{ws_util.TEST_PORT}"
TASKS_URL = "/tasks"
ALL_TASKS_URL = "/all_tasks"

# lancer les tests en commençant par start_webserver() et en finissant par teardown_webserver()
def test_counter_website():
  ws_util.start_webserver()
  try:
    driver = webdriver.Firefox()
    driver.get(f"{BASE_URL}/test.html")
    sleep(2)
    counterButton = driver.find_element(By.XPATH, "//*[text()='Click me!']")
    resetButton = driver.find_element(By.XPATH, "//*[text()='Reset!']")
    counterText = driver.find_element(By.ID, 'counter')
    historiqueText = driver.find_element(By.ID, 'historique')
    for i in range(0, 10):
      counterButton.click()
      assert counterText.text == str(i + 1)
      sleep(0.1)
    assert counterText.text == "10"
    resetButton.click()
    # le texte du compteur doit être de nouveau 0
    assert counterText.text == "0"
    # l'historique doit avoir la valeur 10 à sa fin
    assert historiqueText.text.endswith(" 10")
    for i in range(0, 5):
      counterButton.click()
    assert counterText.text == "5"
    resetButton.click()
    assert historiqueText.text.endswith(" 5")
    sleep(2)
  except AssertionError: #pragma: no cover
    # let pytest errors move forward
    raise
  except: #pragma: no cover
    if driver is None:
      ws_util.teardown_webserver() 
      sys.exit(1)
  finally:
    sleep(2)
    driver.quit()
    ws_util.teardown_webserver() 