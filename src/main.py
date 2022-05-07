import random
from collections import defaultdict

all_amount = 4  # 总共的执行体
choice_amount = 3  # 在线执行体
id_type = [i for i in range(all_amount)]  # 定义的所有执行体id 从0开始
result_type = [1, 2, 3, 4, 5]  # 输出结果的范围
result_type_amount = len(result_type)  # 输出结果的种类数量
percentages0 = [0.7, 0.12, 0.02, 0.04, 0.12]
percentages1 = [0.7, 0.04, 0.06, 0.10, 0.10]
percentages2 = [0.7, 0.08, 0.08, 0.04, 0.1]
percentages3 = [0.7, 0.08, 0.06, 0.06, 0.1]
percentage_group = [percentages0, percentages1, percentages2, percentages3]

choice_id_list = [0 for i in range(choice_amount)]  # 选中的在线执行体id
choice_output_list = [0 for i in range(choice_amount)]  # 执行体各自输出值
result_list = [choice_id_list, choice_output_list]  # 合并的二维list  [[id1,id2..],[output1,output2..]]

result_cnt_list = [[0 for i in range(result_type_amount)]]  # 输出结果的数量统计
result_amount_list = [result_type, result_cnt_list]  # 输出结果的数量统计的二维list[[type1,type2..],[amount1,amount2..]]

S = [0 for i in range(result_type_amount)]  # 一致度
F = [0 for i in range(result_type_amount)]  # 历史置信度
choice_time_list = [0 for i in range(all_amount)]  # 被选为在线执行体的次数
output_time_list = [0 for i in range(all_amount)]  # 采纳为表决结果的次数
F_list = [id_type, choice_time_list, output_time_list]

measure_list = [0.6666667, 0.3333333]


def data_deal(data, percentage):
    x = random.uniform(0, 1)
    cumulative_probability = 0.0
    for item, item_probability in zip(data, percentage):
        cumulative_probability += item_probability
        if x < cumulative_probability:
            break
    return item


def web_data_get():
    result_amount_list[1] = [0 for i in range(result_type_amount)]  # 清空存储数量容器
    # 存储数据出现的次数
    result = [0, 0, 0, 0, 0]
    # 存储输出结果
    nums = [0 for i in range(choice_amount)]
    # 随机输出[0,3]中的3个不重复数
    choice_list = random.sample(range(0, all_amount), choice_amount)
    result_list[0] = choice_list

    temp_cnt = 0
    for temp in choice_list:
        result_list[1][temp_cnt] = data_deal(result_type, percentage_group[temp])
        result_amount_list[1][result_type.index(result_list[1][temp_cnt])] += 1
        temp_cnt += 1


def get_measure():
    total_result = [0 for i in range(result_type_amount)]
    temp_result_amount_list = result_amount_list
    temp_result_list = result_list
    print(result_amount_list, result_list)

    # 计算一致度集合S
    temp_cnt = 0
    for re in temp_result_amount_list[1]:
        S[temp_cnt] = re / choice_amount
        temp_cnt += 1

    # 计算历史度集合F
    for i in range(result_type_amount):
        temp_s = temp_result_amount_list[1][i]
        temp_p = 0
        if temp_s != 0: 
            cnt = 0
            for j in temp_result_list[1]:
                if j == result_type[i]:
                    temp_id = temp_result_list[0][cnt]
                    if F_list[1][temp_id] != 0:
                        temp_pk = F_list[2][temp_id] / F_list[1][temp_id]
                        temp_p += temp_pk
                cnt += 1
            F[i] = temp_p / temp_s
        else:
            F[i] = 0

    for i in range(result_type_amount):
        total_result[i] = measure_list[0] * S[i] + measure_list[1] * F[i]
    total_output = result_type[total_result.index(max(total_result))]

    # 更新数据
    for i in result_list[0]:
        F_list[1][id_type.index(i)] += 1
    temp_id_cnt = 0
    for i in temp_result_list[1]:
        if i == total_output:
            F_list[2][temp_result_list[0][temp_id_cnt]] += 1
        temp_id_cnt += 1
    return total_output


def judge(all_results):
    # 去除None
    m = sorted([i for i in all_results if i])
    print(m)
    m.reverse()
    print(m)

def data_judge_unanimous():
    max_time_list = []
    mylist = result_amount_list[1]
    temp_dict = defaultdict(list)
    for i, x in enumerate(mylist):
        temp_dict[x].append(i)
    test_list = temp_dict[max(k for k, v in temp_dict.items() if len(v) >= 1)]
    for i in test_list:
        max_time_list.append(result_type[i])
    if len(max_time_list) == 1:
        return max_time_list[0]  # 只有唯一最大值
    else:
        return random.choice(max_time_list)  # 有多个最大值，随机返回一个


def data_test(time):
    one_1 = 0
    two_1 = 0
    three_1 = 0
    four_1 = 0
    five_1 = 0
    one_2 = 0
    two_2 = 0
    three_2 = 0
    four_2 = 0
    five_2 = 0

    for i in range(time):
        all_output_list = process()
        result = all_output_list[0]
        if result == 1:
            one_1 = one_1 + 1
        elif result == 2:
            two_1 = two_1 + 1
        elif result == 3:
            three_1 = three_1 + 1
        elif result == 4:
            four_1 = four_1 + 1
        elif result == 5:
            five_1 = five_1 + 1

        result = all_output_list[1]
        if result == 1:
            one_2 = one_2 + 1
        elif result == 2:
            two_2 = two_2 + 1
        elif result == 3:
            three_2 = three_2 + 1
        elif result == 4:
            four_2 = four_2 + 1
        elif result == 5:
            five_2 = five_2 + 1
    print(one_1/time, two_1/time, three_1/time, four_1/time, five_1/time)
    print(one_2/time, two_2/time, three_2/time, four_2/time, five_2/time)


def process():

    # 获取一次数据
    web_data_get()

    # 一致裁决
    result_unanimous = data_judge_unanimous()

    # 多指标裁决
    result_measure = get_measure()

    return [result_unanimous, result_measure]


if __name__ == '__main__':
    data_test(10)
