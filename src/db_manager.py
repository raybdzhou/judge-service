import pymysql


class DBManager:
    db = pymysql.connect(host='localhost', user='testuser', password='test123', database='testdb')
    cursor = db.cursor()
    @staticmethod
    def get(key):
        return DBManager.cursor.execute(f'select {key} from testdb.test_table')
    
    @staticmethod
    def save(value):
        return DBManager.cursor.execute(f'insert into test.test_table (id) values ({value})')
    
    @staticmethod
    def close():
        DBManager.db.close()
