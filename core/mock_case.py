""" 判断用例数据 的参数类型 返回 mock数据 """
import asyncio
import time
import datetime
from datetime import timedelta
import random
import string
from .mock.tefaker import FakerData
import allure
from .base_requests import BaseRequest
from .base_httpx import BaseHttpx
from .base_aiothttp import BaseAiohttp
from .tool.variable_dict import MARK
from .tool.handle_yaml import HandleYaml
class Random_Data:
    """ Random 随机数据"""
    def __init__(self):
        self.float =  random.random() # 1以内浮点小数
        self.two_decimal = round(random.uniform(1, 10),2) # 10以内2位浮点小数
        self.status = random.randint(0,4) # 系统状态
        self.positive_number = random.randint(1,100) # 正数0到100
        self.negative_number= random.randint(-100,0) # 负数100到0
        self.random_list = random.sample(string.ascii_letters + string.digits, 10) # 生成随机10位字符列表
        self.null_list = [] #空列表
        self.null_dict = {} #空字典
        self.default_list = ["测试列表"]
        self.default_dict = {"测试字典"}
        self.decide = random.choice([True, False]) # 判断bool 类型
        self.random_str = "?测试字符`!@#$%^&*()_-[}]{;'<.>/" # 字符串

        self.timestamp = int(round(time.time() * 1000)) # 13位时间戳
        self.now = datetime.datetime.now().date() # 当天日期
        self.yesterday = self.now - timedelta(days=7) # 上周
        self.tomorrow = self.now + timedelta(days=7) #下周
        self.nonetype = "?空值!@#$%^&*"



