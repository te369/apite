from module_path import TESTCONFIG
import configparser
class HandleIni:
    '''配置解析器'''
    def __init__(self,file_name=None,node=None,options_key=None):
        """
        :param file_name: .ini 文件名称
        :param node: 节点名称
        :param options_key: 选项键
        :param config:  ConfigParser()
        """
        self.file_name = file_name
        self.config = configparser.ConfigParser()
        self.node = node
        self.options_key = options_key

        if file_name == None:
            """ 当 配置文件 等于空时 加载默认配置 """
            default_file = f"{str(TESTCONFIG / 'base.ini')}"
            self.config.read(default_file, encoding="utf-8-sig")

        else:
            """ 当配置文件不为空时 传入file_name 读取配置信息"""
            config_file = f"{str(TESTCONFIG / self.file_name )}.ini"
            self.config.read(config_file, encoding="utf-8-sig")

    def get_node_content(self):
        """ 获取节点信息 即 选项信息"""
        sections = self.config.sections() # 获取所有节点
        config_node = [i for i in sections] # 返回一个节点列表  dict.fromkeys
        options_dict = [self.config.options(i) for i in sections] # 返回选项键列表
        return dict(zip(config_node,options_dict)) # 返回字典{"node":"options[list格式]"}


    def get_options_value(self):
        """ 获取选项值 """
        if self.node:
            options_value =  self.config.get(self.node,self.options_key) # 获取选项值
            return {"node":self.node,"options_key":self.options_key,"options_value":options_value} # 返回字典

        else:
            node = "ruoyi"
            options_value = self.config.get(node,self.options_key)
            return {"node":node,"options_key":self.options_key,"options_value":options_value}

# 例子
"""
if __name__ == '__main__':
    # hx = HandleIni(file_name="base",node="mysql",options_key='host').get_options_value()
    h = HandleIni(node="te_user",options_key="username").get_options_value()
    print(h["options_key"])
"""
