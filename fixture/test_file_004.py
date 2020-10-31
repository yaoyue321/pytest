import pytest
#params 列表
@pytest.fixture(params=[(1,2)])
def init_xx(request):
    a,b = request.param

    print(a)
    print(b)

    return request.param

class Test_xx:
    def setup_class(self):
        print("setup_clas")
    def teardown_class(self):
        print("teardown_class")

    def test_xx(self, init_xx):
        assert  init_xx != 4