class MockCase:
    """ 拼接随机数据,组成参数字典 """
    def __init__(self,file_name=None,case_name=None,mock_method=None):
        """
        :param file_name: yaml文件的名称
        :param case_name: case文件的名称
        :param mock_method: mock方法,默认是自己判断参数格式,第二种就是可以自己定义要传的参数
        :param case_data: 读取yaml数据
        :param datas: 读取用例数据
        :random_data: 实例化 Random_Data()
        :random_faker: 实例化 FakerData()
        """
        self.file_name = file_name
        self.case_name = case_name
        self.mock_method = mock_method
        self.case_data = HandleYaml("read_case",self.file_name).base_handle()
        self.datas = self.case_data[self.case_name]
        self.random_data = Random_Data()
        self.faker = FakerData()

    def temporary_dict(self,original_dict):
        """
        :param params_dict: 传递一个原始参数字典
        :return: 返回一个临时字典,格式为{key,value}
        """
        key = [i for i, v in original_dict.items()]
        value = [i for i in original_dict.values()]
        temporary_dict = dict(zip(key, value))
        return temporary_dict

        # print("--------",temporary_dict)

    def default_dict(self,original_dict):
        """
        先创建一个临时字典,判断value值得类型,再用原始字典做更新操作,调用Random_Data 的值
        :param original_dict: 原始字典
        :return: 返回格式为{key:<class 'NoneType'>}
        """
        key = [i for i, v in original_dict.items()]
        value= [type(v) for i, v in original_dict.items()]
        temporary_dict = dict(zip(key, value)) # 临时字典

        for v, k in temporary_dict.items():
            if k == int:
                original_dict.update({v: self.random_data.positive_number})

            if k == float:
                original_dict.update({v: self.random_data.float})

            elif k == str:
                original_dict.update({v: self.random_data.random_str})

            elif k == list:
                original_dict.update({v: self.random_data.null_list})

            elif k == dict:
                original_dict.update({v: self.random_data.null_dict})

            elif k == bool:
                original_dict.update({v: self.random_data.decide})

            else:
                original_dict.update({v: self.random_data.nonetype})

        return original_dict


    def diy_dict(self,temporary_dict,original_dict):
        """
        发送的数据格式：{params:{key,value}},我们需要判断value的数据类型,我们把 value值自己设定,
        例如{params:{phonenumber:18200000000}} 在yaml文件改为 {params:{phonenumber:phone}}
        这样我们就知道 这个键 是手机号码的格式
        所以我们把 key和value 又拼接为一个临时字典。
        为什么需要临时字典？ 因为 value值 可以会有多个符合条件的 比如 pagenum 和 page 都是int格式,直接修改会报错  dictionary update sequence element #0 has length 7; 2 is required

        :param temporary_dict: 临时字典的格式就是这样的{value: type(value)}
        :param original_dict: yaml用例的原始参数字典,我们这里用来更新字典的数据
        :return:返回修改后的原始字典

        """
        """ 这是我们自定义的 yaml文件中 的 value 值,是一个判断条件，需要分析系统字段 找出有哪些格式"""
        assert_key = {"int": "int", "str":"str","username": "username","user_phone": "phone",
                      "useremail":"email","sex":"sex","status": "status",
                      "start": "oldtime", "end": "nowtime","null_list": "nulllist",
                      "null_dict":"nulldict","bool":"bool","nodetype":None}


        for v, k in temporary_dict.items():

            if k == assert_key["int"]:
                original_dict.update({v: self.random_data.positive_number})

            if k == assert_key["str"]:
                original_dict.update({v:self.random_data.random_str})

            elif k == assert_key["username"]:
                original_dict.update({v: self.faker.cn_name()})

            elif k == assert_key["user_phone"]:
                original_dict.update({v: self.faker.cn_phone()})

            elif k == assert_key["useremail"]:
                original_dict.update({v: self.faker.cn_email()})

            elif k == assert_key["sex"]:
                original_dict.update({v: self.faker.cn_sex()})

            elif k == assert_key["status"]:
                original_dict.update({v:self.random_data.status})

            elif k == assert_key["null_list"]:
                original_dict.update({v:self.random_data.null_list})

            elif k == assert_key["null_dict"]:
                original_dict.update({v:self.random_data.null_dict})

            elif k == assert_key["bool"]:
                original_dict.update({v:self.random_data.decide})

            elif k == assert_key["start"]:
                original_dict.update({v:str(self.random_data.yesterday)})

            elif k == assert_key["end"]:
                original_dict.update({v:str(self.random_data.now)})

            elif k == assert_key["nodetype"]:
                original_dict.update({v:self.random_data.nonetype})

        return original_dict

    def diy_data(self):
        """ 定制 mock 拼接字典"""
        if self.mock_method == "diy":
            if self.datas["request_method"] == "get_send":
                url_params = self.datas["url_params"]  # get请求的 的params  原始字典
                temporary_dict = self.temporary_dict(url_params) # 临时字典
                self.diy_dict(temporary_dict, url_params) #原始字典更新为 临时字典的数据
                return self.datas # mock用例


            elif self.datas["request_method"] == "post":
                send_params = self.datas["send_params"] # post 请求和 put请求 发送参数 原始字典
                temporary_dict = self.temporary_dict(send_params)
                self.diy_dict(temporary_dict,send_params)
                return self.datas  # mock用例

            elif self.datas["request_method"] == "put":
                send_params = self.datas["send_params"]# post 请求和 put请求 发送参数 原始字典
                temporary_dict = self.temporary_dict(send_params)
                self.diy_dict(temporary_dict, send_params)
                return self.datas  # mock用例

        else:
            if self.datas["request_method"] == "get_send":
                url_params = self.datas["url_params"]  # get请求的 的params  原始字典
                self.default_dict(url_params)
                return self.datas


            elif self.datas["request_method"] == "post":
                send_params = self.datas["send_params"]  # post 请求和 put请求 发送参数 原始字典
                self.default_dict(send_params)
                return self.datas

            elif self.datas["request_method"] == "put":
                send_params = self.datas["send_params"]  # post 请求和 put请求 发送参数 原始字典
                self.default_dict(send_params)
                return self.datas


