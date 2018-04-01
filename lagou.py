# -*- coding: utf-8 -*-
import requests
import os
import time
import json

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Connection': 'keep-alive',
    'Content-Length': '26',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1522514263,1522517457,1522569876; _ga=GA1.2.2075213195.1522514263; user_trace_token=20180401003743-d61088bc-3501-11e8-b6cd-5254005c3644; LGUID=20180401003743-d6109059-3501-11e8-b6cd-5254005c3644; _gid=GA1.2.798006095.1522514265; LG_LOGIN_USER_ID=432c3274347c7773acfeee621d3d0febc652a8809d295d94; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=2; gate_login_token=f676343106e68da68cc821a6fa2a300cfe32cc4d36696556; index_location_city=%E4%B8%8A%E6%B5%B7; SEARCH_ID=aab4eef5a9cf40d39383d2b812bef11d; WEBTJ-ID=20180401160435-162803c90c62a7-0c3ef6fe7a69998-1269624a-1327104-162803c90c8ce7; _gat=1; LGSID=20180401160436-5190fca2-3583-11e8-abdb-525400f775ce; PRE_UTM=m_cf_cpt_baidu_pc; PRE_HOST=www.baidu.com; PRE_SITE=https%3A%2F%2Fwww.baidu.com%2Fs%3Fwd%3D%25E6%258B%2589%25E5%258B%25BE%25E7%25BD%2591%26rsv_spt%3D1%26rsv_iqid%3D0xae4977460000c098%26issp%3D1%26f%3D8%26rsv_bp%3D0%26rsv_idx%3D2%26ie%3Dutf-8%26tn%3Dmonline_3_dg%26rsv_enter%3D1%26rsv_sug3%3D6%26rsv_sug1%3D4%26rsv_sug7%3D100; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Flp%2Fhtml%2Fcommon.html%3Futm_source%3Dm_cf_cpt_baidu_pc; LGRID=20180401160940-0739c20a-3584-11e8-b6d0-5254005c3644; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1522570180; _putrc=39E6557BEA333FEE; JSESSIONID=ABAAABAABEEAAJA5528CB0FDB9D485F3D16299012B6EF54; login=true; unick=%E9%99%B6%E7%A3%8A; TG-TRACK-CODE=index_code',
    'Host': 'www.lagou.com',
    'Referer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:59.0) Gecko/20100101 Firefox/59.0',
    'X-Anit-Forge-Code': '0',
    'X-Anit-Forge-Token': 'None',
    'X-Requested-With': 'XMLHttpRequest'
}

def get_data(url):
    for  i in range(1,19):
        data = {
            'first': 'true' if i == 1 else 'false',
            'kd': 'python',
            'pn': str(i)
        }
        re = requests.post(url, data=data, headers=headers)
        #print(re.text)
        json_data = json.loads(re.text)
        results = json_data['content']['positionResult']['result'] 
        for result in results:
            msg = {
                'industryField': result['industryField'],
                'education': result['education'],
                'workYear': result['workYear'],
                'city': result['city'],
                'positionAdvantage': result['positionAdvantage'],
                'createTime': result['createTime'],
                'salary': result['salary'],
                'positionName': result['createTime'],
                'companySize': result['createTime'],
                'companyShortName': result['companyShortName'],
                'companyFullName': result['companyFullName'],
                'financeStage': result['financeStage'],
                'jobNature': result['jobNature']
            }
            print(msg)
        exit()

if __name__ == '__main__':
    url = 'https://www.lagou.com/jobs/positionAjax.json?city=上海'
    get_data(url)
