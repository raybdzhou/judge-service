from dataclasses import dataclass
import pymysql
import json
@dataclass
class DatabaseInstance:
    host: str
    user: str
    passwd: str
    database: str
    table: str
with open('config.json', 'r') as jsonfile:
    json_str = json.load(jsonfile)

db_config = json_str["db_config"]
db_instance = DatabaseInstance(
    db_config["host"],
    db_config["user"],
    db_config["passwd"],
    db_config["database"],
    db_config["table"]
)
@dataclass
class DBManager:
    db = pymysql.connect(
        host = db_instance.host,
        user = db_instance.user,
        password = db_instance.passwd,
        database = db_instance.database)
    
    def get_rows(self, key = None):
        return self.get_row_default(id = key)

    # DO NOT EDIT!
    def get_row_default(self, **kwargs):
        """
        rows: number of data to be queried
        **kwargs: conditions
        """

        conds = []
        for k, v in kwargs.items():
            if v is not None:
                conds.append(f"{k}={v}")
        sql_cond = f" WHERE {' and '.join(conds)}" if len(conds) > 0 else ""
        sql = f"SELECT * FROM {db_instance.table}{sql_cond};"
        try:
            cursor = self.db.cursor()
            cursor.execute(sql)
            return cursor.fetchall()
        except Exception as e:
            raise e
    
    def set_row(self, _id = None, _access = None, new_flag = True):
        if _id is None:
            print("ID is not allowed to be None.")
            raise
        if _access is None:
            print("ACCESS is not allowed to be None.")
            raise
        if new_flag:
            self.set_row_default(id = _id, access = _access)
        else:
            self.update_row_default(id = _id, access = _access)

    
    def set_row_default(self, **kwargs):
        """
        **kwargs: key-value to be saved
        """

        ks, vs = [], []
        for k, v in kwargs.items():
            ks.append(k)
            vs.append(v)
        sql = f"INSERT INTO {db_instance.table} ({','.join(ks)}) VALUES ({','.join(vs)});"
        try:
            cursor = self.db.cursor()
            cursor.execute(sql)
            self.db.commit()
            return True
        except Exception as e:
            raise e
    
    def del_row_default(self, **kwargs):
        """
        **kwargs: conditions
        """

        conds = []
        for k, v in kwargs.items():
            if v is not None:
                conds.append(f"{k}={v}")
        sql_cond = f" WHERE {' and '.join(conds)}" if len(conds) > 0 else ""
        sql = f"DELETE FROM {db_instance.table}{sql_cond};"
        try:
            cursor = self.db.cursor()
            cursor.execute(sql)
            self.db.commit()
        except Exception as e:
            raise e
    
    def update_row_default(self, **kwargs):
        """
        **kwargs: key-value to be saved
        """
        
        sets = []
        for k, v in kwargs.items():
            if v is not None:
                sets.append(f"{k}={v}")
        sql_sets = f" SET {','.join(sets)}" if len(sets) > 0 else ""
        sql = f"UPDATE {db_instance.table}{sql_sets};"
        try:
            cursor = self.db.cursor()
            cursor.execute(sql)
            self.db.commit()
            return True
        except Exception as e:
            raise e

    def close(self):
        self.db.close()