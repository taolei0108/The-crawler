import os
import requests

#data = {
#    'source': 'index_nav',
#    'form_email': '805416615@qq.com',
#    'form_password': 'qaz.1233'
#}

#headers = {
#    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:59.0) Gecko/20100101 Firefox/59.0'
#}

#re = requests.post('https://www.douban.com/accounts/login', data=data, headers=headers)

headers = {
    'Cookie': 'll="108288"; bid=eDRoevsBVI4; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1522510023%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3Dfsf0T_69dv0k5z37-aPVOis2XEHmQ-emK4Gy5j0zQW39xtkCBm3aj0EzVMNRKKwj%26wd%3D%26eqid%3Da28a0edb0002157e000000025abfa8c1%22%5D; _pk_id.100001.8cb4=d121a17248d82ec2.1522510023.1.1522511798.1522510023.; _pk_ses.100001.8cb4=*; __utma=30149280.1634874711.1522510030.1522510030.1522510030.1; __utmb=30149280.9.10.1522510030; __utmc=30149280; __utmz=30149280.1522510030.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; ps=y; __yadk_uid=t6VO5WO2aGNWWeUuEQzmlr04BVz7Io7N; push_noty_num=0; push_doumail_num=0; __utmv=30149280.17623; ap=1; dbcl2="176230526:S7RSGI3Ubyk"; ck=FNHq'
}

re = requests.get('https://www.douban.com', headers=headers)

print(re.text)