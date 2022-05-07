import grpc
import db_service_pb2
import db_service_pb2_grpc

import asyncio
import logging

from process import Process

class DBService(db_service_pb2_grpc.DBService):
    def GetAllData(self, request, context):
        print(f"[GetAllData]: get request {request.nid} from {context}")
        _results = Process().get_all_data()
        return db_service_pb2.DBServiceGetAllRsp(results=_results)
    
    def GetSingleData(self, request, context):
        print(f"[GetSingleData]: get request {request} from {context}")
        _results = Process().get_single_data(request.id)
        return db_service_pb2.DBServiceGetSingleRsp(result=_results[0])
    
    def SetData(self, request, context):
        print(f"[SetData]: get request {request} from {context}")
        status_code = Process().set_data(request.data.id, request.data.access)
        return db_service_pb2.DBServiceSetRsp(op_status=status_code)
    
    def Update(self, request, context):
        print(f"[UpdateData]: get request {request} from {context}")
        status_code = Process().update_data(request.data.id, request.data.access)
        return db_service_pb2.DBServiceUpdateRsp(op_status=status_code)


async def serve() -> None:
    server = grpc.aio.server()
    db_service_pb2_grpc.add_DBServiceServicer_to_server(DBService(), server)
    listen_addr = '[::]:50051'
    server.add_insecure_port(listen_addr)
    logging.info("Starting server on %s", listen_addr)
    await server.start()
    await server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(serve())