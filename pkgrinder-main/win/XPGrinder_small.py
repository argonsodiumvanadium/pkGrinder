from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

import time
import json
import os

rave = "https://cutewallpaper.org/21/dancing-crab-gif/Crab-Rave-Gif-Icalliance.gif"

commands = []

username = ""
password = ""
channel = ""

delay = 5

def spam(driver,discord_out):
	while True:
		for command in commands:
			discord_out.send_keys(command)
			discord_out.send_keys(Keys.RETURN)
			time.sleep(delay)


# read the file and initialize shit
file = open("./data.json", "r")
data = json.load(file)
delay = data["delay"]
commands = data["commands"]
channel = data["channel"]

commands.append(rave)


chromedriver = "C:/Users/Argon/Downloads/chromedriver_win32/chromedriver"
cap = DesiredCapabilities.CHROME
cap = {'binary_location': chromedriver}

# open a chrome window and control it
driver = webdriver.Chrome(desired_capabilities=cap, executable_path=chromedriver)

# log in 

# navigate to URL
driver.get("https://discord.com/login")

time.sleep(30)
driver.get(channel)
time.sleep(5)

# find HTML element to spam
msg_input = driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[2]/div/div/div/div/div[2]/div/main/form/div/div/div/div/div[3]/div[2]')

spam(driver,msg_input)


