# -*- coding:utf-8 -*-

'''
    selenium 是一个用于web应用程序测试的工具,提供一些函数,通过这些函数可以定位操作到指定的标签,这些
定位标签的API函数都是用python实现的,框架底层是通过javascript实现的,完全模拟人工操作

使用selenium做爬虫的目的:
    有些网站通过动态加载数据的方式来展示数据,这些网站在正常发起请求的情况下,数据没有办法拿回来,
就可以使用selenium加载操作网页,等待数据加载完成后,再继续解析数据.
    用于用户模拟登录,然后直接访问数据的操作,并且在这些操作中,不需要手动提取cookie,浏览器会根据操作请求,自动携带一些需要的数据

'''

# 引入selenium中webdrider
from selenium import webdriver
import time

firefox_capabilities ={
    "browserName": "firefox",
    "version": "61.0.2",
    "maxInstances": 3,
    "platform": "ANY",
    "javascriptEnabled": True,
    "marionette": True,
}
# 创建一个火狐浏览器对象
try:
    firefox = webdriver.Remote("http://192.168.14.93:4444/wd/hub",desired_capabilities=firefox_capabilities)
    # 打开url
    firefox.get("www.baidu.com")
except Exception as e:
    print ""
    firefox.quit()
#
# firefox.find_element_by_class_name()  # 通过class属性值查找
# firefox.find_element_by_id()  # 通过id属性值查找
# firefox.find_element_by_link_text()  # 通过超链接文本内容查找
# firefox.find_element_by_name()  # 通过name属性值查找
# firefox.find_element_by_css_selector()  # 通过css选择器查找
# firefox.find_element_by_tag_name()  # 通过标签名称查找
# firefox.find_element_by_xpath()  # 通过xpath查找

ele = firefox.find_element_by_id('kw')
# 向输入框输入内容
ele.send_keys('seleium')
# 找到百度一下按钮
btn = firefox.find_element_by_id('su')
# 点击
ele.click()
time.sleep(10)
firefox.quit()


# get_attribute 获取到标签内的属性值
# res = ele.get_attribute('class')
# print(res)
# res = ele.text # 获取标签内的文本内容
# print(res)

# res = ele.tag_name # 获取标签的名称
# print(res)
# res = ele.is_selected() # 判断标签是否被选中
# print(res)
# res = ele.is_enabled() # 判断标签是否可用
# print(res)
# # 向输入框中输入一些数据
# ele.send_keys('selenium')#
# ele.click() # 点击标签
# ele.submit() # 提交表单
# import time
# time.sleep(2)
# res = ele.clear() # 清空输入框内容

# 截图
# ele.screenshot('test.png')