from selenium import webdriver
browser=webdriver.Firefox()
browser.get("http://www.baidu.com")
browser.find_element_by_id("kw").send_keys("selenium")
browser.find_element_by_id("su").click()

from selenium.webdriver.common.action_chains import actionchains
actionchains(driver).double_click(double).perform()
actionchains(driver).drag_and_drop(element).perform()
actionchains(driver).move_to_element()
click_and_hold
context_click
double_click
drag_and_drop
move_to_element
click_and_hold
context_click
double_click
drag_and_drop
move_to_hold
from selenium.webdriver.common.action_chains import   actionchains
actionchains(driver).move_to_hold().perform()
from selenium.webdriver.common.keys import  Keys
senk_keys(JKeys.Back_space)
send_keys(Keys_space)
send_keys(Keys_tab)
send_keys(Keys.control, 'c')
