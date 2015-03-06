from selenium import webdriver
driver=webdriver.Firefox()
driver.get("http://www.baidu.com")
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div[3]/a[6]").click()
