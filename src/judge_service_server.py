import grpc
import judge_service_pb2
import judge_service_pb2_grpc

import asyncio
import logging

from process import Process

class JudgeService(judge_service_pb2_grpc.JudgeService):
    def GetFeature(self, request, context):
        print(f"get request {request} from {context}")
        res = int(Process().run(request.id))
        return judge_service_pb2.JudgeServiceRsp(result=res)

async def serve() -> None:
    server = grpc.aio.server()
    judge_service_pb2_grpc.add_JudgeServiceServicer_to_server(JudgeService(), server)
    listen_addr = '[::]:50051'
    server.add_insecure_port(listen_addr)
    logging.info("Starting server on %s", listen_addr)
    await server.start()
    await server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(serve())