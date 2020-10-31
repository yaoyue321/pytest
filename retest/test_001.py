import pytest
from appium import webdriver
from selenium.webdriver.support.wait import  WebDriverWait
from selenium.webdriver.common.by import By

class Test_ST:
    def setup_class(self):
        desired_caps = dict()
        #平台名字，大小写不敏感
        desired_caps['platformName'] = 'Android'
        #系统版本
        desired_caps['platformVersion'] = '5.1'
        #设备名字
        desired_caps['deviceName'] = '192.168.224.101:5555'
        #要打开的app包名
        desired_caps['appPackage'] = 'com.android.settings'
        # # #要打开的界面名
        desired_caps['appActivity'] = 'com.android.settings.Settings'
        #driver.find_element_by_id("android:id/search_src_text").send_keys("中文")
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def teardown_class(self):
        self.driver.quit()

    def  wait(self,xpath):
        return WebDriverWait(self.driver,10,1).until(lambda x:x.find_element_by_xpath(xpath))

    # @pytest.mark.run(order=1)
    def test_001(self):
        self.wait("//*[contains(@text,'更多')]").click()
        gd_list = self.driver.find_elements_by_id("android:id/title")
        xc_list = []
        for i in gd_list:
            xc_list.append(i.text)
        assert "VPN" in xc_list

    # @pytest.mark.run(order=3)
    def test_002(self):

        self.wait("//*[contains(@text,'移动网络')]").click()
        self.wait("//*[contains(@text,'首选网络')]").click()
        self.wait("//*[contains(@text,'3G')]").click()

        s_list = self.driver.find_elements_by_id("android:id/summary")
        self.driver.find_element()
        t_list = []
        for i in s_list:
            t_list.append(i.text)

        assert "3G" in t_list,"失败"

    if __name__ == '__main__':
        pytest.main(["-s", "test_001.py"])






