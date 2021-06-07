"""本地 mock定制 早期版本,没有重写"""
import random
from .information import province_id, phone_number, bank_cardid, first_name, te_text


class TeMock:
    def te_name(self):
        '''
		随机生成姓名,先读取 te_information.py文件中的 first_name 中的姓,
		之后随机选择 第一个文字和第二个文字,再拼接姓+名称,输入 ABB,AB,ABC 格式名字
		'''
        _first_name = random.choice(first_name)
        _last_name1 = random.choice(te_text)
        _last_name2 = random.choice(te_text)
        ran_num = random.randint(0, 2)
        if ran_num == 0:
            ranx = ''
            for i in range(2):
                ranx += _last_name1
        
        elif random == 1:
            ranx = _last_name1 + _last_name2
        
        else:
            ranx = _last_name1
        
        mock_name = _first_name + ranx
        return mock_name
    
    def te_phone(self):
        '''手机号'''
        _first_number = random.choice(phone_number)
        mock_number = str(_first_number) + ''.join(random.choice('0123456789') for i in range(8))
        return mock_number
    
    def te_idcard(self):
        """身份证号码：1-6位代表省份城市区县,7-14位出生年月日,15-16位代表当地派出所代码,
		17位代表性别,奇数代表男性,偶数代表女性,18位为检验码随机生成0-9,有时用x表示"""
        # 前六位
        _first_card = random.choice(province_id)
        four_number = ''
        for i in range(4):
            ran_num = str(random.randint(0, 9))
            four_number += ran_num
        _six = str(_first_card) + four_number
        
        '''7-14位'''
        birthday = self.idcard_birthday()
        
        '''15-16位'''
        two_number = ''
        for i in range(2):
            two_number += str(random.randint(0, 9))
        _sixteen = _six + birthday + two_number
        
        '''17位'''
        sex = random.randint(1, 2)
        if sex == 1:
            seventeen_num = random.randrange(1, 9, 2)
        else:
            seventeen_num = random.randrange(2, 9, 2)
        '''18位'''
        eighteen_num = str(random.randint(1, 10))
        if eighteen_num == '10':
            eighteen_num = 'X'
        id_card = _sixteen + str(seventeen_num) + eighteen_num
        return id_card
    
    def te_bankcard(self):
        """银行卡信息
		一般为16位到19位,bin码 6位 ,中位数9或12位 ,检验码 1位"""
        _bin = random.choice(bank_cardid)
        digits = random.randint(1, 2)
        if digits == 1:
            card_number = str(_bin) + ''.join(random.choice('0123456789') for i in range(9))
        else:
            card_number = str(_bin) + ''.join(random.choice('0123456789') for i in range(12))
        '''校验码规则:从右边第1个数字开始，每隔一位乘以2,得到sum1,将剩下的数相加得到sum2, sum=sum1+sum2
		   sum对10取模后得到m,若n为0，则校验码为0，其余则为对应的10-n，即n对10得补数'''
        sum = 0
        for i in card_number[-1::-2]:
            for m in i * 2:
                sum = sum + int(m)
        for j in card_number[-2::-2]:
            sum = sum + int(j)
        
        if sum % 10 == 0:
            back_code = '0'
        else:
            back_code = str(10 - sum % 10)
        bankcard = card_number + back_code
        return bankcard
    
    def idcard_birthday(self):
        '''生成出生信息,对应身份证的7-14位'''
        year = random.randint(1950, 2020)
        month = random.randint(1, 12)
        day = random.randint(1, 28)
        _month = '0'
        _day = '0'
        date = ''
        if month < 10 and day < 10:
            _month += str(month)
            _day += str(day)
            date += str(year) + _month + _day
        elif month < 10 and day >= 10:
            _month += str(month)
            date += str(year) + _month + str(day)
        elif month >= 10 and day < 10:
            _day += str(day)
            date += str(year) + str(month) + _day
        elif month >= 10 and day >= 10:
            date += str(year) + str(month) + str(day)
        return date
