""" 封装 requests http请求库"""
import asyncio
import requests
import json
class BaseRequest:
    """ 封装 requestsx请求, 未封装cookies, 若依项目使用 headers 认证:"""
    def __init__(self,address,timeout=5,case_data=None,request_method=None,headers=None,request_data=None,request_params=None,files=None,executor=None):
        """
        :param address: 请求地址
        :param case_data: 测试文件数据
        :param request_method: 请求方法
        :param header: 请求头,视实际情况传参,默认为空
        :param timeout: 超时时间
        :param request_data: 请求数据
        :param request_params= 请求参数
        :param files: 上传文件
        :param:executor : run_in_executor(executor=执行器[线程,进程])
        """
        self.address = address
        self.case_data = case_data
        self.request_method= request_method
        self.headers = headers
        self.timeout = timeout
        self.request_data = request_data
        self.request_params = request_params
        self.files = files
        self.executor = executor

    def response_result(self,response):
        """
        响应结果的校验, request_base(),arequest_base()使用
        :param response: httpx.请求方式
        :return: 返回响应字典
        """

        try:
            base_result = {"status_code": response.status_code, "text": response.text, "json":response.json(),
                      "request": response.request, "content-type": response.headers['content-type']}

            actual_result = {"status_code": response.status_code, "text": response.text, "request": response.request}

            if base_result["json"]["code"] not in [204, 401, 403, 404, 500]: # 若依项目的响应码
                return base_result["json"]# 针对若依项目,可以直接返回 json格式
            else:
                return actual_result


        except json.decoder.JSONDecodeError as json_error:
            return {"json_error": json_error}


    def request_base(self):
        """ 同步的 requests 库, 传入request_method 请求方式 """
        try:
            if self.request_method =="get":
                response = requests.request("GET",url=self.address,headers=self.headers,params=self.request_params,timeout=self.timeout)

            elif self.request_method =="post":
                response = requests.request("POST", url=self.address,headers=self.headers,data=self.request_data,files=self.files,timeout=self.timeout)

            elif self.request_method =="put":
                response = requests.request("PUT", url=self.address,headers=self.headers,data=self.request_data,timeout=self.timeout)

            elif self.request_method =="delete":
                response = requests.request("DELETE", url=self.address,headers=self.headers,timeout=self.timeout)

            return self.response_result(response)

        except requests.exceptions.ConnectTimeout as timeout:
            return {"ConnectTimeout":timeout} # 连接超时

        except requests.exceptions.ConnectionError as link_error:
            return {"ConnectionError":link_error} # 连接失败,url,或其他

    def request_case(self):
        """ 同步的 requests case  """
        try:
            if self.case_data["request_method"] =="get":
                response = requests.request("GET", url=self.address, headers=self.headers, timeout=self.timeout)

            elif  self.case_data["request_method"] =="get_send":
                response = requests.request("GET",url=self.address,headers=self.headers,params=self.case_data["url_params"],timeout=self.timeout)

            elif self.case_data["request_method"] =="post":
                response = requests.request("POST", url=self.address,headers=self.headers,data=json.dumps(self.case_data["send_params"]),files=self.files,timeout=self.timeout)

            elif self.case_data["request_method"] =="put":
                response = requests.request("PUT", url=self.address,headers=self.headers,data=json.dumps(self.case_data["send_params"]),timeout=self.timeout)

            elif self.case_data["request_method"] =="delete":

                response = requests.request("DELETE", url=self.address,headers=self.headers,timeout=self.timeout)

            return response.json() # 若依项目直接返回JSON,做为case校验结果

        except requests.exceptions.ConnectTimeout as timeout:
            return {"ConnectTimeout":timeout} # 连接超时

        except requests.exceptions.ConnectionError as link_error:
            return {"ConnectionError":link_error} # 连接失败,url,或其他

    async def arequest_base(self):
        """ 异步的 requests 请求 """
        loop = asyncio.get_event_loop() # 获取事件循环

        future = loop.run_in_executor(self.executor,self.request_base)# future 可等待对象
        response = await future

        return response

    async def arequest_case(self):
        """ 异步的 requests case"""
        loop = asyncio.get_event_loop()  # 获取事件循环

        future = loop.run_in_executor(self.executor, self.request_case)  # future 可等待对象
        response = await future

        return response

# 例子
"""
case = {'url': 'system/user/list', 'request_method': 'get_send', 'url_params': {'pageNum': '1', 'pageSize': '10', 'userName': '101', 'phonenumber': '180', 'status': '0', 'params[beginTime]': '2020-06-04', 'params[endTime]': '2021-06-03', 'page': '1'}, 'response_data': {'total': 0, 'rows': [], 'code': 200, 'msg': '查询成功'}}
url = " http://noway.ren/prod-api/"+case["url"]
request_method= case["request_method"]
case_response = case["response_data"]
HEADERS = {
    'Authorization': 'Bearer eyJhbGciOiJIUzUxMiJ9.eyJsb2dpbl91c2VyX2tleSI6IjMxNjdlODM0LTRmYTAtNGQzMy1iMmE0LTg1NWEwODIzZTc4YSJ9.jvnu4sTehoXg_lIZmP_s7MqNVNNauHnv7-jTTlTWrbGeuaJLEQJCdibu3FmJWHfoZniw4aoDZuHYNJjAvREs1w',
    'Content-Type': 'application/json'
}
s = BaseRequest(address=url,case_data=case,request_method=request_method,headers=HEADERS).request_case()
"""