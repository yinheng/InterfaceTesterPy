from enum import Enum
import xlrd


class Level(Enum):
    High = 0,
    Middle = 1,
    Low = 2


class RequestType(Enum):
    GET = 0,
    POST = 1,
    DATABASE = 2,
    NONE = -1


class Result(Enum):
    SUCCESS = 0,
    FAILURE = 1


class ResultStatistics:
    success = 0
    fail = 0


class TestCase:
    __index__ = 0
    __id__ = ""
    __testName__ = ""
    __level__ = Level.High
    __requestType__ = RequestType.NONE
    __HTTPHeader__ = ""
    __target__ = ""
    __expectedData__ = ""
    __param__ = ""
    __output__ = ""
    __outputDict__ = {}
    __response__ = ""
    __responseList__ = []
    __result__ = Result.FAILURE


class TestCaseBuilder:
    __index__ = 0
    __id__ = ""
    __testName__ = ""
    __level__ = Level.High
    __requestType__ = RequestType.NONE
    __HTTPHeader__ = ""
    __target__ = ""
    __expectedData__ = ""
    __param__ = ""
    __output__ = ""
    __outputDict__ = {}
    __response__ = ""
    __responseList__ = []
    __result__ = Result.FAILURE

    def index(self, index):
        self.__index__ = index
        return self

    def id(self, uid):
        self.__id__ = uid
        return self

    def test_name(self, test_name):
        self.__testName__ = test_name
        return self

    def level(self, level):
        self.__level__ = level
        return self

    def request_type(self, request_type):
        self.__requestType__ = request_type
        return self

    def http_name(self, http_name):
        self.__HTTPHeader__ = http_name
        return self

    def target(self, target):
        self.__target__ = target
        return self

    def expected_data(self, expected_data):
        self.__expectedData__ = expected_data
        return self

    def param(self, param):
        self.__param__ = param
        return self

    def output(self, output):
        self.__output__ = output
        return self

    def output_dict(self, output_dict):
        self.__outputDict__ = output_dict
        return self

    def response(self, response):
        self.__response__ = response
        return self

    def response_list(self, response_list):
        self.__responseList__ = response_list
        return self

    def result(self, result):
        self.__result__ = result
        return self

    def build(self):
        case = TestCase()
        case.__index__ = self.__index__
        case.__id__ = self.__id__
        case.__testName__ = self.__testName__
        case.__level__ = self.__level__
        case.__requestType__ = self.__requestType__
        case.__HTTPHeader__ = self.__HTTPHeader__
        case.__target__ = self.__target__
        case.__expectedData__ = self.__expectedData__
        case.__param__ = self.__param__
        case.__output__ = self.__output__
        case.__outputDict__ = self.__outputDict__
        case.__response__ = self.__response__
        case.__responseList__ = self.__responseList__
        case.__result__ = self.__result__
        return case


def read_excel(path):

    case_list = []
    test_case_dict = {0: "__id__ ", 1: "__testName__", 2: "__level__", 3: " __requestType__",
                    4: "__HTTPHeader__", 5: "__target__", 6: "__expectedData__", 7: "__param__",
                    8: "__output__", 9: "__response__", 10: "__result__"}

    workbook = xlrd.open_workbook(path)
    sheets = workbook.sheet_names()
    worksheet = workbook.sheet_by_name(sheets[0])
    print("rows:", worksheet.nrows, "col: ", worksheet.ncols)
    for i in range(1, worksheet.nrows):
        case = TestCase()
        for j in range(0, worksheet.ncols):
            col_name = test_case_dict[j]
            print("col_name: ", col_name)
            case.col_name = worksheet.cell_value(i, j)
            print("row: ", i, "col： ", j, case.col_name)
        case_list.append(case)
        print(len(case_list))
    return case_list


# read_excel('''F:/cygwin/home/Template1.xls''')


