# StudioProjects
## MyOwnNotes - steps to run test suite
```
virtualenv mobile
source mobile/bin/activate
pip install -r requirements.txt
python test_my_own_notes.py
```

## Sample output from a test run
### (mobile)StudioProjects:$ python test_my_own_notes.py
```
(mobile)StudioProjects:$ python test_my_own_notes.py
test_about_page (__main__.TestMyOwnNotes) ... ok
test_create_new_note (__main__.TestMyOwnNotes) ... ok
test_edit_settings (__main__.TestMyOwnNotes)
Test editing settings works as expected ... ok
test_help_page (__main__.TestMyOwnNotes) ... ok
test_refresh_note_list (__main__.TestMyOwnNotes) ... ERROR
test_saved_settings (__main__.TestMyOwnNotes)
Test if saved settings are as expected ... FAIL

======================================================================
ERROR: test_refresh_note_list (__main__.TestMyOwnNotes)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "test_my_own_notes.py", line 68, in test_refresh_note_list
    self.driver.find_element_by_xpath("//android.view.View[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.ListView[1]/android.widget.RelativeLayout[1]").click()
  File "/Users/dbhaskaran/StudioProjects/mobile/lib/python2.7/site-packages/selenium/webdriver/remote/webdriver.py", line 253, in find_element_by_xpath
    return self.find_element(by=By.XPATH, value=xpath)
  File "/Users/dbhaskaran/StudioProjects/mobile/lib/python2.7/site-packages/selenium/webdriver/remote/webdriver.py", line 707, in find_element
    {'using': by, 'value': value})['value']
  File "/Users/dbhaskaran/StudioProjects/mobile/lib/python2.7/site-packages/selenium/webdriver/remote/webdriver.py", line 196, in execute
    self.error_handler.check_response(response)
  File "/Users/dbhaskaran/StudioProjects/mobile/lib/python2.7/site-packages/appium/webdriver/errorhandler.py", line 29, in check_response
    raise wde
NoSuchElementException: Message: An element could not be located on the page using the given search parameters.


======================================================================
FAIL: test_saved_settings (__main__.TestMyOwnNotes)
Test if saved settings are as expected
----------------------------------------------------------------------
Traceback (most recent call last):
  File "test_my_own_notes.py", line 54, in test_saved_settings
    assert (server_address == "https://cloud.testdroid.com/")
AssertionError

----------------------------------------------------------------------
Ran 6 tests in 82.034s

FAILED (failures=1, errors=1)
```
