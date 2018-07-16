from xml.dom.minidom import parse
import xml.dom.minidom


class TestConfigReader():
    tag_param = "parameter"
    attr_name = "name"
    attr_value = "value"

    def readTestConfig(self, path):
        dict = {}
        DOMTree = xml.dom.minidom.parse(path)
        config = DOMTree.documentElement
        params = config.getElementsByTagName(TestConfigReader.tag_param)
        for param in params:
            name = param.getAttribute(TestConfigReader.attr_name)
            value = param.getAttribute(TestConfigReader.attr_value)
            print("name= %s, value= %s" % (name, value))
            dict[name] = value

        return dict
