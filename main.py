"""
项目入口文件
"""
import os
import shutil
import pytest
from core.tool.module_path import TESTCASEDIR,REPORTHTML,REPORTHJSON
from core.base_redis import RedisBase
def clean_report():
    """ 如果 html文件夹存在 则进行删除操作"""
    if os.path.exists(REPORTHTML):
        shutil.rmtree(REPORTHTML)

    if os.path.exists(REPORTHJSON):
        shutil.rmtree(REPORTHJSON)

if __name__ == '__main__':
    """
    前置处理： 
    先查询 redis 的 验证码信息,再发送不同权限的用户登录请求,
    之后将 用户的token 写入 /test/config/ruoyi_auth.json 文件
    再通过 conftest.py 中的 ruoyi() 函数传递若依项目的身份验证信息headers
    
    运行用例：
    0.数据清理通过接口请求清理,根据实际情况,也可以使用sql脚本来执行
    1.清除测试报告 和 测试用例的产生的json数据
    2.再执行pytest 指令,最后执行 allure 指令生成报告"""

    clean_report()
    # pytest 运行指定目录下的 测试文件, 单个用例失败重跑一次,没有设置重跑时间, -n 3进程级别的并发(消耗资源)，生成json 文件到 REPORTHJSON 目录
    cmd_pytest_run= f"pytest {str(TESTCASEDIR)} --reruns 1 -n 3 -s -q --alluredir={str(REPORTHJSON)}"

    cmd_report = f'allure generate {str(REPORTHJSON)} -o {REPORTHTML} --clean' # 生成测试报告,读取用例json文件

    [os.system(i) for i in [cmd_pytest_run, cmd_report]]# 列表解析执行指令

    # allure 渲染指令
    # cd_report = 'cd report & allure serve ./htmljson'
    # os.system(cd_report)














