from  selenium import webdriver
import os
driver=webdriver.Firefox()
file_path='file:///' +os.path.abspath('checkbox.html')
driver.get(file_path)
inputs=driver.find_element_by_tag_name('input')
print inputs
for input in inputs:
    id=input.get_attribute('type')
    print id
