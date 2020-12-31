from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located

import time
import requests
import json

rave = "http://gph.is/2cu8U3N"

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
username = data["username"]
password = data["password"]
delay = data["delay"]
commands = data["commands"]
channel = data["channel"]

commands.append(rave)

# open a firefox window and control it
with Firefox() as driver:
	# log in 
	driver.get("https://discord.com/login?email="+username)
	element = driver.find_elements_by_class_name("inputDefault-_djjkz")[1]
	element.send_keys(password+Keys.RETURN)

	# navigate to URL
	time.sleep(5)
	driver.get(channel)
	time.sleep(5)

	# find HTML element to spam
	msg_input = driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[2]/div/div/div/div/div[2]/div/main/form/div/div/div/div/div[3]/div[2]')

	spam(driver,msg_input)


