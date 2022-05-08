import requests
host = "192.168.6.133"
port = 5050
expect_res = 1
def tester(times = None):
    if times is None or times < 0:
        print("times is not allowed")
        raise
    dst = f"http://{host}:{port}"
    correct_times = 0
    for i in range(times):
        req = requests.get(dst)
        if req.status_code == 200 and int(req.text) == expect_res:
            correct_times += 1
    print("Correct Rate:", correct_times/times)

if __name__=="__main__":
    tester(1000)