from selenium.webdriver.common.by import By
from GeneralPage.base_page import BasePage
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


class LoginPage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)

    TextUserName = (By.XPATH,"//input[@placeholder='Email']")
    TextPassWord = (By.XPATH,"//input[@placeholder='Password']")
    LoginButton = (By.XPATH,"//span[normalize-space()='LOGIN']")


    def enter_username(self, username):
        self.send_keys(self.TextUserName,username)
    
    def enter_password(self, password):
        self.send_keys(self.TextPassWord,password)
    
    def click_login_button(self):
        self.click(self.LoginButton)


