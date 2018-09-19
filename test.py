from selenium import webdriver
import time

firefox_capabilities ={
    "browserName": "firefox",
    "version": "61.0.2",
    "platform": "ANY",
    "javascriptEnabled": True,
    "marionette": True,
}
driver=webdriver.Remote("http://192.168.14.93:4444/wd/hub",desired_capabilities=firefox_capabilities)

driver.maximize_window()
time.sleep(5)
driver.get("https://www.baidu.com")

