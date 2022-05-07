import random
import requests
import math
from functools import reduce
import json

with open('config.json', 'r') as jsonfile:
    json_str = json.load(jsonfile)
choice_amount = json_str["choice_amount"]
weights_matrix = json_str["weights_matrix"]

def calculate_wieghts():
    weights = list(map(lambda row: math.sqrt(reduce(lambda x, y: x*y, row)), weights_matrix))
    total_weights = sum(weights)
    weights = [w/total_weights for w in weights]
    return weights[0], weights[1]

class Judge:
    def __init__(self, nodes):
        self.nodes = nodes
        self.req_count = 0
        self.res_map = {}
        self.node_selected_map = {}
        self.node_output_map = {}
        self.current_output_map = {}
        self.F = {}
        self.S = {}
    
    def calculate_pk(self):
        pk = 0
        for k in self.node_selected_map:
            ak = self.node_output_map[k] if k in self.node_output_map else 0
            pk += ak / self.node_selected_map[k]
        return pk

    def run(self, unanimous=False):
        nodes_counts = len(self.nodes)
        selected_nodes = random.sample(range(0, nodes_counts), choice_amount)
        for i in selected_nodes:
            self.req_count += 1
            self.node_selected_map[i] = self.node_selected_map[i] + 1 if i in self.node_selected_map else 1
            self.node_output_map[i] = self.node_output_map[i] if i in self.node_output_map else 0
            res = requests.get(self.nodes[i]).text
            self.res_map[res] = self.res_map[res] + 1 if res in self.res_map else 1
            self.current_output_map[i] = res
        
        self.S = {k: v/self.req_count for k, v in self.res_map.items()}
        self.F = {k: self.calculate_pk()/v for k, v in self.res_map.items()}

        if unanimous:
            judge_list = []
            s_list = [(k, v) for k, v in self.S.items()].sort(key=lambda x: x[1], reverse=True)
            for s in s_list:
                if s[1] == s_list[0][1]:
                    judge_list.append(s[0])
            return random.choice(judge_list)
        else:
            judge_list = []
            for k in self.res_map:
                sp, fp = calculate_wieghts()
                judge_list.append((sp*self.S[k] + fp*self.F[k], k))
            judge_list.sort(key=lambda x: x[0], reverse=True)
            for i in self.current_output_map:
                if self.current_output_map[i] == judge_list[0][1]:
                    self.node_output_map[i] += 1
            self.current_output_map = {}
            return judge_list[0][1]
