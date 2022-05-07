from flask import Flask
import grpc
import db_service_pb2
import db_service_pb2_grpc
import random
import json

app = Flask(__name__)
cache = {}
with open('config.json', 'r') as jsonfile:
    json_str = json.load(jsonfile)
nid = json_str["nid"]
percentages = json_str["percentages"]

@app.route('/')
def handle_request():
    def data_deal(data, percentage):
        x = random.uniform(0, 1)
        cumulative_probability = 0.0
        for item, item_probability in zip(data, percentage):
            cumulative_probability += item_probability
            if x < cumulative_probability:
                break
        return item

    return str(data_deal(list(cache.values())[:5], percentages))

if __name__ == '__main__':
    # 连接 rpc 服务器
    channel = grpc.insecure_channel('localhost:50051')
    # 调用 rpc 服务
    stub = db_service_pb2_grpc.DBServiceStub(channel)
    response = stub.GetAllData(db_service_pb2.DBServiceGetAllReq(nid=1))
    results = response.results
    for result in results:
        cache[result.id] = result.access
    print(list(cache.values()))

    # 启动 web 服务
    app.run()