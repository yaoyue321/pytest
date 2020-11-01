import pytest,allure

class Test_st:
    def setup_class(self):
        print("ss")
    def teardown_class(self):
        print("dd")

    @allure.issue("http://www.baidu.com/ll")
    @allure.testcase("http://www.baidu.com")
    @allure.step(title="第一个测试用例")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_001(self):
        allure.attach("这是一个描述","试一下")
        assert True

#
if __name__ == '__main__':
      pytest.main(["-s","test_ws.py","--alluredir" ,"./report" ])
