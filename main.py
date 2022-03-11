from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
from dotenv import load_dotenv
import os
import time

dotenv_path = Path(".env")
load_dotenv(dotenv_path=dotenv_path)

SIMILAR_ACCOUNT = "chefsteps"
USER = os.getenv("GMAIL")
PASSWORD = os.getenv("PASSWORD")

CHROME_DRIVER = "C:\Developer\chromedriver.exe"

class InstaFollower:

    def __init__(self, website):
        self.driver = webdriver.Chrome(executable_path=website)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        self.driver.maximize_window()

        time.sleep(3)
        self.login_ig = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
        self.login_ig.send_keys(USER)
        self.password_ig = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
        self.password_ig.send_keys(PASSWORD)
        self.password_ig.send_keys(Keys.ENTER)

    def find_follow(self):
        time.sleep(5)
        self.seacher = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[1]')
        self.seacher.click()
        self.seacher_write = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
        self.seacher_write.send_keys(SIMILAR_ACCOUNT)

        time.sleep(2)
        self.choose = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a/div')
        self.choose.click()

        time.sleep(2)
        self.show_followers = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/div')
        self.show_followers.click()

        time.sleep(3)
        self.scroll_down = self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[2]')
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", self.scroll_down)
            time.sleep(2)

    def follow(self):
        self.follow_people = self.driver.find_elements_by_css_selector(".PZuss button")
        for button in self.follow_people:
            # if button.text == "Follow":
            #     time.sleep(2)
            #     button.click()
            # else:
            #     pass
            try:
                time.sleep(2)
                button.click()

            except ElementClickInterceptedException:
                time.sleep(2)
                self.cancel_followed = self.driver.find_element_by_xpath('/html/body/div[7]/div/div/div/div[3]/button[2]')
                self.cancel_followed.click()

ig = InstaFollower(CHROME_DRIVER)
ig.login()
ig.find_follow()
ig.follow()