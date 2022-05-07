from flask import Flask, request
import grpc
import db_service_pb2
import db_service_pb2_grpc
import random
import json
import time

app = Flask(__name__)
cache = {}
cache_mutex = 0
with open('config.json', 'r') as jsonfile:
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
    stub = db_service_pb2_grpc.DBServiceStub(channel)
    response = stub.GetAllData(db_service_pb2.DBServiceGetAllReq(nid=_nid))
    results = response.results
    for result in results:
        cache[result.id] = result.access

def getData(_id):
    # 连接 rpc 服务器
    channel = grpc.insecure_channel(dst)
    # 调用 rpc 服务
    stub = db_service_pb2_grpc.DBServiceStub(channel)
    response = stub.GetSingleData(db_service_pb2.DBServiceGetSingleReq(nid=_nid, id=_id))
    return response.result

def setData(_id, _access):
    # 连接 rpc 服务器
    channel = grpc.insecure_channel(dst)
    # 调用 rpc 服务
    stub = db_service_pb2_grpc.DBServiceStub(channel)
    _data = db_service_pb2.Body(id=_id, access=_access)
    response = stub.SetData(db_service_pb2.DBServiceSetReq(nid=_nid, data=_data))
    return response.op_status

def updateData(_id, _access):
    # 连接 rpc 服务器
    channel = grpc.insecure_channel(dst)
    # 调用 rpc 服务
    stub = db_service_pb2_grpc.DBServiceStub(channel)
    _data = db_service_pb2.Body(id=_id, access=_access)
    response = stub.UpdateData(db_service_pb2.DBServiceUpdateReq(nid=_nid, data=_data))
    return response.op_status


@app.route('/setdata', methods=['POST', 'GET'])
def handle_setdata_request():
    try:
        while cache_mutex != 0:
            time.sleep(1000)
        dump_cache()
        return_code = setData(int(request.form["id"]), int(request.form["access"]))
        dump_cache()
        return return_code
    except Exception as e:
        raise e

@app.route('/updatedata', methods=['POST', 'GET'])
def handle_update_request():
    try:
        while cache_mutex != 0:
            time.sleep(1000)
        dump_cache()
        return_code = updateData(int(request.form["id"]), int(request.form["access"]))
        if return_code == 0 and int(request.form["id"]) in cache:
            cache.pop(int(request.form["id"]))
        dump_cache()
        return return_code
    except Exception as e:
        raise e

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

    while cache_mutex != 0:
        time.sleep(1000)

    select_key = data_deal([i for i in range(1, data_count+1)], percentages)
    if select_key in cache:
        return str(cache[select_key])
    else:
        res = getData(select_key)
        cache[res.id] = res.access
        return str(res.access)

if __name__ == '__main__':
    loadData()
    # 启动 web 服务
    app.run(host='0.0.0.0',port=8080)