import requests
import json
import random
from settings import *

verify_num = 0
VERIFY_LOOP = 5
TIME_OUT = 8
top_proxy_url = 'http://127.0.0.1:5000/https/top/1'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.3"
}

VERIFY_URL = {'http': VERIFY_HTTP_URL, 'https': VERIFY_HTTPS_URL}

def verify(host, port, type):
    try:
        proxies = "%s://%s:%s" % (str(type), str(host), str(port))
        res = requests.get(url=VERIFY_URL[type], headers=headers, timeout=TIME_OUT, proxies={type: proxies})
        print('res.status_code  :  '+str(res.status_code))
        # if res.status_code == requests.codes.ok:
        #     return True
        # else:
        #     return False
        return True
    except:
        return False

def choice(ip_proxys):
    if len(ip_proxys) == 0:
        return None
    proxy = random.choice(ip_proxys)
    return str("%s://%s:%s" % (proxy['type'], proxy['host'], proxy['port']))
    # if verify(proxy['host'], proxy['port'], proxy['type']):
    #     return str("%s://%s:%s" % (proxy['type'], proxy['host'], proxy['port']))
    # ip_proxys.remove(proxy)
    # return choice(ip_proxys)



def get():
    global verify_num
    verify_num = verify_num + 1
    res = requests.get(top_proxy_url, headers=headers)
    ip_porxys = json.loads(res.text)
    proxy = choice(ip_porxys)
    if proxy is None:
        return get()
    verify_num = 0
    return proxy



if __name__ == '__main__':
    get()


