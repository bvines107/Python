from selenium import webdriver
import time


#the program will open the Google Chrome browser,
# if an error occurs the try except state will catch it
try:
    browser = webdriver.Chrome()
except Exception as noC:
    print('There was an error: %s ' % noC)


#the program will sleep for 30 seconds to allows the browser time
#to load
time.sleep(30)


# the speed test website is passed to the browser,
#if an error occurs the try except state will catch it.
try:
    browser.get('https://speedsmart.net/')
except Exception as noP:
    print('There was an error: %s ' % noP)


#the selenium module will locate the start button and start the speed test
#unless an error occurs
try:
    start_test = browser.find_element_by_id('start_button')
    start_test.click()
except Exception as noB:
    print('There was an error: %s ' % noB)


#the program will sleep for 30 seconds to allows the browser time
#to calculate the pc's upload and downtimes.
time.sleep(30)


#the save screenshot method will take a screen shot of the page after the process has
#completed
browser.save_screenshot('results.png')


#the close method will close the browser.
browser.close()