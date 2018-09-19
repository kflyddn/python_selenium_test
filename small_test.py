from  selenium import webdriver
firefox_capabilities ={
    "browserName": "firefox",
    "version": "61.0.2",
    "maxInstances": 3,
    "platform": "ANY",
    "javascriptEnabled": True,
    "marionette": True,
}

try:
    browser=webdriver.Remote("http://192.168.0.189:4444/wd/hub",desired_capabilities=firefox_capabilities)
    browser.get("http://192.168.0.189:7700/account/login")
    browser.get_screenshot_as_file("D:/baidu.png")
    browser.close()
    browser.quit()
except Exception as e:
    print e
else:
    print "All things works well!!!!!!!!"
finally:
    print "done!!!!!!!!!!"