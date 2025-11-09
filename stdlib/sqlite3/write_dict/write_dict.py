import sqlite3

class DbStatement(object):
    @classmethod
    def insert(self, row, header):
        values = [row.get(key, 0.0) for key in header]
        statement = "INSERT INTO mytable ({}) VALUES ({})".format(
                ','.join(repr(h) for h in header), 
                ','.join(repr(v) for v in values))
        return statement


class MyData(object):
    def __init__(self, dbfilename=':memory:'):
        self.connection = sqlite3.connect(dbfilename)
        self.table_name = 'users'
        self.header = ['alias', 'birth_year']
        cursor = self.connection.cursor()
        cursor.execute('DROP TABLE IF EXISTS {}'.format(self.table_name))
        cursor.execute('CREATE TABLE {}')


if __name__ == '__main__':
    header = ['uid', 'alias', 'duration', 'isadmin']
    print DbStatement.insert({'uid':501, 'alias': 'jwayne'}, header)
    print DbStatement.insert(dict(uid=502, alias='cbronson', duration=5.3), header)

    mydata = MyData()
