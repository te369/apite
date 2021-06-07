import pytest
import allure
from core.mock_case import Checks
@allure.feature("api mock 测试")
class TestUseMock:
    @allure.story("用户管理模块")
    @allure.title("REQUESTS-DIY 用户管理-用户查询功能")
    def test_01(self,ruoyi,request_method="requests",file_name='test_mock',case_name="test_02",mock_method="diy"):
        """ 输入 部门名称，用户名称，手机号码，状态，创建时间 来 查询用户信息"""
        Checks(request_method,file_name,case_name, mock_method,ruoyi_headers=ruoyi).request_check()

    @allure.story("用户管理模块")
    @allure.title("HTTPX-DIY 用户管理-用户查询功能")
    def test_02(self,ruoyi,request_method="httpx",file_name='test_mock',case_name="test_02",mock_method="diy"):
        """ 输入 部门名称，用户名称，手机号码，状态，创建时间 来 查询用户信息"""
        Checks(request_method,file_name,case_name, mock_method,ruoyi_headers=ruoyi).request_check()

    @allure.story("用户管理模块")
    @allure.title("REQUESTS 用户管理-用户查询功能")
    def test_03(self,ruoyi,request_method="requests",file_name='test_mock',case_name="test_03"):
        """ 输入 部门名称，用户名称，手机号码，状态，创建时间 来 查询用户信息"""
        Checks(request_method,file_name,case_name,ruoyi_headers=ruoyi).request_check()

    @allure.story("用户管理模块")
    @allure.title("HTTPX 用户管理-用户查询功能")
    def test_04(self,ruoyi,request_method="httpx",file_name='test_mock',case_name="test_03"):
        """ 输入 部门名称，用户名称，手机号码，状态，创建时间 来 查询用户信息"""
        Checks(request_method,file_name,case_name,ruoyi_headers=ruoyi).request_check()


if __name__ == '__main__':
    pytest.main(['-s','test_mock.py'])