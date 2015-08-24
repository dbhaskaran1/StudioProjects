import os
import unittest
from appium import webdriver
from time import sleep
import ConfigParser

class TestMyOwnNotes(unittest.TestCase):
    "Class to run tests against the MyOwnNotes app"
    desired_caps = {}
    config_file = ConfigParser.ConfigParser()

    def setUp(self):
        "Setup for the test"
        try:
            self.config_file.read('./test_my_own_notes.config')
        except Exception,e:
            print e.message

        desired_caps = {}
        desired_caps['platformName'] = self.config_file.get('desired_caps','platformName')
        desired_caps['platformVersion'] = self.config_file.get('desired_caps','platformVersion')
        desired_caps['deviceName'] = self.config_file.get('desired_caps','deviceName')

        # Returns abs path relative to this file and not cwd
        desired_caps['app'] = self.config_file.get('desired_caps','app')
        desired_caps['appPackage'] = self.config_file.get('desired_caps','appPackage')
        desired_caps['appActivity'] = self.config_file.get('desired_caps','appActivity')
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.desired_caps =desired_caps

    def tearDown(self):
        "Tear down the test"
        self.driver.quit()

    def test_edit_settings(self):
        "Test editing settings works as expected"
        self.driver.find_element_by_name("More options").click()
        self.driver.find_element_by_xpath("//android.widget.ListView[1]/android.widget.LinearLayout[1]").click()
        element = self.driver.find_elements_by_class_name("android.widget.EditText")
        element[0].clear()
        element[1].clear()
        element[2].clear()
        element[0].send_keys("https://cloud.testdroid.com/")
        element[1].send_keys("deepak.bhaskaran@gmail.com")
        element[2].send_keys("password")

        element = self.driver.find_elements_by_class_name("android.widget.ImageView")
        element[0].click()

    def test_saved_settings(self):
        "Test if saved settings are as expected"
        self.driver.find_element_by_name("More options").click()
        self.driver.find_element_by_xpath("//android.widget.ListView[1]/android.widget.LinearLayout[1]").click()

        element = self.driver.find_elements_by_class_name("android.widget.EditText")
        server_address = element[0].text
        username = element[1].text
        password = element[2].text

        assert (server_address == "https://cloud.testdroid.com/")
        assert (username == "deepak.bhaskaran@gmail.com")
        assert (password == "password")

    def test_create_new_note(self):
        element = self.driver.find_element_by_name("Create new note")
        element.click()
        element = self.driver.find_element_by_xpath("//android.view.View[1]/android.widget.FrameLayout[2]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.EditText[1]")
        element.send_keys("This is a test")
        self.driver.find_element_by_name("Save note").click()

    def test_refresh_note_list(self):
        element = self.driver.find_element_by_name("synchronize")
        element.click()
        self.driver.find_element_by_xpath("//android.view.View[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.ListView[1]/android.widget.RelativeLayout[1]").click()

    def test_help_page(self):
        self.driver.find_element_by_name("More options").click()
        self.driver.find_element_by_xpath("//android.widget.ListView[1]/android.widget.LinearLayout[2]/android.widget.RelativeLayout[1]/android.widget.TextView[1]").click()
        help_text = self.driver.find_element_by_xpath("//android.view.View[1]/android.widget.FrameLayout[2]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.TextView[1]").text
        assert (help_text.startswith("Which URL should I enter"))

    def test_about_page(self):
        self.driver.find_element_by_name("More options").click()
        self.driver.find_element_by_xpath("//android.widget.ListView[1]/android.widget.LinearLayout[3]/android.widget.RelativeLayout[1]/android.widget.TextView[1]").click()

        about_text = self.driver.find_element_by_xpath("//android.view.View[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.TextView[1]").text
        assert (about_text.startswith("MyOwnNotes 1.6"))

#---START OF SCRIPT
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestMyOwnNotes)
    unittest.TextTestRunner(verbosity=2).run(suite)
