""" 写 pytest case """
from tool.handle_session import HandleSession
from tool.module_path import TESTCASEDIR
class WriteCase:
    def __init__(self,file_name=None,case_str_dict=None,request_name=None,write_method=None):
        """
        :param file_name: 是session 名称 也是 写入yaml文件的名称, 也是pytest 用例文件的名称
        :param case_str_dict: case字典 case_str_dict={"classname":"use","feature":"api测试","story":"用户管理模块","title":"REQUESTS 登录成功,首页获取路由信息"}
        :param request_method: 请求库名称
        :param write_method: 写入方式 追加 或是覆盖
        """
        self.case_str_dict = case_str_dict
        self.request_name = request_name
        self.file_name = file_name
        self.write_method = write_method



    def case_import(self):
        """ pytest 用例头文件 :
        import pytest
        import allure
        from core.base_checks import Check
        @allure.feature("api测试")

        """
        case_head = f'import pytest' \
                    f'\nimport allure' \
                    f'\nfrom core.base_checks import Check' \
                    f'\n@allure.feature("{self.case_str_dict["feature"]}")' \
                    f'\nclass Test{self.case_str_dict["classname"]}:\n'
        return case_head


    def case_self(self,case_num):
        """ pytest 测试函数: case_num 是 i for i  in range(session会话数)
        @allure.story("用户管理模块")
        @allure.title("RE")
        def test_1(self, ruoyi,request_method="requests", file_name="test_base", case_name="test_1"):
            Check(request_method, file_name,case_name,ruoyi_headers=ruoyi).request_check()

        """
        case_name = f"test_0{case_num}" # 用例名称
        space= "    " # 4个空格
        case_func= f'\n{space}@allure.story("{self.case_str_dict["story"]}")' \
                   f'\n{space}@allure.title("{self.case_str_dict["title"]}")' \
                   f'\n{space}def {case_name}(self, ruoyi,request_method="{self.case_str_dict["request_name"]}", file_name="{self.file_name}", case_name="{case_name}"):' \
                   f'\n{space}{space}Check(request_method, file_name,case_name,ruoyi_headers=ruoyi).request_check()\n'

        return case_func

    def case_tail(self):
        """ pytest尾部 main 函数
        if __name__ == '__main__':
            pytest.main(['-s','test_base.py'])
        """
        space = "    "  # 4个空格
        case_func= f"\nif __name__ == '__main__':" \
                   f"\n{space}pytest.main(['-s','{self.file_name}.py'])"
        return case_func

    def write(self):
        """ 可以同时写入 yaml文件 和 pytest 文件
        需要把 session_txt 命名为 test_开头 这样我们的yaml文件 和 pytest 文件就不用取名字了,
        """
        case_name = TESTCASEDIR /"test_base"/ f"{self.file_name}.py"
        print(case_name)
        case_number = HandleSession(self.file_name,handle_method="read_session_num").base_handle()
        if self.write_method =="write":
            HandleSession(self.file_name,write_method="write").base_handle()
            with open(case_name,'a',encoding="utf-8")as case:
                case.write(self.case_import()) # 写入引入文件
                for i in range(case_number):
                    case.write(self.case_self(i+1)) # 写入case 文件
                case.write(self.case_tail())


        else:
            # 覆盖写入
            HandleSession(self.file_name, write_method="rewrite").base_handle()
            with open(case_name, 'w', encoding="utf-8")as case:
                case.write(self.case_import())  # 写入引入文件
                for i in range(case_number):
                    case.write(self.case_self(i+1))  # 写入case 文件
                case.write(self.case_tail())
# 例子
"""
case_dict ={"classname":"use","request_name":"requests","feature":"测试用例生成演示","story":"用户管理模块","title":"RE"}
WriteCase(file_name='test_users',case_str_dict=case_dict,write_method="write").write()
"""

