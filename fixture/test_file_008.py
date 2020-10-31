import pytest

def re():
    lis = []
    with open ('./1.txt','r') as f:
        for i in f.readlines():
            # print(i)
            # print(i.split('='))
            lis.append(eval(i.split('=')[-1]))
        return(lis)
#
class Test_xx:
# #     @pytest.mark.parametrize('li',['123','456'])
# #     def test_yy(self,li):
# #         assert  li == '123'
# #
#       @pytest.mark.parametrize('li,wang',[('123','456'),('789','910')])
#       def test_yy(self,li,wang):
#            assert  li == '789'

        @pytest.mark.parametrize('li,wang',re())
        def test_yy(self,li,wang):
            print( "li:%s,wang:%s" % (li,wang))



