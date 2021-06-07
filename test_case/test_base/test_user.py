import pytest
import allure
from core.base_checks import Check
@allure.feature("api测试")
class TestUse:
    @allure.story("用户管理模块")
    @allure.title("REQUESTS 登录成功,首页获取路由信息")
    def test_01(self,ruoyi,request_method="requests",file_name='test_user',case_name="test_01"):
        """ headers权限认证成功,返回路由信息 """
        Check(request_method, file_name,case_name,ruoyi_headers=ruoyi).request_check()


    @allure.story("用户管理模块")
    @allure.title("REQUESTS 用户管理-用户查询功能")
    def test_02(self,ruoyi,request_method="requests",file_name='test_user',case_name="test_02"):
        """ 输入 部门名称，用户名称，手机号码，状态，创建时间 来 查询用户信息"""
        Check(request_method, file_name,case_name,ruoyi_headers=ruoyi).request_check()

    @allure.story("用户管理模块")
    @allure.title("REQUESTS 用户管理-新增用户功能")
    def test_03(self,ruoyi,request_method="requests",file_name='test_user',case_name="test_03"):
        """ 输入已存在的 用户昵称，归属部门，手机号码，邮箱，用户名称，用户密码，用户性别，状态，岗位，角色，备注 来添加用户
            返回 新增失败
        """
        Check(request_method, file_name,case_name,ruoyi_headers=ruoyi).request_check()

    @allure.story("用户管理模块")
    @allure.title("REQUESTS 用户管理-修改用户信息功能")
    def test_04(self,ruoyi,request_method="requests",file_name='test_user',case_name="test_04"):
        """ 修改用户备注信息,提示修改成功"""
        Check(request_method, file_name,case_name,ruoyi_headers=ruoyi).request_check()

    @allure.story("用户管理模块")
    @allure.title("REQUESTS 用户管理-删除用户信息功能")
    def test_05(self,ruoyi,request_method="requests",file_name='test_user',case_name="test_05"):
        """ 通过url 传入用户参数 ,删除用户"""
        Check(request_method, file_name,case_name,ruoyi_headers=ruoyi).request_check()

    @allure.story("用户管理模块")
    @allure.title("HTTPX 登录成功,首页获取路由信息")
    def test_06(self,ruoyi,request_method="httpx",file_name='test_user',case_name="test_01"):
        """ headers权限认证成功,返回路由信息 """
        Check(request_method, file_name,case_name,ruoyi_headers=ruoyi).request_check()


    @allure.story("用户管理模块")
    @allure.title("HTTPX 用户管理-用户查询功能")
    def test_07(self,ruoyi,request_method="httpx",file_name='test_user',case_name="test_02"):
        """ 输入 部门名称，用户名称，手机号码，状态，创建时间 来 查询用户信息"""
        Check(request_method, file_name,case_name,ruoyi_headers=ruoyi).request_check()

    @allure.story("用户管理模块")
    @allure.title("HTTPX 用户管理-新增用户功能")
    def test_08(self,ruoyi,request_method="httpx",file_name='test_user',case_name="test_03"):
        """ 输入已存在的 用户昵称，归属部门，手机号码，邮箱，用户名称，用户密码，用户性别，状态，岗位，角色，备注 来添加用户
            返回 新增失败
        """
        Check(request_method, file_name,case_name,ruoyi_headers=ruoyi).request_check()

    @allure.story("用户管理模块")
    @allure.title("HTTPX 用户管理-修改用户信息功能")
    def test_09(self,ruoyi,request_method="httpx",file_name='test_user',case_name="test_04"):
        """ 修改用户备注信息,提示修改成功"""
        Check(request_method, file_name,case_name,ruoyi_headers=ruoyi).request_check()

    @allure.story("用户管理模块")
    @allure.title("HTTPX 用户管理-删除用户信息功能")
    def test_10(self,ruoyi,request_method="httpx",file_name='test_user',case_name="test_05"):
        """ 通过url 传入用户参数 ,删除用户"""
        Check(request_method, file_name,case_name,ruoyi_headers=ruoyi).request_check()

    @allure.story("用户管理模块")
    @allure.title("REQUESTS异步 用户管理-用户查询功能")
    @pytest.mark.asyncio
    async def test_11(self,ruoyi,request_method="arequests",file_name='test_user',case_name="test_01"):
        await Check(request_method, file_name, case_name,ruoyi_headers=ruoyi).check_arequest()

    @allure.story("用户管理模块")
    @allure.title("REQUESTS异步 用户管理-用户查询功能")
    @pytest.mark.asyncio
    async def test_12(self,ruoyi,request_method="arequests",file_name='test_user',case_name="test_02"):
        await Check(request_method, file_name, case_name,ruoyi_headers=ruoyi).check_arequest()

    @allure.story("用户管理模块")
    @allure.title("REQUESTS异步 用户管理-新增用户功能")
    @pytest.mark.asyncio
    async def test_13(self,ruoyi,request_method="arequests",file_name='test_user',case_name="test_03"):
        await Check(request_method, file_name, case_name,ruoyi_headers=ruoyi).check_arequest()

    @allure.story("用户管理模块")
    @allure.title("REQUESTS异步 用户管理-修改用户信息功能")
    @pytest.mark.asyncio
    async def test_14(self,ruoyi,request_method="arequests",file_name='test_user',case_name="test_04"):
        await Check(request_method, file_name, case_name,ruoyi_headers=ruoyi).check_arequest()

    @allure.story("用户管理模块")
    @allure.title("REQUESTS异步 用户管理-删除用户信息功能")
    @pytest.mark.asyncio
    async def test_15(self,ruoyi,request_method="arequests",file_name='test_user',case_name="test_05"):
        await Check(request_method, file_name, case_name,ruoyi_headers=ruoyi).check_arequest()

    @allure.story("用户管理模块")
    @allure.title("HTTPX异步 登录成功,首页获取路由信息")
    @pytest.mark.asyncio
    async def test_16(self,ruoyi,request_method="ahttpx",file_name='test_user',case_name="test_01"):
        await Check(request_method, file_name, case_name,ruoyi_headers=ruoyi).check_arequest()

    @allure.story("用户管理模块")
    @allure.title("HTTPX异步 用户管理-删除用户信息功能")
    @pytest.mark.asyncio
    async def test_17(self,ruoyi,request_method="ahttpx",file_name='test_user',case_name="test_02"):
        await Check(request_method, file_name, case_name,ruoyi_headers=ruoyi).check_arequest()

    @allure.story("用户管理模块")
    @allure.title("HTTPX异步 用户管理-新增用户功能")
    @pytest.mark.asyncio
    async def test_18(self,ruoyi,request_method="ahttpx",file_name='test_user',case_name="test_03"):
        await Check(request_method, file_name, case_name,ruoyi_headers=ruoyi).check_arequest()

    @allure.story("用户管理模块")
    @allure.title("HTTPX异步 用户管理-修改用户信息功能")
    @pytest.mark.asyncio
    async def test_19(self,ruoyi,request_method="ahttpx",file_name='test_user',case_name="test_04"):
        await Check(request_method, file_name, case_name,ruoyi_headers=ruoyi).check_arequest()

    @allure.story("用户管理模块")
    @allure.title("HTTPX异步 用户管理-删除用户信息功能")
    @pytest.mark.asyncio
    async def test_20(self,ruoyi,request_method="ahttpx",file_name='test_user',case_name="test_05"):
        await Check(request_method, file_name, case_name,ruoyi_headers=ruoyi).check_arequest()

    @allure.story("用户管理模块")
    @allure.title("AIOHTTP 登录成功,首页获取路由信息")
    @pytest.mark.asyncio
    async def test_21(self,ruoyi,request_method="aiohttp",file_name='test_user',case_name="test_01"):
        await Check(request_method, file_name, case_name,ruoyi_headers=ruoyi).check_arequest()

    @allure.story("用户管理模块")
    @allure.title("AIOHTTP 用户管理-用户查询功能")
    @pytest.mark.asyncio
    async def test_22(self,ruoyi,request_method="aiohttp",file_name='test_user',case_name="test_02"):
        await Check(request_method, file_name, case_name,ruoyi_headers=ruoyi).check_arequest()

    @allure.story("用户管理模块")
    @allure.title("AIOHTTP 用户管理-新增用户功能")
    @pytest.mark.asyncio
    async def test_23(self,ruoyi,request_method="aiohttp",file_name='test_user',case_name="test_03"):
        await Check(request_method, file_name, case_name,ruoyi_headers=ruoyi).check_arequest()

    @allure.story("用户管理模块")
    @allure.title("HTTPX 用户管理-修改用户信息功能")
    @pytest.mark.asyncio
    async def test_24(self,ruoyi,request_method="aiohttp",file_name='test_user',case_name="test_04"):
        await Check(request_method, file_name, case_name,ruoyi_headers=ruoyi).check_arequest()

    @allure.title("HTTPX 用户管理-修改用户信息功能")
    @allure.story("用户管理模块")
    @allure.title("HTTPX 用户管理-删除用户信息功能")
    @pytest.mark.asyncio
    async def test_25(self,ruoyi,request_method="aiohttp",file_name='test_user',case_name="test_05"):
        await Check(request_method, file_name, case_name,ruoyi_headers=ruoyi).check_arequest()

if __name__ == '__main__':
    pytest.main(['-s','test_user.py'])
