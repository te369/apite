""" 异步操作mysql """
import asyncio
import aiomysql

class MysqlBase:
    def __init__(self,host,user,password,sql_str):
        """
        :param host: mysql host
        :param user: 用户名
        :param password: 密码
        :param sql_str: sql语句
        """
        self.host = host
        self.user = user
        self.password = password
        self.sql_str = sql_str

    async def execute(self):
        """ 先连接 mysql ,获取下标,执行语句,等待结果完成,返回结果
        :param conn： 创建连接
        :param cur: 获取下标
        :param result 获取结果
        """
        conn = await aiomysql.connect(host=self.host,port=3322,user="root",password=self.password,db="mysql")
        cur = await conn.cursor()

        await cur.execute(self.sql_str)# 网络IO操作 执行sql
        result = await cur.fetchall() # 网络IO操作：获取SQL结果

        await cur.close()
        conn.close() # 网络Io 操作 ：关闭链接

        return result



mysql1 = MysqlBase(host="47.101.187.47",user="root",password="ying9366",sql_str="SELECT Host,User FROM user").execute()
s = asyncio.run(mysql1)
print(s)
