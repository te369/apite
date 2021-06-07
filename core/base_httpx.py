""" 封装 httpx http请求库
    httpx 与 requests 语法相似, 支持异步
    支持 http2
"""
import json
import httpx

class BaseHttpx:
    """ 封装 Httpx 请求"""
    def __init__(self,address,timeout=5,case_data=None,request_method=None,headers=None,request_data=None,request_params=None,files=None):
        """
        :param address: 请求地址
        :param timeout: 超时时间
        :param case_data : 测试文件数据
        :param request_method: 请求方法
        :param header: 请求头,视实际情况传参,默认为空
        :param request_data: 请求数据
        :param request_params: 请求参数
        :param files: 上传文件
        :param client: httpx 客户端
        :param async_client: httpx 异步客户端
        """
        self.address = address
        self.timeout = timeout
        self.case_data = case_data
        self.request_method = request_method
        self.headers = headers
        self.request_data = request_data
        self.request_params = request_params
        self.files = files
        self.client = httpx.Client()
        self.async_client = httpx.AsyncClient()

    def response_result(self,response):
        """
        :param response: httpx.请求方式
        :return: 返回响应字典
        """
        try:
            base_result = {"status_code": response.status_code, "text": response.text, "json":response.json(),
                      "request": response.request, "content-type": response.headers['content-type']}

            actual_result = {"status_code": response.status_code, "text": response.text, "request": response.request}

            if base_result["json"]["code"] not in [204, 401, 403, 404, 500]:
                return base_result["json"] # 针对若依项目,可以直接返回 json格式
            else:
                return actual_result

        except json.decoder.JSONDecodeError as json_error:
            return {"json_error": json_error}

    def httpx_base(self):
        """ httpx 请求 """
        with self.client as client:
            try:
                if self.request_method == "get":
                    response = client.get(url=self.address,headers=self.headers,params=self.request_params,timeout=self.timeout)

                elif self.request_method =="post":
                    response = client.post(url=self.address, headers=self.headers, data=self.request_data, files=self.files,timeout=self.timeout)

                elif self.request_method == "put":
                    response = client.put(url=self.address, headers=self.headers, data=self.request_data,timeout=self.timeout)

                elif self.request_method == "delete":
                    """ delete请求 若依项目 删除方法 是在 url 拼接参数 如: DELETE http://noway.ren/prod-api/system/post/5"""

                    response = client.delete(url=self.address,headers=self.headers,
                                             timeout=self.timeout)  # response = httpx.delete(url=self.address,headers=self.header,params=self.request_data,timeout=self.timeout)

                return self.response_result(response)
            # httpx.RequestError 超级类 except httpx.RequestError as exc: return {"url_error":exc.request.url}...

            except httpx.ConnectError as connect_error: # 连接失败
                return {"ConnectError":connect_error}

            except httpx.ConnectTimeout as timeout: # 连接超时
                return {"ConnectTimeout":timeout}

    def httpx_case(self):
        """ httpx 发送 case 数据，先判断 case_dict["request_method"] 的方法 再进行相应请求"""
        with self.client as client:
            try:
                if self.case_data["request_method"] == "get":
                    response = client.get(url=self.address,headers=self.headers,timeout=self.timeout)

                elif self.case_data["request_method"] == "get_send":
                    response = client.get(url=self.address, headers=self.headers, params=self.case_data["url_params"],timeout=self.timeout)

                elif self.case_data["request_method"] =="post":
                    response = client.post(url=self.address, headers=self.headers, data=json.dumps(self.case_data["send_params"]), files=self.files,timeout=self.timeout)

                elif self.case_data["request_method"] == "put":
                    response = client.put(url=self.address, headers=self.headers, data=json.dumps(self.case_data["send_params"]),timeout=self.timeout)

                elif self.case_data["request_method"] == "delete":
                    """ delete请求 若依项目 删除方法 是在 url 拼接参数 如: DELETE http://noway.ren/prod-api/system/post/5"""

                    response = client.delete(url=self.address,headers=self.headers,
                                             timeout=self.timeout)  # response = httpx.delete(url=self.address,headers=self.header,params=self.request_data,timeout=self.timeout)

                return response.json()

            except httpx.ConnectError as connect_error: # 连接失败
                return {"ConnectError":connect_error}

            except httpx.ConnectTimeout as timeout: # 连接超时
                return {"ConnectTimeout":timeout}


    async def ahttpx_base(self):
        """ httpx 异步请求"""
        try:
            async with self.async_client as client:
                if self.request_method == "get":
                    response = await client.get(url=self.address,headers=self.headers,params=self.request_params,timeout=self.timeout)

                elif self.request_method == "post":
                    response = await client.post(url=self.address, headers=self.headers, data=self.request_data,
                                                 files=self.files, timeout=self.timeout)

                elif self.request_method == "put":
                    response = await client.put(url=self.address, headers=self.headers, data=self.request_data,
                                                timeout=self.timeout)

                elif self.request_method == "delete":
                    response = await client.delete(url=self.address,headers=self.headers,
                                                   timeout=self.timeout)
                return self.response_result(response)

        except httpx.ReadError as read_error:
            return {"ReadError":read_error} # 如 指定的网络名不再可用

        except httpx.ConnectError as connect_error: # 连接失败
            return {"ConnectError":connect_error}

        except httpx.ConnectTimeout as timeout: # 超时
            return {"ConnectTimeout":timeout}

    async def ahttpx_case(self):
        """ httpx 异步请求 发送case"""
        try:
            async with self.async_client as client:
                if self.case_data["request_method"] == "get":
                    response = await client.get(url=self.address,headers=self.headers,timeout=self.timeout)

                elif self.case_data["request_method"] == "get_send":
                    response = await client.get(url=self.address,headers=self.headers,timeout=self.timeout,params=self.case_data["url_params"])


                elif self.case_data["request_method"] == "post":
                    response = await client.post(url=self.address, headers=self.headers, data=json.dumps(self.case_data["send_params"]),
                                                 files=self.files, timeout=self.timeout)

                elif self.case_data["request_method"] == "put":
                    response = await client.put(url=self.address, headers=self.headers, data=json.dumps(self.case_data["send_params"]),
                                                timeout=self.timeout)

                elif self.case_data["request_method"] == "delete":
                    response = await client.delete(url=self.address,headers=self.headers,
                                                   timeout=self.timeout)
                return response.json()

        except httpx.ReadError as read_error:
            return {"ReadError":read_error} # 如 指定的网络名不再可用

        except httpx.ConnectError as connect_error: # 连接失败
            return {"ConnectError":connect_error}

        except httpx.ConnectTimeout as timeout: # 超时
            return {"ConnectTimeout":timeout}