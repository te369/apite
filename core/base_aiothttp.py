""" 封装 aiohttp 异步http请求库 """
import json
import aiohttp

class BaseAiohttp:
    """ 封装 aiohttp 请求"""
    def __init__(self,address,timeout=5,case_data=None,request_method=None,headers=None,request_data=None,request_params=None,files=None):
        """
        :param address: 请求地址
        :param request_method: 请求方法
        :param case_data : 测试文件数据
        :param headers: 请求头,视实际情况传参,默认为空
        :param request_data: 请求数据
        :param request_params : 请求参数
        :param timeout: 超时时间
        :param files: 上传文件
        """
        self.address = address
        self.case_data = case_data
        self.request_method = request_method
        self.timeout = timeout
        self.headers = headers
        self.request_data = request_data
        self.request_params = request_params
        self.files = files

    async def response_result(self,response):
        """
        :param response: httpx.请求方式
        :return: 返回响应字典
        """

        try:
            base_result = {"status_code": response.status, "text": await response.text(),"json":await response.json(),
                      "request": response.request_info}

            actual_result = {"status_code": response.status, "text":await response.text(), "request": response.request_info}

            if base_result["json"]["code"] not in [204, 401, 403, 404, 500]: # 若依项目的响应码

                return base_result["json"] # 针对若依项目,可以直接返回 json格式
            else:
                return actual_result

        except json.decoder.JSONDecodeError as json_error:
            return {"json_error": json_error}

    async def aiohttp_base(self):
        """ aiohttp 请求 """
        async with aiohttp.ClientSession(headers=self.headers) as session: # headers 设置为全局 ,为了方便
            if self.request_method == "get":
                response = await session.get(url=self.address,timeout=self.timeout)

            elif self.request_method == "get_send":
                response = await session.get(url=self.address, params=self.request_params, timeout=self.timeout)

            elif self.request_method == "post_json":
                response = await session.post(url=self.address,json=self.request_data,timeout=self.timeout, )

            elif self.request_method == "post_data":
                response = await session.post(url=self.address, data=self.request_data, timeout=self.timeout,)

            elif self.request_method == "put":
                response = await session.put(url=self.address, data=self.request_data, timeout=self.timeout, )

            elif self.request_method == "delete":
                response = await session.delete(url=self.address)

            return await self.response_result(response)

    async def aiohttp_case(self):
        """ aiohttp case
        1. 激活客户端
        2. 判断测试数据中的请求方式,进行响应操作
        3. 将结果以 json 格式返回
        """
        async with aiohttp.ClientSession(headers=self.headers) as session:
            if self.case_data["request_method"] == "get":
                response = await session.get(url=self.address,timeout=self.timeout)
                return await response.json()

            elif self.case_data["request_method"] == "get_send":
                response = await session.get(url=self.address, params=self.case_data["url_params"], timeout=self.timeout)
                return await response.json()

            elif self.case_data["request_method"] == "post":
                response = await session.post(url=self.address, json=self.case_data["send_params"],timeout=self.timeout)
                return await response.json()

            # elif self.request_method == "post_data": # 这里post 和 put 参数 直接使用 json格式传递
            #     response = await session.post(url=self.address, timeout=self.timeout, data=self.request_data)

            elif self.case_data["request_method"] == "put":
                response = await session.put(url=self.address, json=self.case_data["send_params"],timeout=self.timeout)
                return await response.json()

            elif self.case_data["request_method"] == "delete":
                response = await session.delete(url=self.address)
                return await response.json()