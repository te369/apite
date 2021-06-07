"""存储测试数据的通用信息,百家姓,身份证号,手机号开头,银行卡"""

'''身份证号码开头省份标识'''
province_id = [11, 12, 13, 14, 15, 21, 22, 23, 31, 32, 33, 34, 35, 36, 37, 41, 42, 43, 44, 45, 46,
               50, 51, 52, 53, 54, 61, 62, 63, 65, 65, 81, 82, 83]

'''手机号码标识'''
phone_number = [139, 138, 137, 136, 135, 134, 159, 158, 15, 150, 151, 152, 188,
                130, 131, 132, 156, 155, 133, 153, 189]
'''银行卡号
    "工商银行": "623062", "中国银行": "621343","建设银行": "622676","招商银行": "410062",
    "中信银行": "433680","光大银行": "622663","民生银行": "622622","交通银行": "621335",
    "平安银行": "622989","农业银行": "622848"
'''
bank_cardid= [623062,621343,622676,410062,433680,622663,622622,621335,622989,622848]

'''百家姓'''
first_name = ['赵', '钱', '孙', '李', '周', '吴', '郑', '王', '冯', '陈', '褚', '卫', '蒋',
              '沈', '韩', '杨', '朱', '秦', '尤', '许', '何', '吕', '施', '张', '孔', '曹',
              '严', '华', '金', '魏', '陶', '姜', '戚', '谢', '邹', '喻', '柏', '水', '窦', '章', '云', '苏',
	          '潘', '葛', '奚', '范', '彭', '郎', '鲁', '韦', '昌', '马', '苗', '凤', '花', '方', '俞', '任', '袁', '柳',
	          '酆', '鲍', '史', '唐', '费', '廉', '岑', '薛', '雷', '贺', '倪', '汤', '滕', '殷', '罗', '毕', '郝', '邬',
	          '安', '常', '乐', '于', '时', '傅', '皮', '卞', '齐', '康', '伍', '余', '元', '卜', '顾', '孟', '平', '黄',
	          '和', '穆', '萧', '尹', '姚', '邵', '湛', '汪', '祁', '毛', '禹', '狄', '米', '贝', '明', '臧', '计', '伏',
	          '成', '戴', '谈', '宋', '茅', '庞', '熊', '纪', '舒', '屈', '项', '祝', '董', '粱', '杜', '阮', '蓝', '闵',
	          '席', '季', '麻', '强', '贾', '路', '娄', '危', '江', '童', '颜', '郭', '梅', '盛', '林', '刁', '钟', '徐',
	          '邱', '骆', '高', '夏', '蔡', '田', '樊', '胡', '凌', '霍', '虞', '万', '支', '柯', '昝', '管', '卢', '莫',
	          '经', '房', '裘', '缪', '干', '解', '应', '宗', '丁', '宣', '贲', '邓', '郁', '单', '杭', '洪', '包', '诸',
	          '左', '石', '崔', '吉', '钮', '龚', '程', '嵇', '邢', '滑', '裴', '陆', '荣', '翁', '荀', '羊', '於', '惠',
	          '甄', '麴', '家', '封', '芮', '羿', '储', '靳', '汲', '邴', '糜', '松', '井', '段', '富', '巫', '乌', '焦',
	          '巴', '弓', '牧', '隗', '山', '谷', '车', '侯', '宓', '蓬', '全', '郗', '班', '仰', '秋', '仲', '伊', '宫',
	          '宁', '仇', '栾', '暴', '甘', '钭', '厉', '戎', '祖', '武', '符', '刘', '景', '詹', '束', '龙', '叶', '幸',
	          '司', '韶', '郜', '黎', '蓟', '薄', '印', '宿', '白', '怀', '蒲', '邰', '从', '鄂', '索', '咸', '籍', '赖',
	          '卓', '蔺', '屠', '蒙', '池', '乔', '阴', '欎', '胥', '能', '苍', '双', '闻', '莘', '党', '翟', '谭', '贡',
	          '劳', '逄', '姬', '申', '扶', '堵', '冉', '宰', '郦', '雍', '舄', '璩', '桑', '桂', '濮', '牛', '寿', '通',
	          '边', '扈', '燕', '冀', '郏', '浦', '尚', '农', '温', '别', '庄', '晏', '柴', '瞿', '阎', '充', '慕', '连',
	          '茹', '习', '宦', '艾', '鱼', '容', '向', '古', '易', '慎', '戈', '廖', '庾', '终', '暨', '居', '衡', '步',
	          '都', '耿', '满', '弘', '匡', '国', '文', '寇', '广', '禄', '阙', '东', '殴', '殳', '沃', '利', '蔚', '越',
	          '夔', '隆', '师', '巩', '厍', '聂', '晁', '勾', '敖', '融', '冷', '訾', '辛', '阚', '那', '简', '饶', '空',
	          '曾', '毋', '沙', '乜', '养', '鞠', '须', '丰', '巢', '关', '蒯', '相', '查', '後', '荆', '红', '游', '竺',
	          '权', '逯', '盖', '益', '桓', '公', '万俟', '司马', '上官', '欧阳', '夏侯', '诸葛', '闻人', '东方', '赫连',
	          '皇甫', '尉迟', '公羊', '澹台', '公冶', '宗政', '濮阳', '淳于', '单于', '太叔', '申屠', '公孙', '仲孙',
	          '轩辕', '令狐', '钟离', '宇文', '长孙', '慕容', '鲜于', '闾丘', '司徒', '司空', '亓官', '司寇', '仉', '督',
	          '子车', '颛孙', '端木', '巫马', '公西', '漆雕', '乐正', '壤驷', '公良', '拓跋', '夹谷', '宰父', '谷梁', '晋',
	          '楚', '闫', '法', '汝', '鄢', '涂', '钦', '段干', '百里', '东郭', '南门', '呼延', '归', '海', '羊舌', '微生',
	          '岳', '帅', '缑', '亢', '况', '后', '有', '琴', '梁丘', '左丘', '东门', '西门', '商', '牟', '佘', '佴', '伯',
	          '赏', '南宫', '墨', '哈', '谯', '笪', '年', '爱', '阳', '佟', '言', '福']

