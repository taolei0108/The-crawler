import requests
import json

headers = {
    'Accept': 'application/json',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
  #  'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': 'Hm_lvt_0c0e9d9b1e7d617b3e6842e85b9fb068=1521814736,1521905115,1522587605; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22162533a0cd65d7-0529121ca5bad1-1269624a-1327104-162533a0cd8722%22%2C%22%24device_id%22%3A%22162533a0cd65d7-0529121ca5bad1-1269624a-1327104-162533a0cd8722%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.baidu.com%2Flink%22%2C%22%24latest_referrer_host%22%3A%22www.baidu.com%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%7D%7D; signin_redirect=https%3A%2F%2Fwww.jianshu.com%2Fp%2F4504f0038a73; read_mode=day; default_font=font2; locale=zh-CN; Hm_lpvt_0c0e9d9b1e7d617b3e6842e85b9fb068=1522587768; _m7e_session=fb3d3292906dfb300e4b3fe81aa960ca',
    'Host': 'www.jianshu.com',
    'If-None-Match': 'W/"a7294b2d0c1fff431f342d3d8b8df6ef"',
    'Referer': 'https://www.jianshu.com/p/4504f0038a73',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:59.0) Gecko/20100101 Firefox/59.0'
}

if __name__ == '__main__':
    url = 'https://www.jianshu.com/notes/25867399/included_collections?page=1'

 #   data = {
  #      'page': '1'
   # }

    re = requests.get(url, headers = headers)
  #  print(re.text)

    json_data = json.loads(re.text)
    infos = json_data['collections']
    for info in infos:
        print(info['title'])

