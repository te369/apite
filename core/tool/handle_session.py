""" 操作 fiddler 会话 读取信息 并写入"""
import json
from urllib import parse
from core.tool.module_path import SESSIONTXTDIR
from core.tool.variable_dict import MARK,METHOD
from .handle_yaml import HandleYaml

class HandleSession:
    """ 快速写数据用例
        读取Fiddler 抓包的session 文本信息, 写入session 为 yaml文件格式的用例数据"""
    def __init__(self,file_name=None,handle_method=None,write_method=None,write_file=None):
        """
        :param file_name: fiddler session 文件名称 也是写入名称
        :param handle_method: 操作方法
        :param write_file: yaml 写入文件名称
        """
        self.file_name = file_name
        self.handle_method = handle_method
        self.write_method = write_method

    def writedata(self,data):
        """ 写入文件 """
        HandleYaml(self.write_method,self.file_name,data).base_handle()

    def send_params(self,session):
        """ request 发送的参数
        :param session: 单个会话
        :param params: 截取从Cookie: 到  HTTP/1.1 200 之间的参数内容
        :param params_json: 发送参数：{"deptId":105,"userName":"test_use"},移除 { 左侧信息
        :param params_dict: 将 参数转化为 字典格式, 便于 yaml 文件写入
        :return: params_dict
        """
        params = session.split(MARK["body_head"])[1].split(MARK["body_tail"])[0]
        params_json = params.replace(params.split('{')[0], "")# 没有移除\n 因为我们text中有换行
        params_dict = json.loads(params_json)
        return params_dict

    def response_content(self,session):
        """ response 响应信息
        :param session: 单个会话
        :param response: 从 Expires: 0 向下标记到会话结束
        :param response_json: 响应信息{"msg":"操作成功","code":200}, 移除 { 左侧信息
        :param response_dict: 将 response_json 转化为字典格式 便于 yaml 文件写入
        :return: response_dict
        """
        response = session.split(MARK["raw_head"])[1]
        response_json = response.replace(response.split('{')[0], "")
        response_dict = json.loads(response_json)
        return response_dict


    def process(self,session,case_number):
        """ 判断用例请求,并写入yaml文件
        在下标中 0 代表当前位置 的 前面部分, 1 代表 后面部分,下面是参数的意义
        :param session: 传入文本信息
        :param case_number: 用例编号
        :param case_number: 这是一条用例名称拼接, test_0+ str (range循环) 结果为 test_01,test02
        :return: 生成 yaml文件
        """
        case_number = "test_0" + str(case_number + 1)
        if METHOD["get"] in session:
            url = session.split(METHOD["get"])[1].split(MARK["head"])[0].split(MARK["base_url"])[1].rstrip()
            params_url = url.split("?")[0]
            response_dict = self.response_content(session)
            """ 1.判断 Get 请求是否有参数,先将? 代替为&,
                2.接着判断url中有几个参数,循环取出key和value
                3.拼接字典
                """
            if "?" in url:

                params_params = url.replace("?", "&")
                params_num = [i for i in range(params_params.count("&"))]

                params = {
                    f'{params_params.split("&")[i + 1].split("=")[0]}': f'{params_params.split("&")[i + 1].split("=")[1]}'
                    for i in params_num}

                case = {case_number: {"url": params_url, "request_method": "get_send", "url_params": params,
                                    "response_data": response_dict}}
                self.writedata(case)

            else:
                case = {case_number: {"url": url, "request_method": "get", "response_data": response_dict}}
                self.writedata(case)


        elif METHOD["post"] in session:
            url = session.split(METHOD["post"])[1].split(MARK["head"])[0].split(MARK["base_url"])[1].rstrip()
            params_dict = self.send_params(session)
            response_dict = self.response_content(session)
            case = {case_number: {"url": url, "request_method": "post", "send_params":params_dict,"response_data": response_dict}}
            self.writedata(case)


        elif METHOD["put"] in session:
            url = session.split(METHOD["put"])[1].split(MARK["head"])[0].split(MARK["base_url"])[1].rstrip()
            params_dict = self.send_params(session)
            response_dict = self.response_content(session)
            case = {case_number: {"url": url, "request_method": "put", "send_params": params_dict,
                                  "response_data": response_dict}}
            self.writedata(case)

        elif METHOD["delete"] in session:
            url = session.split(METHOD["delete"])[1].split(MARK["head"])[0].split(MARK["base_url"])[1].rstrip()
            response_dict = self.response_content(session)
            case = {case_number: {"url": url, "request_method": "delete", "response_data": response_dict}}
            self.writedata(case)

    def base_handle(self):
        """ 操作fiddler会话
        1. 获取文件路径,并读取信息
        2. 先获取用例数,之后 将 用例文本分割为单个
        3. 判断 请求方式 get,post,put,delete, 再次分割会话
        4. 根据请求会话, 区别操作,之后写入 yaml 文件
        """
        file_name = SESSIONTXTDIR /f"{self.file_name}.txt"
        with open(file_name, "rt", encoding="utf-8") as file:
            file = file.read()
            session_num = file.count(MARK["session_num"]) # 判断用例数
            decoding_file = parse.unquote(file) # 解码session信息
            if self.handle_method =="read":
                return file
            elif self.handle_method == "read_session_num":
                return session_num
            else:

                session_num = decoding_file.count(MARK["session_num"]) # 判断用例数
                for i in range(session_num):
                    session = decoding_file.split(MARK["session_mark"])[i] # 分割为单个会话

                    self.process(session=session, case_number=i)

# 例子
"""
if __name__ == '__main__':
    #HandleSession(file_name='test_base',handle_method="read").base_handle()
    # HandleSession(file_name='test_base',write_method='write').base_handle()
"""

