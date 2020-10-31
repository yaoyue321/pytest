import pytest

class Test_xx:
    def test_xx(self,init_xx):
        return True
    @pytest.mark.xfail(2>1,reason="111")
    def test_yy(self):
        return False
