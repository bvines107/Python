from selenium import webdriver
import time

chrome = webdriver.Chrome()

chrome.get("http://www.google.com")

searchElem = chrome.find_element_by_name("q")
searchElem.send_keys("Python Tutorials")
enterElem = chrome.find_element_by_name("btnK")
enterElem.submit()

time.sleep(10)

results = chrome.find_elements_by_xpath("//a[@ping]")

print("Found " + str(len(results)) + " searches")

for name in results:
    print(name.get_attribute("innerHTML"))


chrome.close()

