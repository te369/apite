"""通过第三方库 faker 来生成测试数据"""
import random
from faker import Factory

class FakerData:
    def __init__(self):
        '''声明所在区域,引用本地化定制数据'''
        self.fake = Factory().create('zh_CN')

    def cn_name(self):
        '''姓名'''
        return self.fake.name()

    def cn_sex(self):
        '''性别'''
        sex_list = [30007, 22899]
        sex = random.choice(sex_list)
        return chr(sex)

    def cn_phone(self):
        '''手机号码'''
        return self.fake.phone_number()

    def cn_email(self):
        '''邮箱'''
        return self.fake.email()

    def cn_identity(self):
        '''身份证号码'''
        return self.fake.ssn()

    def cn_address(self):
        '''地址'''
        return self.fake.address()

    def cn_card(self):
        '''信用卡号'''
        return self.fake.credit_card_number()

    def user_short(self):
        '''个人信息简介'''
        return self.fake.profile(fields=None, sex=None)

