""" 项目路径 """
from pathlib import Path
ROOTDIR = Path(__file__).parents[2]

floor = {"core":"core","mock_data":"mock",
         "use_process":"process","test_report":"report","test_data":"tedata",
         "test_case":"test_case","usr_tool":"tool","use_config":"config"} # 层级字典

""" 目录 """
CORE = ROOTDIR / floor["core"]  # core 层

MOCKDIR = CORE / floor["mock_data"]  # mock 层 处理mock数据

PROCESSDIR = CORE / floor["use_process"] # process层 封装 线程,进程,协程

TOOLDIR  = CORE / floor["usr_tool"] # tool层 存放一些工具方法,如装饰器,json多层key解析

REPORTDIR = ROOTDIR / floor["test_report"] # report 层 存放测试报告

TESTDATADIR = ROOTDIR / floor["test_data"] # tedata 层 存放用于测试得配置文件

TESTCASEDIR = ROOTDIR / floor["test_case"]# check 层 存放测试用例

TESTCONFIG = TESTDATADIR / floor["use_config"] # 项目的config 文件

""" 存储文件层 """
SESSIONTXTDIR =  TESTDATADIR / "session_text" # fiddler会话存储目录

YAMLDIR = TESTDATADIR / "teyaml" # yaml格式用例数据存储目录

REPORTHTML = REPORTDIR / "html" # 测试报告html存储路径

REPORTHJSON = REPORTDIR /"htmljson"# 测试用例 json 文件 存储路径
