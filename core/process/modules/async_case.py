import asyncio
from functools import partial
import requests
class Coroutine:
    async def sync_executor(self,executor,url=None, data=None):
        """
        request 异步的例子
        :param executor: 执行器
        :param url: url
        :param data: 发送的参数
        :return: json的响应数据
        """
        """ run_in_executor(执行器,func,kwargs)"""
        loop = asyncio.get_event_loop() # 生成 或获取一个事件循环
        future = loop.run_in_executor(executor, partial(requests.post, url=url,data=data))
        response = await future # 可等待对象
        return response.json()
