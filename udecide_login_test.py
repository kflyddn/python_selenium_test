#coding=utf-8
from selenium import webdriver
import unittest
import sys
import time
from selenium.webdriver.common.by import By


reload(sys)
sys.setdefaultencoding('utf8')
class TestLogin(unittest.TestCase):
    # 指定浏览器
    def setUp(self):
        firefox_capabilities ={
            "browserName": "firefox",
            "version": "61.0.2",
            "maxInstances": 3,
            "platform": "ANY",
            "javascriptEnabled": True,
            "marionette": True,
        }
        try:
            self.driver = webdriver.Remote("http://192.168.86.19:4444/wd/hub",desired_capabilities=firefox_capabilities)
            # 打开url
            self.driver.get("https://udecide-demo.digitalalchemy.net.au/login")
        except Exception as e:
            print ""
            self.driver.quit()

    # 登录操作
    def test_login(self):
        try:
            title = self.driver.title
            #print title
            now_url = self.driver.current_url
            #print now_url
            username = "udecide"
            password = "@uDec1de"
            # 执行登录操作 用户名的定位
            self.driver.find_element_by_id("username").clear()
            self.driver.find_element_by_id("username").send_keys(username)
            #密码的定位
            self.driver.find_element_by_id("password").clear()
            self.driver.find_element_by_id("password").send_keys(password)
            # 点击登录
            #self.driver.find_element_by_css_selector("button").click()
            #self.driver.find_element_by_id("submit").click()
            self.driver.find_element_by_tag_name("button").click()
            time.sleep(10)
            # 登录成功断言
            #login_name = self.driver.find_element_by_xpath('html/body/div[2]').text
            login_name = self.driver.find_element_by_link_text("ADMIN").text
            #login_name = self.driver.find_element_by_xpath('html/body/div[3]/div[2]/ul/li[1]/a/strong').text
            #login_name = login_name.strip('Hello')
            #print login_name.strip()
            assert login_name == "ADMIN"
            #assert login_name == "You are now logged in. Welcome back!"
        except Exception as e:
            print "bbbbbbbbbbbbbbbbbbbbbbbbbbbbb\n"
            print str(e)

    # 关闭浏览器
    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()