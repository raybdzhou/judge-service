from flask import Flask, make_response
from judge import Judge
import json

judge = None
app = Flask(__name__)
with open('config.json', 'r') as jsonfile:
    json_str = json.load(jsonfile)
node_map = {}
node_map_list = json_str["nodes"]
for n in node_map_list:
    node_map[n["nid"]] = n["ip_addr"]

@app.route('/')
def proxy():
    res, headers_server = judge.run()
    rsp = make_response(res)
    rsp.headers["Server"] = headers_server
    return rsp

if __name__== "__main__":
    # 采用一致表决
    # judge = Judge(node_map, True)
    # 采用多模表决
    judge = Judge(node_map)
    app.run(host='0.0.0.0',port=5050)