class Checks:
    def __init__(self,request_method=None,file_name=None,case_name=None,mock_method=None,ruoyi_headers = None, request_params = None):
        """
        :param request_method: 请求方式
        :param file_name: 文件名称
        :param case_name: 用例名称
        :param mock_method: mock方式 默认或是diy
        :ruoyi_headers: http请求的头部信息,在这里我们传递若依项目的 认证方式
        :request_params: url params参数
        """
        self.request_method = request_method
        self.file_name = file_name
        self.case_name = case_name
        self.mock_method = mock_method
        self.ruoyi_headers = ruoyi_headers
        self.request_params = request_params

    def get_case_data(self):
        """ 获取 mock case的值 """
        if self.mock_method =="diy":
            case_data = MockCase(self.file_name,self.case_name,mock_method="diy").diy_data()
            return case_data
        else:
            case_data = MockCase(self.file_name,self.case_name).diy_data()
            return case_data

    def request_check(self):
        """ 同步请求
        :param case_data: mock case 的值
        :param request_url: yaml 文件的 request_url 请求头, 这里我们做一个host+路由的拼接
        :param request_headers: 若依项目的鉴权机制,在 headers部分：'Authorization': 'Bearer + token'
        :param case_response: yaml 文件的case预期结果
        """
        case_data = self.get_case_data()
        request_url = MARK["base_url"] + case_data["url"]
        case_response = case_data["response_data"]

        with allure.step(
            "同步请求"):  # 判断参数类型 result = [type(i) for i in [case_data["url"], request_url, request_headers, case_data, case_response,response]]
            allure.attach(name="请求库", body=self.request_method)
            allure.attach(name="请求方法", body=case_data["request_method"])
            allure.attach(name="请求接口", body=case_data["url"])
            allure.attach(name="请求地址", body=request_url)
            allure.attach(name="请求头", body=str(self.ruoyi_headers))
            allure.attach(name="用例参数", body=str(case_data))
            allure.attach(name="预期结果", body=str(case_response))

            if self.request_method == "requests":
                response = BaseRequest(address=request_url, case_data=case_data, headers=self.ruoyi_headers,
                                       request_data=None).request_case()

                allure.attach(name="实际结果", body=str(response))

                assert case_response == response  # 对比结果

            elif self.request_method == "httpx":
                response = BaseHttpx(address=request_url, case_data=case_data, headers=self.ruoyi_headers,
                                     request_params=self.request_params,
                                     request_data=None).httpx_case()

                allure.attach(name="实际结果", body=str(response))

                assert case_response == response  # 对比结果


    async def check_arequest(self):
        """ 异步请求的校验结果
        :param actual_results: 实际结果
        :return:
        """
        case_data = self.get_case_data()
        request_url = MARK["base_url"] + case_data["url"]
        case_response = case_data["response_data"]
        with allure.step("异步请求"):
            allure.attach(name="请求库",body=self.request_method)
            allure.attach(name="请求方法", body=case_data["request_method"])
            allure.attach(name="请求接口", body=case_data["url"])
            allure.attach(name="请求地址", body=request_url)
            allure.attach(name="请求头", body=str(self.ruoyi_headers))
            allure.attach(name="用例参数", body=str(case_data))
            allure.attach(name="预期结果", body=str(case_response))
            if self.request_method == "arequests":
                response = await BaseRequest(address=request_url, case_data=case_data, headers=self.ruoyi_headers,request_params=self.request_params,
                                       request_data=None).arequest_case()
                allure.attach(name="实际结果", body=str(response))

                assert case_response == response


            elif self.request_method == "ahttpx":
                response = await BaseHttpx(address=request_url, case_data=case_data, headers=self.ruoyi_headers,request_params=self.request_params,
                                       request_data=None).ahttpx_case()

                #self.output_log(response=response)
                allure.attach(name="实际结果", body=str(response))

                assert case_response == response

            elif self.request_method == "aiohttp":
                response = await BaseAiohttp(address=request_url, case_data=case_data, headers=self.ruoyi_headers,request_params=self.request_params,
                                       request_data=None).aiohttp_case()

                allure.attach(name="实际结果", body=str(response))

                assert case_response == response

# 例子
'''
head ={"Authorization": "Bearer eyJhbGciOiJIUzUxMiJ9.eyJsb2dpbl91c2VyX2tleSI6IjA0ODhjNWJhLWNjOTgtNDQ0MC1hOTM2LTM3MTczMmViYzA3NCJ9.7fDOJMxbq3o8KN5OUO0zY-8ScHF1oOKxhBT5ZtCtlTseK4hmeVNyo1j9lMt8xyXvaCF-Zgkc1OM5f9LRNQRetA",
        "Content-Type": "application/json"}

# m = MockCase('test_mock',"test_02","diy").diy_data()
# print(m)

s = Checks(request_method="aiohttp",file_name='test_mock',case_name='test_04',mock_method="diy",ruoyi_headers=head).check_arequest()
asyncio.run(s)
'''
