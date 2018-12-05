import ddt
import unittest

data =[
    {"user":"admin1","pwd":"111111","except":True},
    {"user":"admin2","pwd":"222222","except":False},
    {"user":"admin3","pwd":"333333","except":True},
    {"user":"admin4","pwd":"444444","except":False}
]

@ddt.ddt
class Test(unittest.TestCase):

    @ddt.data(*data)
    def test_01(self,test_data):
        print("测试的数据是：%s"%test_data)


if __name__ == '__main__':
    unittest.main()
