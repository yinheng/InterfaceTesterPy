import unittest
from com.yinheng.test import test_config_reader

test_config_xml_path = '''E:/Workspace-Wendy/InterfaceTestPy/resource/test_config.xml'''

class InterfaceTest(unittest.TestCase):

    def setUp(self):
        dict = test_config_reader.TestConfigReader().readTestConfig(test_config_xml_path)
        print(dict)

    def testInterface(self):
        assert 1 > 0
        pass

unittest.main()