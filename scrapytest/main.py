from scrapy.cmdline import execute

import sys
import os
import threading
from data5u import GetIpThread

def scrapy():
    GetIpThread(apiUrl, fetchSecond).start();


if __name__ == '__main__':
    order = "f9ae0d4529fad58993ec0d27a4b74baf";
    # 获取IP的API接口
    apiUrl = "http://api.ip.data5u.com/dynamic/get.html?order=" + order;
    # 获取IP时间间隔，建议为5秒
    fetchSecond = 5;
    # 开始自动获取IP
    # GetIpThread(apiUrl, fetchSecond).start();

    # threading.Thread(target=scrapy)

    # sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    # execute(["scrapy", "crawl", "lianjia"])

    from scrapy import cmdline
    cmdline.execute('scrapy crawl lianjia'.split())

