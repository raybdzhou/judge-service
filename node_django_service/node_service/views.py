from django.http import HttpResponse
import grpc
import node_service.db_service_pb2
import node_service.db_service_pb2_grpc
import random
import json
import time

cache = {}
cache_mutex = 0
with open('../node_service/config.json', 'r') as jsonfile:
    json_str = json.load(jsonfile)
_nid = json_str["nid"]
data_count = json_str["data_count"]
percentages = json_str["percentages"]
dst = json_str["rpc_dst"]

def dump_cache():
    cache_mutex ^= 1

def loadData():
    # 连接 rpc 服务器
    channel = grpc.insecure_channel(dst)
    # 调用 rpc 服务
    stub = node_service.db_service_pb2_grpc.DBServiceStub(channel)
    response = stub.GetAllData(node_service.db_service_pb2.DBServiceGetAllReq(nid=_nid))
    results = response.results
    for result in results:
        cache[result.id] = result.access

def getData(_id):
    # 连接 rpc 服务器
    channel = grpc.insecure_channel(dst)
    # 调用 rpc 服务
    stub = node_service.db_service_pb2_grpc.DBServiceStub(channel)
    response = stub.GetSingleData(node_service.db_service_pb2.DBServiceGetSingleReq(nid=_nid, id=_id))
    return response.result

def handle_request():
    def data_deal(data, percentage):
        x = random.uniform(0, 1)
        cumulative_probability = 0.0
        for item, item_probability in zip(data, percentage):
            cumulative_probability += item_probability
            if x < cumulative_probability:
                break
        return item

    while cache_mutex != 0:
        time.sleep(1000)

    select_key = data_deal([i for i in range(1, data_count+1)], percentages)
    if select_key in cache:
        return str(cache[select_key])
    else:
        res = getData(select_key)
        cache[res.id] = res.access
        HttpResponse(str(res.access))

def index(request):
    return HttpResponse(handle_request())

loadData()