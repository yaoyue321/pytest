import pytest

@pytest.fixture(scope="function",autouse=True)
#不写默认为scope="function"
# @pytest.fixture(scope="class",autouse=True)
def init_xx():
    print("before")

class  Test_xx:
    def test_xx(self):
        print("test_xx")
    def test_yy(self):
        print("test_yy")