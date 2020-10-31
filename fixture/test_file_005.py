import pytest
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

class Test_index:
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

    def wait_ele(self,type,data):
        if type == "id":
            return WebDriverWait(self.driver,10,1).until(lambda x:x.find_element_by_id(data))
        if type == "xpath":
            return WebDriverWait(self.driver,10,1).until(lambda x:x.find_element_by_xpath(data))

    @pytest.fixture()
    def in_dex(self):
        dc = self.wait_ele("xpath","//*[contains(@text,'电池')]")
        gd = self.wait_ele("xpath","//*[contains(@text,'更多')]")
        self.driver.drag_and_drop(dc,gd)
        self.wait_ele("xpath", "//*[contains(@text,'位置信息')]").click()

    @pytest.mark.usefixtures("in_dex")
    def test_in(self):
        jx = self.wait_ele("id","android:id/summary")
        jx.click()
        self.wait_ele("xpath", "//*[contains(@text,'耗电量')]").click()
        self.driver.find_element_by_class_name("android.widget.ImageButton").click()
        assert "耗电量" in jx.text




