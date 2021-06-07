"""调度器"""
import asyncio

import requests
from modules.async_case import Coroutine
from modules.executors import async_executor
class Scheduler:
    def __init__(self,address,send_data):
        """
        :param executor: 执行器
        :param address: 网址
        :param send_data: 发送的数据
        """
        self.executor = async_executor
        self.address = address
        self.send_data = send_data

    async def te_func(self):
        """测试函数 测试Coroutine的 requests post方法"""
        return await Coroutine().sync_executor(self.executor,self.address, self.send_data)


'''
address = "https://httpbin.org/post"
send_data = {"args": {},}

S = Scheduler(address,send_data).te_func()
asyncio.run(S)
'''


