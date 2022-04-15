from dataclasses import dataclass
import pymysql
@dataclass
class DatabaseInstance:
    host: str
    user: str
    passwd: str
    database: str

db_instance = DatabaseInstance('localhost', 'judgeuser', 'Judgeuser123@', 'judge123')
@dataclass
class DBManager:
    db = pymysql.connect(
        host = db_instance.host,
        user = db_instance.user,
        password = db_instance.passwd,
        database = db_instance.database)
    
    def get_rows(self, key):
        cursor = self.db.cursor()
        cursor.execute("select id, access from judge_table where id = %s;" % key)
        raw_data = cursor.fetchall()
        results = []
        for raw in raw_data:
            results.append(raw[1])
        return results.pop()
    
    
    def close(self):
        self.db.close()
