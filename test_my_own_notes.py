import os
import unittest
from appium import webdriver
from time import sleep

class TestMyOwnNotes(unittest.TestCase):
    "Class to run tests against the MyOwnNotes app"

    def setUp(self):
        "Setup for the test"
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.4'
        desired_caps['deviceName'] = 'Android Emulator'

        # Returns abs path relative to this file and not cwd
        desired_caps['app'] = "/Users/dbhaskaran/StudioProjects/apps/MyOwnNotes.apk"
        desired_caps['appPackage'] = "org.aykit.MyOwnNotes"
        desired_caps['appActivity'] = "org.aykit.owncloud_notes.SettingsActivity"
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        "Tear down the test"
        self.driver.quit()

    def edit_settings(self):
        "Test editing settings works as expected"
        element = self.driver.find_elements_by_class_name("android.widget.EditText")
        element[0].clear()
        element[1].clear()
        element[2].clear()
        element[0].send_keys("https://cloud.testdroid.com/")
        element[1].send_keys("deepak.bhaskaran@gmail.com")
        element[2].send_keys("password")

        element = self.driver.find_elements_by_class_name("android.widget.ImageView")
        element[0].click()


    def saved_settings(self):
        "Test if saved settings are as expected"
        element = self.driver.find_elements_by_class_name("android.widget.EditText")
        server_address = element[0].text
        username = element[1].text
        password = element[2].text
        assert (server_address == "https://cloud.testdroid.com/")
        assert (username == "deepak.bhaskaran@gmail.com")
        assert (password == "password")


#---START OF SCRIPT
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestMyOwnNotes)
    unittest.TextTestRunner(verbosity=2).run(suite)
