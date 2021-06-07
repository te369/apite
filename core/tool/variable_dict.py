""" tool 层的 str变量 存储"""
from .module_path import SESSIONTXTDIR

""" 存储  分割 fiddler txt 信息"""
FIDDLERPATH = SESSIONTXTDIR  # fiddler 会话的存储路径

SESSIONMARK = "------------------------------------------------------------------" # 每个session会话的分隔符

HEAD ="""HTTP/1.1
Host: noway.ren
""" # 判断请求方式 截取URL

HOST = " http://noway.ren/" # Host

SESSIONNUMBER = "Host: noway.ren" # 统计会话数

METHOD = {"get":"GET ","post":"POST ","put":"PUT ","delete":"DELETE "} # 请求方法

BODYHEAD ="Cookie: "
BODYTAIL = "HTTP/1.1 200"

RAWHEAD = "Expires: 0"
RESULTHEAD = "Content-Length: "

BASEURL= "http://noway.ren/prod-api/" # 请求的url头

HEADERS = {
    'Authorization': 'Bearer eyJhbGciOiJIUzUxMiJ9.eyJsb2dpbl91c2VyX2tleSI6IjJjNjdlMGFkLTMwNDUtNDcyNS1iNjE5LWIwNmUwMGM1ZjU5YiJ9.4kLXKPcmxsiatS4w1e_dEWynI7Ymcwoh6Ax74vIP32V9noMjyQQNUX9xwOI_pJiNapSI2LibBpotu1ktcHvyww',
    'Content-Type': 'application/json'
} # 请求头

MARK ={"session_dir":FIDDLERPATH,"session_mark":SESSIONMARK,"head":HEAD,
       "host":HOST,"session_num":SESSIONNUMBER,"body_head":BODYHEAD,
       "body_tail":BODYTAIL,"raw_head":RAWHEAD,"result_head":RESULTHEAD,
       "base_url":BASEURL,"headers":HEADERS} # 标记字典


