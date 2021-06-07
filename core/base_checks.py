""" 校验 用例数据的 预期响应结果 与实际接口请求返回的响应结果"""
# import asyncio
import logging
import allure
from .base_requests import BaseRequest
from .base_httpx import BaseHttpx
from .base_aiothttp import BaseAiohttp
from .tool.variable_dict import MARK
from .tool.handle_yaml import HandleYaml



class Check:
    """ 检验 response结果"""

    def __init__(self,request_method=None, file_name=None, case_name=None,ruoyi_headers=None,request_params=None):
        """
        :param request_method: 请求方式
        :param file_name: 文件名称
        :param case_name: 用例名称
        :ruoyi_headers: http请求的头部信息,在这里我们传递若依项目的 认证方式
        :request_params: url params参数
        """
        self.request_method = request_method
        self.file_name = file_name
        self.case_name = case_name
        self.ruoyi_headers = ruoyi_headers
        self.request_params = request_params


    def read_case_content(self):
        """
        :return: 读取 yaml用例数据 返回用例数据
        """
        case_data = HandleYaml('read', self.file_name).base_handle()
        return case_data[self.case_name]


    def output_log(self, response):
        """ 输出 log"""
        case_data = self.read_case_content()
        log_dict = {"请求接口": case_data["url"], "请求方式": case_data["request_method"], "预期数据": case_data["response_data"],
                    "实际响应": response}
        logging.info(log_dict)

    def request_check(self):
        """ 同步请求
        :param case_data: 读取的yaml文件原始字典,使用 用例名称获取结果
        :param request_url: yaml 文件的 request_url 请求头, 这里我们做一个host+路由的拼接
        :param request_headers: 若依项目的鉴权机制,在 headers部分：'Authorization': 'Bearer + token'
        :param case_response: yaml 文件的case预期结果
        """

        case_data = self.read_case_content()
        request_url = MARK["base_url"] + case_data["url"]
        case_response = case_data["response_data"]

        with allure.step("同步请求"): # 判断参数类型 result = [type(i) for i in [case_data["url"], request_url, request_headers, case_data, case_response,response]]
            allure.attach(name="请求库",body=self.request_method)
            allure.attach(name="请求方法", body=case_data["request_method"])
            allure.attach(name="请求接口", body=case_data["url"])
            allure.attach(name="请求地址", body=request_url)
            allure.attach(name="请求头", body=str(self.ruoyi_headers))
            allure.attach(name="用例参数", body=str(case_data))
            allure.attach(name="预期结果", body=str(case_response))
            if self.request_method == "requests":
                response = BaseRequest(address=request_url, case_data=case_data, headers=self.ruoyi_headers,request_data=None).request_case()

                allure.attach(name="实际结果", body=str(response))
                assert case_response == response  # 对比结果

            elif self.request_method == "httpx":
                response = BaseHttpx(address=request_url, case_data=case_data, headers=self.ruoyi_headers,request_params=self.request_params,
                                 request_data=None).httpx_case()

                allure.attach(name="实际结果", body=str(response))
                assert case_response == response  # 对比结果

    async def check_arequest(self):
        """ 异步请求的校验结果
        :param actual_results: 实际结果
        :return:
        """
        case_data = self.read_case_content()
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

# Check例子
'''
HEADERS = {
    'Authorization': 'Bearer eyJhbGciOiJIUzUxMiJ9.eyJsb2dpbl91c2VyX2tleSI6IjMxNjdlODM0LTRmYTAtNGQzMy1iMmE0LTg1NWEwODIzZTc4YSJ9.jvnu4sTehoXg_lIZmP_s7MqNVNNauHnv7-jTTlTWrbGeuaJLEQJCdibu3FmJWHfoZniw4aoDZuHYNJjAvREs1w',
    'Content-Type': 'application/json'
}
# read = Check(file_name='test_base',case_name="test_02").read_case_content()

s = Check(request_method="ahttpx",file_name='test_base',ruoyi_headers=HEADERS,case_name="test_02").check_arequest()

task  = [
    Check(request_method="ahttpx",file_name='test_base',ruoyi_headers=HEADERS,case_name="test_02").check_arequest(),
    Check(request_method="aiohttp",file_name='test_base',ruoyi_headers=HEADERS,case_name="test_02").check_arequest(),
    Check(request_method="ahttpx",file_name='test_base',ruoyi_headers=HEADERS,case_name="test_03").check_arequest(),
    Check(request_method="aiohttp",file_name='test_base',ruoyi_headers=HEADERS,case_name="test_03").check_arequest()
]
asyncio.run(s)
asyncio.run(asyncio.wait(task))
'''