import os
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.common import NoSuchElementException, InvalidSelectorException
from selenium.webdriver.common.by import By


from dotenv import load_dotenv

PROMISED_DOWN = 90
PROMISED_UP = 9
CHROME_DRIVER_PATH="C:\\Users\\skiou"
URL = "https://tinder.com/"

load_dotenv(dotenv_path=".venv/.env")
username=os.getenv("mail")
password = os.getenv("password")

def driver_initialization (url : str):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)
    chrome_options.add_argument("--start-maximized")

    inner_driver = webdriver.Chrome(options=chrome_options)
    inner_driver.get(url)
    return inner_driver

driver = driver_initialization(URL)

