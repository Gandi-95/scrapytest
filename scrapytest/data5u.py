

IPPOOL = [ ]

import requests;
import time;
import threading;
from data5u import IPPOOL;

# 获取代理IP的线程类
class GetIpThread(threading.Thread):
    def __init__(self,apiUrl, fetchSecond):
        super(GetIpThread, self).__init__();
        self.fetchSecond=fetchSecond;
        self.apiUrl=apiUrl;
    def run(self):
        while True:
            # 获取IP列表
            res = requests.get(self.apiUrl).content.decode()
            # 按照\n分割获取到的IP
            IPPOOL = res.split('\n');
            # 休眠
            print(IPPOOL)
            time.sleep(self.fetchSecond);