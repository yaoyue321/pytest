import pytest

@pytest.fixture()
def init_xx():
    print("初始化测试数据工作")
    with open("./data.txt","w") as f:
        f.write("3")

@pytest.mark.usefixtures("init_xx")
class Test_xx:
    def setup_class(self):
        print("setup_clas")
    def teardown_class(self):
        print("teardown_class")

    def test_xx(self):
        with open("./data.txt","r") as f:
            assert  f.read() == "1"
    def test_yy(self):
        assert False



