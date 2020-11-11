#!/usr/bin/env python

""" 
is-defense.py: Verifies if thesis defense date has changed on PeiPal page
"""
__author__  = "Pedro Barreiros"
__email__   = "pxcodename6@gmail.com"

from selenium import webdriver
from decouple import config
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from mailit import send_mail
import time

DRIVERPATH = config("DRIVERPATH")
URL = config("URL")
DIUSER = config("DIUSER")
DIPASS = config("DIPASS")

while True: 
    driver = webdriver.Firefox(executable_path=DRIVERPATH)
    driver.get(URL)
    driver.find_element_by_id("username").send_keys(DIUSER)
    driver.find_element_by_id("password").send_keys(DIPASS)
    driver.find_element_by_name("submit").click()

    time.sleep(1)

    selection = Select(driver.find_element_by_xpath("//select[@name='ano']"))
    selection.select_by_visible_text("1920")

    time.sleep(1)

    driver.find_element_by_link_text("Trabalho").click()

    time.sleep(1)

    tabledata = driver.find_elements_by_xpath("//table/tbody/tr[27]/td")

    for row in tabledata:
        defense_date = row.text

    if defense_date == "0000-00-00 00:00:00":
        print("Still no updates regarding thesis defense date -> " + defense_date)
        #send_mail("Thesis Defense Date", "Thesis defense date will be on the " + defense_date)
    else:
        print("Here is the date: ", defense_date)
        send_mail("Thesis Defense Date", "Thesis defense date will be on the " + defense_date)

    time.sleep(2)
    driver.close()
    time.sleep(3600*2)



