""" yaml 文件的读写入操作"""
import ruamel.yaml as yaml
from ruamel.yaml import YAML

from .module_path import YAMLDIR

class HandleYaml:
    """ yaml文件的 读写操作 """
    def __init__(self,handle_method=None,file_name=None,write_data=None):
        """
        :param handle_method: 操作方法：读取,写入
        :param file_name: 文件名称
        :param write_data: 待写入数据
        """
        self.handle_method = handle_method
        self.file_name = file_name
        self.write_data = write_data
        self.yaml = YAML()

    def base_handle(self):
        """ 读写 yaml 文件的方法"""
        # file_name = self.file_name+'.yml'
        file_name = YAMLDIR /f"{self.file_name}.yml"

        if self.handle_method == "read":
            with open(file_name,'r',encoding="utf-8") as file:
                yaml_content = self.yaml.load(file)
                return yaml_content

        if self.handle_method == "read_case":
            with open(file_name,'r',encoding="utf-8") as file:
                yaml_content =  yaml.load(file.read(), Loader=yaml.Loader)
                return yaml_content

        elif self.handle_method == "write":
            """ 追加写入 dump设置：缩进为4格,不加载默认流样式,允许Unicode """
            with open(file_name, 'a', encoding="utf-8") as file:
                self.yaml.indent(mapping=4, sequence=4, offset=2)
                self.yaml.dump(self.write_data,file)

        elif self.handle_method == "rewrite":
            """ 覆盖写入 dump设置：缩进为4格,不加载默认流样式,允许Unicode """
            with open(file_name, 'w', encoding="utf-8") as file:
                self.yaml.indent(mapping=4, sequence=4, offset=2)
                self.yaml.dump(self.write_data,file)

#例子
"""
if __name__ == '__main__':
    data= {"deptId": 105, "userName": "test_use", "nickName": "te100", "password": "123456", "phonenumber": "15300000001",
     "email": "1000@qq.com", "sex": "0", "status": "0", "remark": "新增用户", "postIds":[4], "roleIds":[2]}
    now_raw ={"msg":200,"code":300}
    data = {"test_01": {"postdata": data,'asbresult': now_raw}}
    # 写入
    # HandleYaml("write",'test_a',write_data=data).base_handle()
    # 读取
    h = HandleYaml('read', 'test_base').base_handle()
    print(h)
"""
