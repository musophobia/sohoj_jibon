from selenium import webdriver
import time
import urllib
import urllib2
import random

siteName=raw_input("site url without http: ") 
refreshrateFrom=raw_input("Sleep Between: ")
refreshrateTo=raw_input("To: ")
refreshrate=random.randint(int(refreshrateFrom), int(refreshrateTo))
driver = webdriver.Firefox()
driver.get("http://"+siteName)
while True:
    time.sleep(refreshrate)
    driver.refresh()
