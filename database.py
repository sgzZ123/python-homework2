import sqlite3


# 数据库处理类
class Operator:
    def __init__(self, BaseName):
        self.name = BaseName + '.db'

    # 建立新的表
    def CreateNewTable(self, TableName, ListName):
        conn = sqlite3.connect(self.name)
        c = conn.cursor()
        # 生成命令
        command = 'CREATE TABLE %s (' % (TableName,)
        for names in ListName:
            if names == 'year':
                command += "'%s' text primary key not null," % (names,)
            else:
                command += "'%s' text not null," % (names,)
        command = command.strip(',')
        command += ');'
        # 执行命令
        c.execute(command)
        print('create database successfully')
        conn.commit()
        conn.close()

    # 插入数据
    def InsertInfo(self, TableName, DataList):
        conn = sqlite3.connect(self.name)
        c = conn.cursor()
        # 获得列的名称
        c.execute("PRAGMA table_info(%s)" % (TableName,))
        structure = c.fetchall()
        items = []
        for contents in structure:
            items.append(contents[1])
        # 生成插入数据的命令，并插入数据
        for datas in DataList:
            item_string = "'" + str(items).strip('[').strip(']').replace("'", '').replace(',',"','") + "'"
            item_string = item_string.replace(' ', '')
            data_string = ''
            for item in items:
                data_string += "'" + datas[item] + "'" + ','
            data_string = data_string.strip(',')
            c.execute('INSERT INTO %s (%s) \
                           VALUES (%s);' % (TableName, item_string, data_string))

        conn.commit()
        conn.close()
        print('Insert Finished')

    # 从数据库中获得数据
    def GetData(self, TableName):
        conn = sqlite3.connect(self.name)
        c = conn.cursor()
        # 从指定表中获得所有数据
        c.execute("select * from %s;" % (TableName,))
        datas = c.fetchall()
        # 从指定表中获得列名称
        c.execute("PRAGMA table_info(%s)" % (TableName,))
        structure = c.fetchall()
        items = [content[1] for content in structure]
        conn.commit()
        conn.close()
        # 将所得的数据和列名称对应起来组成字典列表
        Info = []
        for data in datas:
            Info.append(dict(zip(items, data)))
        return Info


