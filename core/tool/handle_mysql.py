import pymysql

dbinfo = {
    "host": "",
    "user": "root",
    "password": "xxxx",
    "port": 0000}

class HandleMysql():
    """ mysql 操作 """
    def __init__(self, db_cof, database):
        """
        :param db_cof: 配置文件
        :param database:表名
        """
        self.db_cof = db_cof
        self.db = pymysql.connect(database=database,cursorclass=pymysql.cursors.DictCursor,**db_cof)# InnoDB引擎 可以设置 autocommit=True

        self.cursor = self.db.cursor()# 链接数据库,使用cursor()方法获取操作游标

    def select(self, sql):
        ''' SQL 查询语句 '''
        self.cursor.execute(sql)
        results = self.cursor.fetchall()
        return results

    def execute(self, sql):
        ''' SQL 删除、提交、修改语句,
        cursor.execute(sql) 执行Sql语句, db.commit()提交修改, db.rollback()发生错误时回滚 '''
        try:
           self.cursor.execute(sql)
           self.db.commit()
        except:
           self.db.rollback()

    def close(self):
        '''关闭数据库连接'''
        self.db.close()

