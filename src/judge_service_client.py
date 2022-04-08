import grpc
import judge_service_pb2
import judge_service_pb2_grpc

def run():
    # 连接 rpc 服务器
    channel = grpc.insecure_channel('localhost:50051')
    # 调用 rpc 服务
    stub = judge_service_pb2_grpc.JudgeServiceStub(channel)
    response = stub.GetFeature(judge_service_pb2.JudgeServiceReq(id=1001))
    print(f'Client received: {response.result}')

if __name__ == '__main__':
    run()