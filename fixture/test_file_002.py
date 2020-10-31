import pytest

@pytest.fixture()
def init_xx():
    print("初始化测试数据工作")
    with open("./data.txt","w") as f:
        f.write("1")

class Test_xx:
    def test_xx(self,init_xx):
        with open("./data.txt","r") as f:
            assert f.read() == "1"
    def test_yy(self):
        assert False
