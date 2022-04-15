from dataclasses import dataclass
from db_manager import DBManager
@dataclass
class Process:
    dbm = DBManager()
    def run(self, key):
        res = self.dbm.get_rows(key)
        return res