'''文字库'''
te_text = ['删', '泛', '煎', '瞪', '彻', '排', '矣', '虾', '菩', '伪', '棋', '技',
             '愧', '鸿', '眯', '尺', '跑', '捂', '馆', '猖', '他', '蛙', '藐', '族', '猛', '蒸', '到',
             '叩', '尘', '届', '洋', '躬', '嗽', '床', '综', '轿', '妻', '屉', '荒', '鲸', '炎', '窜', '罕',
             '痛', '脯', '闷', '助', '核', '卿', '维', '感', '塔', '穴', '死', '请', '晰', '胃', '球', '警',
             '捍', '芙', '儒', '盔', '粟', '烘', '绣', '绽', '玷', '泞', '击', '看', '橘', '卉', '虚', '以',
             '其', '龄', '凶', '溢', '啰', '柯', '苔', '隔', '筛', '姿', '榕', '箫', '铅', '陕', '廷', '阮',
             '挟', '烙', '主', '降', '淀', '逸', '虑', '掌', '祸', '涌', '惧', '煮', '瞎', '瀑', '稽', '邬',
             '悦', '靖', '照', '抢', '旷', '纠', '忘', '犁', '澳', '及', '莘', '瓷', '允', '杉', '掺', '啤',
             '晏', '光', '吞', '传', '坑', '熏', '鳄', '运', '京', '材', '送', '心', '匈', '俗', '涝',
             '遗', '饭', '姬', '假', '踪', '雁', '贯', '推', '哑', '琉', '插', '扣', '卯', '熄', '西', '植',
             '条', '曲', '驯', '抛', '骨', '咬', '唤', '射', '骄', '梯', '批', '签', '对', '诊', '砸', '立',
             '呕', '娱', '电', '换', '外', '珍', '修', '俯', '祭', '绰', '怎', '劣', '油', '馒', '惑', '赐',
             '桔', '榨', '邴', '扯', '盒', '仆', '牺', '夜', '宴', '触', '圃', '嗦', '肪', '斟',
             '脉', '峻', '佩', '叨', '迈', '境', '拦', '毅', '臧', '窦', '砖', '穗', '社', '豚', '柑',
             '囊', '桶', '奏', '爬', '辆', '拐', '营', '玻', '嘛', '耻', '拴', '日', '肤', '是',
             '滩', '货', '踩', '丙', '奉', '焊', '摔', '悔', '尿', '瞬', '愤', '驶', '栏', '捉', '琐',
             '膜', '长', '军', '倡', '岖', '之', '睫', '揪', '壮', '毯', '鸟', '颠', '嗜', '沐', '侨',
             '禅', '该', '怡', '示', '衰', '颤', '隅', '诡',
             '匿', '锁', '裸', '肆', '识', '崛', '壬', '什', '沉', '痒', '术', '褂', '欧',
             '訾', '膨', '校', '茂', '悄', '伙', '赔', '座', '使', '崇', '得', '瞩',
             '横', '赃', '牟', '检', '婴', '玖', '麴', '陌', '褒', '露', '书', '迎', '践',
             '狱', '潜', '厦', '勃', '鸦', '放', '袭', '份', '缎', '除', '限', '傻', '殿',
             '鼻', '蒂', '摧', '淋', '亿', '罢', '烦', '狐', '愚', '耍', '窍', '惋',
             '狮', '碳', '尾', '百', '并', '陵', '葱', '据', '秃', '像', '笔', '锈',
             '称', '活', '数', '拂', '阚', '虫', '蜗', '炮', '渝', '崭', '详', '俞', '垛',
             '捣', '志', '趟', '释', '伤', '录', '庶', '墩', '扎', '鸳', '疲', '升', '擒',
             '仗', '耳', '纵', '跨', '啪', '艇', '绊', '摹', '跟', '糕', '氛', '姑', '煌',
             '毡', '兽', '斗', '旅', '啊', '爷', '椰', '视', '吹', '饮', '氓', '迄', '泳',
             '由', '狡', '赠', '巧', '县', '杂', '拉', '溉', '姆', '迫', '骑', '序', '怕', '狠',
             '毫', '遮', '嘴', '焰', '魔', '汰', '翠', '恳', '胶', '着', '癌', '匾', '填', '铜',
             '匙', '绿', '短', '憎', '我', '嚷', '永', '茧', '浏', '劈', '凑', '胆', '狞', '敖',
             '辣', '堡', '谬', '磷', '弹', '沧', '枉', '唧', '久', '阶', '肯', '涕', '蜀', '蟋',
             '颅', '匀', '屑', '蔼', '毒', '鸥', '栈', '咋', '殊', '汉', '珊', '扩', '妹', '黯',
             '嵌', '打', '逛', '吼', '壶', '战', '芦', '诫', '哮', '缕', '泽', '郦', '疫', '幼',
             '钥', '确', '新', '雀', '递', '踱', '渡', '宏', '唾', '娃', '岸', '账', '晓', '笼',
             '绝', '谐', '结', '故', '琳', '膝', '品', '褥', '与', '兜', '诽', '议', '焉', '惩',
             '团', '软', '洛', '力', '继', '您', '芜', '徘', '棚', '缴', '渤', '肢', '者', '厘',
             '众', '鹰', '坪', '涣', '联', '自', '祀', '窘', '界', '减', '灸', '黔',
             '眷', '木', '袋', '忆', '岗', '抄', '促', '耗', '奢', '价', '铝', '碘', '两', '背', '形',
             '淌', '苹', '溃', '裴', '浅', '住', '扔', '润', '乡', '颊', '曼', '敞', '丹', '瞒', '却',
             '敏', '部', '呼', '憨', '屎', '兢', '搁', '父', '字', '摩', '刹', '曙', '懒',
             '蹈', '学', '邑', '盹', '半', '淆', '滔', '律', '来', '听', '朦', '慰', '锚', '显',
             '尬', '厚', '孽', '壤', '超', '点', '妈', '刃', '馅', '铸', '缆', '挎', '淑', '惟',
             '蔺', '陡', '税', '篓', '叔', '患', '猩', '驴', '乾', '民', '吧', '卞', '鸣', '迭',
             '迂', '蚤', '婿', '稻', '佑', '叹', '老', '簇', '罩', '村', '蕉', '驱', '处', '恬',
             '孕', '挤', '七', '多', '剃', '讨', '青', '塑', '励', '诞', '冤', '捺', '咒', '梳',
             '砚', '坦', '诚', '置', '渺', '饺', '色', '怜', '鞍', '枫', '为', '丢', '狰', '债',
             '滴', '级', '箭', '赞', '鬓', '肾', '赌', '坯', '耸', '潮', '套',
             '覆', '灌', '仅', '弦', '嘲', '戌', '岛', '兼', '靶', '资', '矛', '螃', '萌',
             '稀', '谚', '健', '丝', '则', '共', '渔', '踊', '性', '膏', '炊', '种', '开',
             '胀', '献', '咽', '驳', '脾', '亲', '逞', '值', '莺', '滤', '茄', '羿', '娇', '腋',
             '途', '鞋', '邰', '茫', '蜘', '撑', '忿', '可', '泉', '祷', '君', '朋', '操', '蓄',
             '样', '正', '疚', '豺', '群', '寥', '钾', '脆', '潭', '诵', '粥', '矢', '咕', '例',
             '扁', '节', '捎', '刊', '览', '硅', '土', '吗', '谆', '投', '豁', '翼', '巡',
             '跳', '瞻', '狼', '苞', '翟', '拾', '鹏', '聪', '渗', '卵', '办', '戳', '格', '衍',
             '企', '芝', '宅', '疤', '临', '窄', '语', '障', '澄', '甸', '号', '俩', '亮',
             '懦', '洲', '人', '酥', '斧', '斥', '堕', '凯', '贸', '腹', '鲫', '履', '因', '扭',
             '卤', '刷', '遍', '嫂', '虞', '馨', '串', '廊', '屏', '窑', '谦', '崖', '宙',
             '层', '泪', '唇', '暑', '彪', '艳', '改', '羔', '摸', '专', '官', '音', '截', '责',
             '特', '隶', '断', '缸', '幻', '私', '悖', '瘫', '窥', '娥', '疼', '鲜', '呢',
             '桩', '尊', '吓', '簿', '统', '劲', '羹', '薯', '磁', '竹', '抽', '瑞', '怒', '趾',
             '帐', '椅', '霄', '坏', '愣', '绷', '侣', '侈', '荀', '判', '便', '旱', '散', '咳',
             '枚', '浴', '讶', '惹', '腐', '粮', '脱', '镑', '豫', '腿', '茹', '指', '矩',
             '袜', '咐', '庙', '峨', '子', '葫', '发', '里', '大', '获', '茉', '括', '庭', '逗',
             '会', '舞', '挂', '龚', '褚', '寨', '猾', '乱', '栅', '蜒', '亥', '虎', '逃', '秤',
             '勒', '雇', '遥', '往', '玫', '场', '抡', '进', '恤', '析', '囤', '堆', '箱',
             '躏', '贵', '离', '溺', '效', '型', '留', '踏', '逄', '染', '勤', '掐', '复', '澡', '藻',
             '尧', '寅', '筑', '囚', '怔', '雕', '狸', '酗', '祁', '败', '磨', '佳', '买', '叛', '痰',
             '收', '手', '兆', '趣', '尴', '糯', '骂', '夯', '建', '哆', '破', '贰', '剂', '萍', '域',
             '糖', '画', '茎', '偶', '醇', '敢', '哪', '疟', '庐', '溪', '擦', '五', '食', '俱', '热',
             '莉', '玲', '谋', '仁', '襟', '措', '圈', '炭', '科', '拿', '陋', '盲', '瞅', '撵',
             '零', '墅', '扫', '痹', '橱', '休', '冶', '肿', '测', '瑙', '赢', '蔬', '诺', '酪',
             '巾', '抖',
             '招', '加', '苦', '钢', '肚', '产', '紧', '护', '道', '雹', '琅', '涛', '消', '野',
             '乒', '吊', '止', '河', '蝴', '仓', '驮', '蹋', '锣', '巳', '霉', '疮', '杰', '隋', '臭',
             '必', '预', '追', '遂', '逊', '钭', '劝', '甩', '俄', '熙', '面', '概', '吠', '蝗', '启',
             '匡', '浆', '辜', '柄', '桐', '拷', '总', '啥', '供', '辟', '缠', '赤', '盟', '芳', '征',
             '柒', '近', '迪', '柱', '翘', '蕾', '荷', '泌', '莹', '惊', '端', '极', '额', '取', '讯',
             '刺', '茶', '恋', '斜', '缰', '聘', '慧', '缘', '柜', '飘', '济', '迁', '辫', '湘', '择', '徒',
             '禽', '裤', '瘾', '昂', '剔', '睁', '爪', '骤', '姨', '纯', '巨', '舆', '恍', '狄', '急', '瞿',
             '绚', '谜', '豆', '疯', '良', '涯', '斩', '围', '矮', '慌', '菜', '愈', '犹', '坟', '妇', '夸',
             '赁', '蝎', '府', '羞', '佟', '鹅', '世', '窖', '召', '殳', '善', '讼', '册', '违', '每', '姊',
             '衙', '冈', '寒', '喝', '望', '秩', '己', '凉', '匕', '螺', '豪', '等', '脐', '昔', '缑', '遣',
             '赋', '稚', '弛', '昼', '忌', '名', '觉', '恕', '引', '璃', '八', '认', '出', '妮', '逝', '闪',
             '戊', '肖', '偏', '袍', '威', '赫', '烁', '奠', '定', '崩', '阔', '碗', '荐', '灾', '倘', '系',
             '庾', '个', '佐', '绘', '睐', '怨', '奖', '症', '搬', '奴', '期', '甚', '圾', '兴', '役', '纺',
             '诗', '克', '惫', '墟', '筋', '叭', '饿', '舶', '毋', '揍', '存', '盗', '槛', '曰', '约', '胰',
             '察', '凛', '表', '好', '筐', '沼', '根', '尖', '酸', '臊', '寡', '掏', '撕', '滚', '春', '清',
             '拙', '慈', '锦', '赚', '玄', '吱', '笨', '唆', '嫉', '圆', '顿', '积', '骚', '寝', '谁', '衔',
             '掘', '比', '蛤', '捅', '低', '牢', '训', '靡', '绑', '棍', '载', '很', '蚀', '本', '均', '炒',
             '首', '款', '蜻', '舵', '火', '抠', '穿', '旋', '剧', '母', '烫', '幕', '裁', '鲤', '绪', '榆',
             '爆', '烤', '酉', '站', '傍', '馋', '袖', '涡', '佛', '痢', '度', '浩', '巷', '槽', '狈', '妃',
             '亭', '挫', '褪', '怖', '耙', '隐', '兰', '票', '厕', '誊', '彰', '媳', '亏', '蜕', '版', '腮',
             '宾', '若', '右', '拔', '俺', '猿', '呻', '闺', '卒', '厅', '汞', '垢', '独', '侮', '寻', '命',
             '逮', '闲', '客', '讲', '麦', '驹', '扼', '德', '二', '棒', '领', '羚', '钧', '且', '差', '妒',
             '夹', '星', '锯', '没', '创', '贴',
             '跋', '馈', '绅', '固', '侵', '爹', '讳', '天', '装', '揉', '糠', '橙', '竟', '蹭', '了',
             '吐', '堰', '胳', '驻', '现', '祈', '担', '刮', '龟', '洁', '分', '烹', '针', '惶', '纤',
             '决', '朽', '胧', '冻', '逼', '慨', '裳', '洗', '泰', '菲', '拥', '坷', '窝', '医', '恭',
             '架', '皂', '扳', '梢', '酝', '帕', '吏', '裘', '城', '埃', '鼓', '抱', '犀', '哇', '物',
             '湾', '躯', '纬', '倒', '韶', '说', '朗', '否', '坊', '鹦', '雍', '肌', '参', '歇', '帮',
             '抓', '脂', '镀', '宇', '午', '禁', '乘', '磕', '夕', '蛾', '蹦', '韵', '喳', '凝', '执',
             '快', '瘸', '镐', '市', '或', '博', '规', '亩', '凳', '霎', '九', '喊', '窒', '赛',
             '嘿', '抚', '草', '茸', '贪', '又', '展', '州', '豹', '蛀', '葵', '榴', '残', '吸', '颈',
             '四', '冒', '在', '难', '偿', '弗', '缅', '挨', '舱', '损', '鹃', '兑', '浑', '窃', '扇',
             '织', '配', '盐', '敦', '栗', '棘', '免', '箩', '脖', '贬', '此', '辗', '凿', '夔',
             '瘤', '凸', '肛', '狭', '被', '氮', '愁', '补', '伞', '生', '受', '布', '式', '帖',
             '晁', '勿', '芋', '吭', '纹', '於', '险', '停', '臣', '询', '陷', '柔', '溜', '宪', '斋', '溶',
             '蟀', '颇', '赴', '沿', '惰', '旬', '彩', '婆', '郊', '傲', '馍', '竞', '弯', '啦', '筝', '躺',
             '韦', '尸', '川', '靠', '嚎', '题', '燥', '紫', '拣', '掉', '寄', '雌', '鸭', '鲨', '趁',
             '押', '暮', '郜', '秽', '乍', '肃', '碟', '攻', '浮', '末', '棕', '赣', '憾', '模', '设', '氯',
             '盯', '钻', '桌', '享', '刨', '邦', '绍', '爽', '漫', '濒', '奸', '琢', '息', '桥', '渠', '颓',
             '岔', '职', '舅', '典', '猬', '需', '避', '绒', '嘀', '碾', '剿', '缪', '灯', '妆', '瓜', '谯',
             '伦', '想', '哄', '捆', '随', '蒜', '奋', '握', '倾', '仙', '肴', '饱', '底', '南', '罪', '幢',
             '绳', '泼', '饼', '葡', '闸', '响', '果', '虹', '晒', '愉', '援', '源', '胞', '胖', '教', '奇',
             '订', '莲', '掀', '瞭', '菠', '恨', '只', '如', '移', '屹', '铃', '登', '杠', '隧', '洽',
             '牙', '求', '垫', '的', '动', '斑', '垃', '遇', '念', '呜', '脏', '状', '波', '萝', '寞', '彼',
             '芥', '集', '淮', '迢', '妄', '钙', '勉', '素', '芒', '轰', '租', '拍', '勋', '谍', '观', '歪',
             '娘', '藏', '持', '风', '档', '睦', '精', '阐', '坠', '憔', '杀', '雅', '庵',
             '抵', '臀', '坝', '购', '侍', '胎', '逯', '脸', '莱', '寓', '秧', '瑰', '泻', '伸', '懊', '仿',
             '作', '跷', '肝', '菊', '兔', '锻', '沽', '牲', '练', '功', '蚪', '秆', '找', '演', '俐',
             '累', '负', '辽', '绸', '翻', '远', '变', '吵', '箕', '香', '叁', '悬', '率', '希', '锹', '繁',
             '壹', '御', '振', '环', '孤', '舟', '帜', '眉', '壁', '汲', '漏', '碰', '乜', '势', '萤', '杏',
             '帘', '晨', '第', '秸', '厍', '而', '镶', '镰', '眠', '悲', '腰', '饵', '恰', '添', '皿',
             '摊', '炕', '僧', '沪', '盆', '骇', '谴', '研', '匪', '径', '佴', '剪',
             '缭', '缓', '秘', '粤', '譬', '妨', '揣', '钩', '内', '眨', '喧', '厨', '鹿', '走', '浇',
             '汽', '惜', '无', '斤', '静', '臼', '咄', '附', '裹', '锄', '涮', '吻', '思', '忍', '岩', '谎',
             '嘱', '知', '控', '目', '炬', '组', '澈', '篷', '啃', '厂', '糙', '檀', '证', '雨', '耘', '昏',
             '妙', '泵', '肥', '厌', '某', '勘', '禀', '嘹', '旭', '锡', '码', '隗', '唱', '栾', '朵', '仔',
             '掩', '荤', '帷', '硬', '饰', '六', '粒', '滋', '少', '菱', '冬', '菇', '棱', '异', '延', '胚',
             '循', '诀', '旺', '券', '瑟', '浊', '耽', '顷', '膛', '省', '蓉', '歉', '再', '坛', '粪', '篡',
             '宝', '煞', '斯', '话', '料', '淘', '餐', '稳', '刀', '袄', '慷', '缉', '掂', '拧', '柠', '楼',
             '霞', '前', '檐', '惨', '酱', '吃', '桓', '膀', '么', '罐', '姐', '濮', '澜', '财', '淫', '洞',
             '噪', '牌', '夺', '碌', '岁', '娶', '院', '优', '峰', '乎', '畅', '虏', '宜', '摇', '浓', '笑',
             '挽', '哦', '杯', '所', '顶', '褐', '挖', '竺', '潇', '服', '哩', '苛', '尝', '桨', '咖',
             '爵', '梭', '努', '衫', '募', '沛', '皇', '钳', '早', '齿', '哗', '祟', '转', '缤', '救',
             '坚', '癸', '业', '谅', '液', '蛛', '神', '籽', '当', '杖', '奚', '吟', '枪', '哀', '摆', '蚁',
             '溅', '抒', '敲', '虽', '佃', '候', '谱', '靳', '刚', '挠', '频', '股', '失', '泥', '熔', '谤',
             '屁', '甫', '腥', '後', '返', '辈', '胜', '寺', '疑', '拨', '捏', '次', '堤', '裙', '械', '输',
             '闫', '兄', '抑', '蚕', '掷', '腻', '宵', '伴', '幅', '拄', '篇', '拜', '义', '美', '鹉',
             '员', '皓', '下', '枢', '脑', '霜', '既', '工', '聆', '鄢', '邹', '让', '晦', '巍', '庆', '讥',
             '冠', '真', '冥', '笛', '嫩', '蔓', '毙', '酌', '肇', '屋', '疆', '嚣', '梨', '骏', '晶', '鉴',
             '轩', '侄', '靴', '肩', '废', '缚', '篱', '扒', '坡', '眶', '旗', '蝙', '朴', '挡', '举', '腊',
             '信', '拳', '痊', '调', '婚', '婉', '阻', '选', '梗', '啄', '扛', '哼', '叽', '队', '把', '涉',
             '害', '片', '塌', '雳', '桃', '伺', '辉', '微', '算', '绕', '涧', '丸', '店', '漠', '瞳',
             '列', '渴', '拟', '仑', '琼', '棠', '副', '搅', '撼', '乓', '晾', '铐', '影', '锰', '熬', '诬',
             '跺', '磅', '岂', '撩', '笙', '情', '各', '吁', '垄', '喷', '橄', '板', '邱', '赶', '璩', '膊',
             '搞', '汹', '才', '碑', '阿', '歧', '茵', '碧', '峭', '犯', '蛋', '框', '契', '凡', '敌', '稍',
             '簧', '肘', '沦', '钝', '赂', '涨', '拘', '噩', '郝', '淤', '遏', '屡', '椒', '逆', '礼', '行',
             '已', '伐', '劫',
             '怯', '做', '鼠', '蔗', '瘩', '区', '阅', '纳', '驾', '筏', '轧', '忱', '叫', '饲', '沮', '悼',
             '蔽', '机', '逻', '玉', '扬', '盾', '播', '悉', '儿', '妓', '革', '剥', '讹', '骗', '梧', '访',
             '擎', '虐', '间', '割', '蟹', '牡', '艺', '黑', '跃', '樟', '英', '偷', '腔', '砰', '嘉', '实',
             '碎', '缩', '鬼', '局', '借', '敬', '蕊', '孩', '体', '贮', '辱', '廓', '它', '悠', '梆', '跛',
             '檬', '卦', '亚', '梦', '函', '钠', '非', '致', '剖', '街', '达', '辙', '舄', '先', '穷', '湿',
             '枕', '考', '匠', '贫', '沫', '互', '灶', '胥', '氏', '芹', '荫', '祥', '冰', '揽', '竣',
             '过', '韧', '案', '逾', '鞭', '审', '脓', '堂', '挚', '乞', '叮', '挥', '仍', '煽', '起', '飞',
             '糜', '哨', '敷', '泄', '宛', '峡', '捧', '敛', '声', '帽', '谨', '狂', '垒', '姥', '你', '陪',
             '乙', '抬', '迷', '侧', '代', '拒', '絮', '轨', '炫', '携', '回', '绞', '贞', '踢', '羽',
             '吆', '涵', '捷', '课', '园', '替', '肋', '葬', '即', '但', '灵', '殉', '渲', '瞧', '氢', '兵',
             '撬', '捡', '重', '湃', '叼', '将', '瘟', '腺', '汇', '伟', '夷', '凰', '隘', '犬', '震', '寂',
             '默', '岭', '蜓', '嫁', '喜', '炉', '栖', '叠', '懈', '徊', '殃', '辐', '筷', '恒', '呆', '蹲',
             '础', '一', '派', '醋', '叙', '欎', '萨', '庸', '药', '薪', '硕', '漓', '乖', '蒯', '歹',
             '赡', '雾', '竿', '迅', '炼', '句', '拭', '弄', '粹', '碱', '夫', '刻', '弱', '栓', '肮', '蛮',
             '萎', '硫', '忧', '俏', '浪', '斌', '浙', '折', '币', '彤', '畔', '掠', '媒', '错', '角', '激',
             '赘', '给', '衅', '饥', '编', '提', '盏', '三', '闯', '哟', '仪', '协', '脊', '铛', '采',
             '链', '昨', '牵', '祠', '搭', '欠', '奔', '港', '寸', '唉', '蜈', '脚', '帚', '嗡', '匆', '霸',
             '诱', '弃', '妖', '用', '宽', '要', '俊', '纸', '呀', '承', '乂', '峦', '距', '窿', '忙',
             '舰', '闽', '构', '槐', '乃', '畸', '撞', '蜜',
             '邻', '崎', '网', '嗅', '扈', '梁', '宓', '女', '屯', '惭', '筒', '疏', '愕', '辅', '尹',
             '凄', '喇', '榄', '鳞', '砍', '醒', '适', '倍', '姓', '属', '讽', '馁', '喉', '嫌', '至', '番',
             '吮', '拇', '咨', '增', '藉', '纽', '意', '丫', '忠', '昆', '盈', '禾', '贼', '蠕', '尽', '探',
             '沥', '唯', '渐', '掰', '坐', '记', '政', '闹', '誉', '肠', '洼', '太', '吩', '欲', '玛', '郗',
             '质', '弥', '月', '拱', '炸', '厢', '搏', '幌', '樊', '凭', '甜', '睹', '告', '邪', '暖', '竖',
             '吨', '署', '恢', '屿', '艘', '捕', '试', '睡', '撰', '烧', '酣', '珠', '惯', '纫', '铭', '陨',
             '盘', '馏', '偎', '轴', '呛', '烛', '最', '磊', '灭', '矫', '颂', '慢', '瓤', '癣', '株', '翔',
             '煤', '辩', '朝', '银', '笪', '谣', '船', '抗', '邀', '疗', '线', '悯', '搜', '恐',
             '鄙', '贱', '晌', '叉', '谓', '跌', '译', '迟', '驼', '砂', '畏', '北', '象', '述', '占', '帆', '苇',
             '续', '郏', '恩', '滞', '纱', '估', '狗', '蜡', '铁', '蓟', '盼', '湛', '鸡', '昭', '捶', '椭', '沟',
             '萄', '她', '佣', '今', '旧', '芽', '栋', '笋', '缔', '际', '桦', '几', '捞', '漾', '颖', '蹬', '廖',
             '旁', '惦', '鼎', '瓣', '压', '剩', '整', '娟', '孝', '僚', '悍', '监', '垮', '翩', '徽', '凹', '闵',
             '擅', '裂', '守', '邢', '够', '揩', '完', '晴', '去', '匣', '篮', '也', '块', '顺', '丘', '倦',
             '腕', '稠', '拗', '藤', '合', '庇', '阵', '词', '航', '略', '挣', '究', '咪', '枣', '皆', '写', '流',
             '地', '渊', '焚', '擂', '付', '具', '误', '喂', '读', '囱', '暗', '雏', '跤', '切', '基', '侦', '姻',
             '初', '疹', '蟆', '霹', '舀', '痪', '烟', '键', '味', '滨', '央', '辖', '燃', '鳍', '似', '嚼', '遭',
             '授', '瘪', '贷', '注', '突', '旦', '铲', '晃', '淹', '兹', '菌', '导', '墓', '倪', '报', '拖',
             '拓', '委', '烂', '谊', '滕', '逐', '疾', '淡', '雪', '卷', '莽', '就', '茬', '尼', '榜', '划', '呵',
             '圣', '捌', '销', '媚', '碍', '士', '沁', '稼', '眼', '阙', '筹', '糟', '熟', '荔', '辰', '僵',
             '猴', '泣', '塞', '勺', '缝', '毁', '弊', '著', '蚓', '氧', '撤', '粗', '映', '细', '徙', '务', '始',
             '态', '艰', '趋', '誓', '捻', '晕', '僻', '历', '侠', '泡', '耕', '化', '痘', '轮', '依', '络', '窗',
             '纲', '惕', '密', '薇', '暨', '垦', '岑', '仉', '阀', '甲', '彬',
             '奈', '椿', '披', '小', '贿', '准', '尔', '涤', '千', '治', '丑', '啡', '蝇', '库', '诈', '铺', '汁',
             '贻', '待', '挪', '鳖', '窟', '貌', '佘', '硝', '保', '迹', '标', '弧', '搀', '灰', '疙', '图', '予',
             '摘', '亦', '骡', '较', '鸵', '拽', '贲', '津', '绩', '欣', '隙', '令', '芭', '秉', '矿', '糊', '见',
             '柿', '伶', '胸', '邮', '酆', '台', '荧', '匹', '捐', '灼', '芮', '卡', '孵', '懂', '矾', '室', '沾',
             '猜', '蝉', '蚣', '反', '弟', '身', '倚', '暇', '甄', '诉', '婶', '直', '纷', '欺', '妥', '般', '锌',
             '竭', '卑', '漆', '绢', '臂', '酒', '坤', '枝', '速', '昝', '嘶', '轻', '魂', '滇', '哥', '衬', '理',
             '蚯', '闭', '剑', '豌', '刑', '舔', '坎', '翅', '汛', '男', '漂', '痕', '塘', '量', '口', '另', '削',
             '韭', '猎', '带', '户', '十', '绵', '器', '智', '棉', '拼', '中', '腾', '鸽', '渣', '袱', '藕', '杆',
             '验', '悟', '卧', '原', '透', '唁', '撒', '跪', '缀', '锥', '争', '丛', '啼', '售', '悴', '森', '睛',
             '些', '阁', '堪', '宠', '羡', '觅', '不', '怠', '簸', '蚌', '蛇', '墙', '蹄', '湖', '蜂', '鹊', '椎',
             '闰', '肺', '辑', '哉', '搔', '制', '芯', '抹', '诲', '冗', '颁', '枯', '蝶', '旨', '紊', '更', '皱',
             '血', '戒', '钞', '瘦', '荡', '困', '拎', '瞄', '衷', '辨', '罚', '嵇', '勇', '璧', '婪', '头', '贩',
             '鸯', '吾', '滥', '嗓', '逢', '催', '还', '颗', '丧', '秒', '深', '泊', '遵', '咧', '撮', '位', '詹',
             '哲', '浸', '奶', '含', '拢', '愿', '病', '淳', '镜', '培', '鹤', '蠢', '啸', '乏', '论', '绎', '苟',
             '咏', '芬', '幽', '托', '丽', '爸', '蚂', '酿', '溯', '咙', '蝌', '件', '丐', '倔', '描', '奥', '址',
             '猪', '魄', '樱', '丈', '蝠', '曝', '镇', '恃', '髓', '殖', '造', '顽', '呈', '秀', '唠', '舍', '交',
             '畴', '吝', '摄', '评', '恶', '橡', '贤', '焕', '胁', '尉', '楷', '粉', '事', '帝', '埋',
             '洒', '退', '栽', '聋', '搓', '棺', '趴', '页', '榔', '俭', '憋', '咱', '肉', '驰', '蘑', '门',
             '柬', '撇', '嘻', '辞', '耀', '魅', '同', '甥', '备', '扑', '澎', '乳', '魁', '落', '蕴', '垂', '欢',
             '气', '侥', '策', '裕', '聊', '晚', '埠', '汗', '歌', '揭', '俘', '扮', '这', '然', '赦', '砌', '答',
             '酬', '蔑', '躁', '舌', '树', '哭', '酷', '氨', '灿', '痴', '攀', '入', '戏', '恼', '暂', '夭',
             '烈', '接', '友', '棵', '昧', '礁', '卖', '搂', '净', '哎', '瓶', '按', '躲', '污',
             '拆', '问', '雄', '皖', '蹂', '上', '酵', '苑', '沸', '涩', '亡', '邵', '挺', '们',
             '怪', '介', '忽', '矗', '钉', '呐', '扰', '埂', '巅', '茁', '普', '足', '锅', '玩', '缺',
             '醉', '卸', '蚊', '育', '猫', '钓', '锐', '聚', '砾', '庚', '歼', '娜', '挑', '锋', '锤', '未', '防',
             '拌', '赎', '唬', '混', '衣', '漱', '哺', '稿', '耐', '喘', '瓦', '翰', '壳', '拯', '睬',
             '畜', '冲', '瓢', '壤', '类', '粘']
