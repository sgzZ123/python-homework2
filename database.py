import sqlite3


class Operator:
    def __init__(self, BaseName):
        self.name = BaseName + '.db'

    def CreateNewTable(self, TableName, ListName):
        conn = sqlite3.connect(self.name)
        c = conn.cursor()
        command = 'CREATE TABLE %s (' % (TableName,)
        for names in ListName:
            if names == 'year':
                command += "'%s' text primary key not null," % (names,)
            else:
                command += "'%s' text not null," % (names,)
        command = command.strip(',')
        command += ');'
        c.execute(command)
        print('create database successfully')
        conn.commit()
        conn.close()

    def InsertInfo(self, TableName, DataList):
        conn = sqlite3.connect(self.name)
        c = conn.cursor()
        c.execute("PRAGMA table_info(%s)" % (TableName,))
        structure = c.fetchall()
        items = []
        for contents in structure:
            items.append(contents[1])
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

    def GetData(self, TableName):
        conn = sqlite3.connect(self.name)
        c = conn.cursor()
        c.execute("select * from %s;" % (TableName,))
        datas = c.fetchall()
        c.execute("PRAGMA table_info(%s)" % (TableName,))
        structure = c.fetchall()
        items = [content[1] for content in structure]
        conn.commit()
        conn.close()
        Info = []
        for data in datas:
            Info.append(dict(zip(items, data)))
        return Info


