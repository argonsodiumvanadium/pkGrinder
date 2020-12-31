from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located

import time
import requests
import json

API_PATH = "https://pokeapi.co/api/v2/"

commands = [
	"http://gph.is/2cu8U3N",
	".route 12",
	"2",
	"krabby",
	"wartortle",
	"raichu",
	"gloom",
	"starmie",
	"arcanine",
	"2",
]

class DriverManager():
	def __init__ (self, driver):
		self.driver = driver

	def get_unread_from(text):
		msgs = self.driver.find_elements_by_class_name("message-2qnXI6")

		for i in range(0, len(msgs)):
			index = len(msgs) - 1 - i

			if msgs[index] == text:
				return msgs[index : len(msgs)]

		return []

	def find_last_by_class(self,class_name):
		elements = self.driver.find_elements_by_class_name(class_name)
		return elements[- 1]


class Brain ():
	def __init__ (self,gym_num, discord_out, driver):
		self.current_gym = gym_num
		self.out = discord_out
		self.driver_manager = DriverManager(driver)
		self.form_strategy()

	def send_command (self,text):
		self.out.send_keys(text)
		self.out.send_keys(Keys.ENTER)

	def wait (self, t = 5):
		time.sleep(t)

	def form_strategy (self):
		self.get_gym_info ()

	def get_gym_info (self):
		self.send_command(".gymbattle")
		self.wait()

		pk_name = self.driver_manager.find_last_by_class("embedAuthorName-3mnTWj").text
		print(pk_name)
		pk_name = pk_name.split(" ")[-1]

		self.get_type(pk_name.lower())

	def get_type (self, name):
		response = requests.get(API_PATH+"pokemon/" + name).text

		pk_data = json.loads(response)

		types = pk_data["types"]

		st = ""

		for pk_type in types:
			st = st + pk_type["type"]["name"]

		print(st)

		self.send_command(st)
		self.wait()




def start_AI(driver,discord_out):
	brain = Brain(4, discord_out, driver)



with Firefox() as driver:
	driver.get("https://discord.com/login?email=username")
	element = driver.find_elements_by_class_name("inputDefault-_djjkz")[1]
	element.send_keys("password"+Keys.RETURN)

	time.sleep(5)
	driver.get("https://discord.com/channels/732851808388644915/788713521448747028")
	time.sleep(5)

	msg_input = driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[2]/div/div/div/div/div[2]/div/main/form/div/div/div/div/div[3]/div[2]')

	start_AI(driver,msg_input)


