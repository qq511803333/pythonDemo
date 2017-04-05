# -*-utf-8 -*-
import requests, json
import time, datetime
import pymysql

conn = pymysql.connect(
    user='root',
    password='guang888',
    host='localhost',
    database='mydatabase'
)
db = conn.cursor();

requests.packages.urllib3.disable_warnings()
i = 5;
while i:
    a = str(i)
    response = requests.get(
        "https://kyfw.12306.cn/otn/leftTicket/queryX?leftTicketDTO.train_date=2017-" + datetime.datetime.now().strftime(
            "%m") + "-0" + a + "&leftTicketDTO.from_station=BJP&leftTicketDTO.to_station=JZD&purpose_codes=ADULT",
        headers={
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, sdch, br",
            "Accept-Language": "zh-CN,zh;q=0.8,en;q=0.6",
            "Cache-Control": "max-age=0",
            "Connection": "keep-alive",
            "Cookie": "JSESSIONID=0A02F045C473534438EDBF1743A5F63DCBB0CF541F; __NRF=A252AD1CCAAD8A8F9B94BD60415A87F3; BIGipServerotn=1173357066.50210.0000; _jc_save_fromStation=%u5317%u4EAC%2CBJP; _jc_save_toStation=%u9526%u5DDE%2CJZD; _jc_save_fromDate=2017-04-06; _jc_save_toDate=2017-04-03; _jc_save_wfdc_flag=dc",
            "Host": "kyfw.12306.cn",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
        }, verify=False)
    i += 1;
    time.sleep(3)
    print(response.text)
    data = json.loads(response.text)
    for dataStr in data['data']:
        query = dataStr['queryLeftNewDTO']
        sql = ("insert into train (data) values ('%s')" % str((query['start_station_telecode'])))
        print(sql)
        try:
            db.execute(sql)
            conn.commit()
        except:
            conn.rollback()
if (i == 8):
    i = 1
conn.close();

