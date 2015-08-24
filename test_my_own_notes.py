import os
import unittest
from appium import webdriver
from time import sleep

class TestMyOwnNotes(unittest.TestCase):
    "Class to run tests against the MyOwnNotes app"
    desired_caps = {}

    def setUp(self):
        "Setup for the test"
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.4'
        desired_caps['deviceName'] = 'Android Emulator'

        # Returns abs path relative to this file and not cwd
        desired_caps['app'] = "/Users/dbhaskaran/StudioProjects/apps/MyOwnNotes.apk"
        desired_caps['appPackage'] = "org.aykit.MyOwnNotes"
        #desired_caps['appActivity'] = "org.aykit.owncloud_notes.SettingsActivity"
        desired_caps['appActivity'] = "org.aykit.owncloud_notes.NoteListActivity"
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
