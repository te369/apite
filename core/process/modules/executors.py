""" 执行器 """
import asyncio
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
from threadpool_executor_shrink_able import ThreadPoolExecutorShrinkAble
"""
threadpool_executor_shrink_able
智能的可自动实时调节线程数量的线程池。
此线程池和官方concurrent.futures的线程池 是鸭子类关系，
所以可以一键替换类名 或者 import as来替换类名。 对比官方线程池，有4个创新功能或改进。
"""

MULTI_NUMBER = 10

thread_pool_executor = ThreadPoolExecutor(MULTI_NUMBER) # 线程池执行器
process_pool_executor = ProcessPoolExecutor(MULTI_NUMBER) # 进程池执行器
coroutine_executor = asyncio.get_event_loop() # 协程执行器

"""
        loop = asyncio.get_event_loop()  # 获取事件循环
        future = loop.run_in_executor(async_executor,func)
"""
async_executor = ThreadPoolExecutorShrinkAble(MULTI_NUMBER) #
