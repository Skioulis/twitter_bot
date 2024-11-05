import os
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.common import NoSuchElementException, InvalidSelectorException

from InternetSpeedTwitterBot import InternetSpeedTwitterBot


from dotenv import load_dotenv

PROMISED_DOWN = 90
PROMISED_UP = 9
CHROME_DRIVER_PATH="C:\\Users\\skiou"
URL = "https://tinder.com/"
load_dotenv(dotenv_path=".venv/.env")
username=os.getenv("mail")
password = os.getenv("password")



bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()

