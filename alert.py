
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

import unittest
class alert(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Firefox()
	
	def test_login(self):
		driver=self.driver
		driver.get("http://192.168.1.232:86")
		name=driver.find_element_by_xpath("//*[@id='myform']/input[2]")
		password=driver.find_element_by_xpath("//*[@id='myform']/input[3]")
		vertify=driver.find_element_by_xpath("//*[@id='myform']/div[1]/input")
		name.send_keys("admin")
		password.send_keys("123456")
		vertify.send_keys("1111")
		submit=driver.find_element_by_xpath("//*[@id='myform']/div[3]/div[2]/button")				
		submit.click()
	def test_alert(self):
		driver=self.driver
		switch=driver.find_element_by_xpath("/html/body/div[2]/div/div/ul/li[8]/a")
		rate_table=driver.find_element_by_xpath("//*[@id='content']/div[1]/ul[1]/li[8]/ul/li[8]/a")
		ActionChains(driver).move_to_element(switch).perform()
		current_url=driver.current_url
		print current_url
if __name__== "__main__":
	unittest.main()
