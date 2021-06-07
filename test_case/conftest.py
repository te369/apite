import pytest
import simplejson
from core.tool.module_path import TESTCONFIG

'''
@pytest.fixture(scope="session")
def request_method():
    """ 全局传递 用例方法"""
    return request_method

@pytest.fixture(scope="session")
def file_name():
    """ 全局传递 filename yaml文件"""
    return file_name

@pytest.fixture(scope="session")
def case_name():
    """ 全局传递 用例名称"""
    return case_name
'''

@pytest.fixture(scope="session")
def ruoyi():
    """ 全局传递 headers, 若依项目的 鉴权方式 Authorization"""
    auth_path = TESTCONFIG /'ruoyi_auth.json'
    with open(auth_path,'r',encoding="utf-8") as auth:
        ruoyi_auth = simplejson.load(auth)
    return ruoyi_auth


