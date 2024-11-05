from selenium import webdriver
from selenium.common import NoSuchElementException, InvalidSelectorException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
from os import getenv
from time import sleep

load_dotenv(dotenv_path=".venv/.env")
username= getenv("mail")
password = getenv("password")
phone = getenv("phone")
speedtest_url = "https://www.speedtest.net/"
twitter_url='https://twitter.com/login'

class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = self.driver_initialization()
        self.up = 0
        self.down = 0

    def driver_initialization(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        chrome_options.add_argument("--start-maximized")

        inner_driver = webdriver.Chrome(options=chrome_options)
        return inner_driver

    def get_internet_speed(self):
        self.driver.get(speedtest_url)
        self.driver.find_element(By.ID, value="onetrust-accept-btn-handler").click()
        self.driver.find_element(By.XPATH, value="//span[@class='start-text']").click()
        sleep(45)
        self.down = self.driver.find_element(By.XPATH,
                                             value="//span[@class='result-data-large number result-data-value download-speed']").text
        self.up = self.driver.find_element(By.XPATH,
                                           value="//span[@class='result-data-large number result-data-value upload-speed']").text
        print(f"dowload speed {self.down}")
        print(f"upload speed {self.up}")
        sleep(5)



    def tweet_at_provider(self):
        self.driver.get(twitter_url)
        the_post = f"my internter speed today is: {self.down} - {self.up}"

        sleep(3)
        # Enter Mail
        mail_input = self.driver.find_elements(By.XPATH, value='//input[@class="r-30o5oe r-1dz5y72 r-13qz1uu r-1niwhzg r-17gur6a r-1yadl64 r-deolkf r-homxoj r-poiln3 r-7cikom r-1ny4l3l r-t60dpp r-fdjqy7"]')
        mail_input[0].send_keys(username, Keys.TAB, Keys.ENTER)
        sleep(1)
        #enter phone
        # mporei na valw try
        phone_input = self.driver.find_elements(By.XPATH,
                                                value="//input[@class='r-30o5oe r-1dz5y72 r-13qz1uu r-1niwhzg r-17gur6a r-1yadl64 r-deolkf r-homxoj r-poiln3 r-7cikom r-1ny4l3l r-t60dpp r-fdjqy7']")
        phone_input[0].send_keys(phone, Keys.ENTER)

        sleep(1)

        # password input

        password_input = self.driver.find_elements(By.XPATH,
                                               value='//input[@class="r-30o5oe r-1dz5y72 r-13qz1uu r-1niwhzg r-17gur6a r-1yadl64 r-deolkf r-homxoj r-poiln3 r-7cikom r-1ny4l3l r-t60dpp r-fdjqy7"]')
        password_input[0].send_keys(password, Keys.ENTER)
        sleep(3)
        # Accept cookies
        self.driver.find_element(By.XPATH, value="//div[@class='css-146c3p1 r-bcqeeo r-qvutc0 r-37j5jr r-q4m81j r-a023e6 r-rjixqe r-b88u0q r-1awozwy r-6koalj r-18u37iz r-16y2uox r-1777fci']").click()

        # write to post

        post_box = self.driver.find_elements(By.XPATH, value="//div[@class='public-DraftStyleDefault-block public-DraftStyleDefault-ltr']")

        post_box[0].send_keys(the_post)
        sleep(1)

        post_button = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button')
        post_button.click()

