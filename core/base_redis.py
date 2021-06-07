import asyncio
import json
from functools import partial

import aioredis
import requests

class RedisBase:
    _redis = None
    def __init__(self,redis_address,redis_password):
        """
        :param redis_address:  redis地址
        :param redis_password: redis密码
        """
        self.redis_address = redis_address
        self.redis_password = redis_password

    async def get_redis(self):
        """ 当redis 不为空时,创建连接并返回,若以项目db=0"""
        if not self._redis:
            self._redis = await aioredis.create_redis_pool(address=self.redis_address, password=self.redis_password, db=0,
                                                           encoding="utf-8")
        return self._redis

    async def close(self):
        """关闭redis连接 """
        if self._redis:
            self._redis.close()

    async def get_captcha(self, key):
        """ 获取redis验证码结果
            请求验证码接口,获取 uuid,连接redis,get 查询 captcha_codes:uuid
            之后关闭连接
        :param key: 传入要查询的key值
        :param uuid: 生成验证码会产生uuid
        :param captcha: 验证码答案
        :return: {uuid , captcha}
        """
        uuid = requests.get("http://noway.ren/prod-api/captchaImage").json()["uuid"]

        redis = await self.get_redis() # 网络io操作：创建 redis 链接

        captcha = await redis.get(key + ":" + uuid)# 网络IO 操作: get captcha_codes:uuid

        result = {"uuid": uuid, "captcha": captcha} # 请求结果
        return result

        await self.close() # 关闭 redis 连接



    async def get_login_token(self):
        """ 请求登录 获取token,先获取 redis验证码 和uuid 调用登录接口"""
        result = await self.get_captcha("captcha_codes")
        code = result["captcha"].replace('"', "")
        uuid = result["uuid"]

        payload = json.dumps({
            "username": "te123",
            "password": "123456",
            "code": code,
            "uuid": uuid
        })

        url = "http://noway.ren/prod-api/login"
        headers = {
            'Content-Type': 'application/json'
        }

        loop = asyncio.get_event_loop()
        # 可等待对象
        future = loop.run_in_executor(None, partial(requests.post, url=url, headers=headers, data=payload))
        token = await future

        return token.json()["token"]


    async def get_info(self):
        """ get请求 例子"""
        url = "http://noway.ren/prod-api/getInfo"
        token = await self.get_login_token()
        Bearer = ("Bearer " + token)
        headers = {
            'Content-Type': 'application/json',
            "Authorization": Bearer}
        response = requests.request("GET", url, headers=headers).json()

        return response


"""
redis1 = RedisBase(redis_address="",redis_password="")
redis2 = RedisBase(redis_address="",redis_password="")
task_list = [
    redis1.get_login_token(),
    redis2.get_login_token()
]
asyncio.run(asyncio.wait(task_list))
"""