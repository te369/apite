""" 常用的装饰器 """
import time
from functools import wraps
from functools import partial
from concurrent import futures
class BaseDecorator:
    """ 装饰器类 """
    def base_decorator(self,func):
        """ 闭包 返回函数"""
        @wraps(func)
        def func_result(*args,**kwargs):
            func(*args,**kwargs)
        return func_result

    def func_time(func):
        """ 装饰器 测试程序运行时间"""
        timer = Timer()
        @wraps(func)
        def warpper(*args, **kwargs):
            # timer = Timer()
            timer.func_start_time()
            func(*args, **kwargs)
            timer.func_end_time()
        return warpper

class Timer:
    """ 计时器函数"""
    def __init__(self):
        self.val = 0

    def func_start_time(self):
        """ 程序开始时间"""
        self.val = time.time()

    def func_end_time(self):
        """ 程序结束时间"""
        end_time = round(time.time() - self.val, 6)
        print(f'程序运行时间为: {end_time}s')

class Allow_Count:
    """约束函数运行次数
    来源：https://mp.weixin.qq.com/s/Qs5Un3_-4EHfLsLVFL1rYQ
    """
    def __init__(self, count):
        self.count = count
        self.i = 0

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kw):
            if self.i >= self.count:
                return
            self.i += 1
            return func(*args, **kw)
        return wrapper

class Timeout:
    """函数超时退出"""
    __executor = futures.ThreadPoolExecutor(5)

    def __init__(self, seconds):
        self.seconds = seconds

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kw):
            future = Timeout.__executor.submit(func, *args, **kw)
            return future.result(timeout=self.seconds)
        return wrapper