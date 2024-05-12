import requests
import urllib3
from web3 import Web3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

import requests
import time

MAX_PROXY_CHECK_ATTEMPTS = 5
SLEEP_TIME = 60

def check_proxy(proxy):
    for i in range(MAX_PROXY_CHECK_ATTEMPTS):
        try:
            response = requests.get('https://myip.ipip.net', proxies=proxy, timeout=5)
            print('验证成功, IP信息: ', response.text)
            return True
        except Exception as e:
            print('代理失效，等待1分钟后重新验证')
            time.sleep(SLEEP_TIME)
    print('代理验证失败，无法继续执行任务')
    return False

# 修改代理
PROXY = {
    'http': 'http://7182*****a:ce65b53e-global@*******:1000',
    'https': 'http://7182*****a:ce65b53e-global@*******:1000',
}

proxy_status = check_proxy(PROXY)

def getTestToken(address):
    headers = {
        'Host': 'mevm.devnet.m1.movementlabs.xyz',
        'Connection': 'close',
        'sec-ch-ua': '";Not A Brand";v="99", "Chromium";v="88"',
        'Accept': 'application/json, text/plain, */*',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36',
        'Content-Type': 'application/json',
        'Origin': 'https://faucet.movementlabs.xyz',
        'Sec-Fetch-Site': 'same-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://faucet.movementlabs.xyz/',
        'Accept-Language': 'zh-CN,zh;q=0.9',
    }

    json_data = {
        'jsonrpc': '2.0',
        'id': 1,
        'method': 'eth_faucet',
        'params': [
            '{}'.format(address),
        ],
    }
    for i in range(100):
        try:
            response = requests.post('https://mevm.devnet.m1.movementlabs.xyz/', headers=headers, json=json_data,
                                     proxies=PROXY,
                                     verify=False,
                                     timeout=5)
            print('[{}] {}尝试领水中...'.format(i,address))
            print(response.json())
        except KeyboardInterrupt:
            print("Interrupted by user")
            break
        except:
            pass

# 查询余额
def checkBalance(address):
    web3 = Web3(Web3.HTTPProvider('https://mevm.devnet.m1.movementlabs.xyz/v1/'))
    balance_wei = web3.eth.get_balance(address)
    balance_eth = web3.from_wei(balance_wei,'ether')
    return balance_eth

with open('seeds.txt') as f:
    file = f.readlines()

# 获取地址
address = []
for x in file:
    line = x.rstrip()
    address.append(line.split(':')[0])

#领水
for i in address:
    getTestToken(i)

# 查询余额
balance={}
for i in address:
    balance[i] = str(checkBalance(i))

# 写入地址
with open('balances.txt', 'w') as f:
    for address, amount in balance.items():
        f.write(f"{address}\t{amount}\n")
