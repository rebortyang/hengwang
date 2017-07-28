from datetime import datetime
import requests
import random
import json


class TodayOnHistory(object):
    """
    处理历史的今天返回的数据
    """
    def __init__(self):
        """
        初始化相关数据，包括接口的url，param
        return None
        """
        month = datetime.now().month
        day = datetime.now().day

        self.url = 'http://api.juheapi.com/japi/toh'
        key = '11e32e4203c1305e3bfd0f1a71ba254a'
        self.param = {'v': '1.0', 'month': month, 'day': day, 'key': key}

    def get_history(self):
        wb_data = requests.get(self.url, self.param)
        data = wb_data.json()
        if data['error_code'] == 0:
            result = data['result']
            rodom_num = random.randint(0, len(result) - 1)
            return json.dumps(result[rodom_num])
        else:
            return json.dumps(data)
