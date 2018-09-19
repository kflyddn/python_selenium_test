#coding=utf-8
from selenium import webdriver
import unittest
import sys
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
        #self.driver = webdriver.Firefox()
        self.driver = webdriver.Remote("http://192.168.14.93:4444/wd/hub",desired_capabilities=firefox_capabilities)
    # 打开url
        self.driver.get("http://kflyddn.top:7600/account/login")

    # 登录操作
    def test_login(self):
        title = self.driver.title
        print title
        now_url = self.driver.current_url
        #print now_url
        username = "kflyddn@gmail.com"
        password = "zblj1211"
        # 执行登录操作
        #用户名的定位
        self.driver.find_element_by_id("email").clear()
        self.driver.find_element_by_id("email").send_keys(username)
        #密码的定位
        self.driver.find_element_by_id("password").clear()
        self.driver.find_element_by_id("password").send_keys(password)
        # 点击登录
        #self.driver.find_element_by_css_selector(".btn.btn-success.btn-block").click()
        self.driver.find_element_by_id("submit").click()
        # 登录成功断言
        login_name = self.driver.find_element_by_xpath('html/body/div[1]').text
        print login_name.strip()
        #login_name = self.driver.find_element_by_xpath('html/body/div[3]/div[2]/ul/li[1]/a/strong').text
        #login_name = login_name.strip('Hello')
        #assert login_name == username
        assert login_name == "You are now logged in. Welcome back!"

    # 关闭浏览器
    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()