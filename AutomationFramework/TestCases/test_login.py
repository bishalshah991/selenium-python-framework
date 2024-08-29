import pytest
import softest as softest
from PageObject.login_page import LoginPage
from DataSet.application_data import TestData


@pytest.mark.usefixtures("tc_setup")
class TestLogin(softest.TestCase):

    def test_login_to_application(self,driver):
        self.login = LoginPage(self.driver)
        self.login.enter_username(TestData.username)
        print("user Logged in successfully")