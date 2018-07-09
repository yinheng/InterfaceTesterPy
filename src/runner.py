import abc
import requests
import data


class TestCaseRequester:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_response(self, case):
        return


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
        ret = requests.post(url,  data=param)
        response = ret.text
        return response


case_list = data.read_excel('''F:/cygwin/home/Template1.xls''')
for case in case_list:
    if case.__requestType__ == "GET":
        response = HTTPGetRequester().getResponse(case)
        print("get response:", response)

    if case.__requestType__ == "POST":
        response = HTTPGetRequester().getResponse(case)
        print("get response:", response)

