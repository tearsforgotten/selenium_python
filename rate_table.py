#!/usr/bin/env python
#coding=utf-8
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
import time





class class4_uploadrate(unittest.TestCase):
    def setUp(self):
        url="http://192.168.1.232:86"
        self.driver=webdriver.Firefox()
        self.base_url=url



    def test_login(self):
        driver=self.driver
        driver.get(self.base_url + "/")
        ####log web###
        name=driver.find_element_by_xpath("//*[@id='myform']/input[2]")
        password=driver.find_element_by_xpath("//*[@id='myform']/input[3]")
        vertify=driver.find_element_by_xpath("//*[@id='myform']/div[1]/input")
        submint=driver.find_element_by_xpath("//*[@id='myform']/div[3]/div[2]/button")
        name.send_keys("admin")
        password.send_keys("123456")
        vertify.send_keys("1234")
        try:
            submint.click()
        except AssertionError:
            print "login fial"
        else:
            print "login success"

        ####log switch menu
        driver.get(self.base_url + "/rates/rates_list")

        ####creat a new rate
        create_Tag=WebDriverWait(driver,30).\
            until(lambda driver: driver.find_element_by_xpath("//*[@id='content']/div[4]/a[1]"))
        creatNew_rate=create_Tag.click()
        time.sleep(3)
        try:
            rateTableName=driver.find_element_by_xpath("//*[@id='myform']/table[1]/tbody/tr[1]/td[2]/input")
        except:
            print "not fount rate name"
        finally:
            rateTableName.send_keys("test_upload9")
        driver.find_element_by_xpath("//*[@id='ratelist']/tfoot/tr/td/input[1]").click()
        ###find upload menu
        driver.find_element_by_xpath("//*[@id='content']/div[7]/div/div[1]/ul/li[3]/a").click()
        time.sleep(2)

        upload_file=WebDriverWait(driver,60).\
            until(lambda driver: driver.find_element_by_xpath("//*[@id='myform']/table/tbody/tr[1]/td[2]/span/input[1]"))
        import spidermonkey
        rt = spidermonkey.Runtime()
        cx = rt.new_context()
        cx.execute('document.getElementsByName('myfile_filename')[0].value = "test_upload_test.csv";')

        time.sleep(60)

def Configure():
    parser = argparse.ArgumentParser(description='rate upload test')
    parser.add_argument('-c', dest='rate_file', action='store', help='rate file')
    args = parser.parse_args()
    if args.config_file is None:
        parser.print_help()
        sys.exit(-1)

    return args

if __name__=="__main__":
    unittest.main()
    args=Configure()

