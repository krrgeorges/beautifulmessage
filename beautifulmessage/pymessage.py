from bs4 import BeautifulSoup as bs
from selenium import webdriver as wb
import time
from beautifulmessage.beautifulmessage.exceptions import *

"""
    Package information:
         Author : Rojit George
"""

class PyMessage:
    "Message sending package for Indian Mobile Numbers."
    url = "http://site24.way2sms.com/entry?ec=0080&id=8cds"

    def __init__(self,number,message):
        "Initializing the package variables."
        self.number = number
        self.message = message
        if len(number) > 10 or len(number) < 10:
            raise NumberLengthException("It seems you have entered an invalid number.")
        if len(message) > 140:
            raise MessageLengthException("Message length should be less than 140 characters.")
        
    def msg(self,driver):
        "Function for message sending."
        time.sleep(4)
        driver.switch_to_frame(driver.find_element_by_id("frame"))
        driver.find_element_by_id("mobile").send_keys(self.number)
        driver.find_element_by_id("message").send_keys(self.message)
        driver.find_element_by_name("Send").click()
        print("Message sent successfully to "+self.number)

    def smain(self):
        "Driver function for package."
        driver = wb.PhantomJS()
        driver.get(self.url)
        self.validate(driver,"9167913144","dragonvale")
        driver.execute_script("javascript:goToMain('s');")
        time.sleep(4)
        driver.execute_script("javascript:loadSMSPage('sendSMS');")
        self.msg(driver)

    def validate(self,driver,username,password):
        "Validation function for the site."
        driver.find_element_by_name("username").send_keys(username)
        driver.find_element_by_name("password").send_keys(password)
        driver.find_element_by_id("loginBTN").click()

    def send(self):
        "Main function for the package."
        self.smain()
        

    
