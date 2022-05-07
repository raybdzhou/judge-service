from dataclasses import dataclass
from db_manager import DBManager
import db_service_pb2

@dataclass
class Process:
    dbm = DBManager()

    def get_all_data(self):
        raw_data = self.dbm.get_rows()
        return [db_service_pb2.Body(id=_id, access=_access) for _id, _access in raw_data]
    
    def get_single_data(self, id):
        raw_data = self.dbm.get_rows(key = id)
        return [db_service_pb2.Body(id=_id, access=_access) for _id, _access in raw_data]
    
    def set_data(self, id, access):
        if self.dbm.set_row(id, access) is True:
            return 0
        else:
            return 1
    
    def update_data(self, id, access):
        if self.dbm.set_row(id ,access, False) is True:
            return 0
        else:
            return 1