import abc
import requests
import pymysql
import data


class TestCaseRequester:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_response(self, case):
        pass


class HTTPGetRequester(TestCaseRequester):
    def get_response(self, case):
        url = case.__target__
        ret = requests.get(url)
        response = ret.text
        print("response: ", response)
        return response


class HTTPPostRequester(TestCaseRequester):
    def get_response(self, case):
        url = case.__target__
        param = case.__param__
        print("url: ",  url)
        print("param: ", param)
        ret = requests.post(url,  data=param)
        response = ret.text
        print("ret url: ", ret.url)
        return response


class MYSQLRequester(TestCaseRequester):
    def get_response(self, case):
        url = case.__target__
        param = case.__param__
        # 打开数据库连接
        db = pymysql.connect(url, "root", "yinheng", "TESTDB")

        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()

        # 使用 execute()  方法执行 SQL 查询
        cursor.execute(param)

        # 使用 fetchone() 方法获取单条数据.
        response = cursor.fetchone()

        print("Database version : %s " % response)

        # 关闭数据库连接
        db.close()
        return response


case_list = data.read_excel('''F:/cygwin/home/Template1.xls''')
print("case_list: ", len(case_list))
for case in case_list:
    print("case target:", case.__target__)
    print("case name:", case.__testName__)
    print("case param:", case.__param__)
    print("case requestType: ", case.__requestType__)
    if case.__requestType__ == "GET":
        response = HTTPGetRequester().get_response(case)
        print("get response:", response)

    if case.__requestType__ == "POST":
        response = HTTPGetRequester().get_response(case)
        print("get response:", response)

    if case.__requestType__ == "DATABASE":
        response = MYSQLRequester().get_response(case)

