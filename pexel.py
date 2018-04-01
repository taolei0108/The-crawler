import re

import requests
from bs4 import BeautifulSoup
import os
from multiprocessing import Pool

photos = []


headers = {
    'Accept': '*/*',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:59.0) Gecko/20100101 Firefox/59.0'
}


def get_data(url):
    re = requests.get(url, headers=headers)
    soup = BeautifulSoup(re.text, 'lxml')
    imgs = soup.select('article.photo-item > a > img')
    for img in imgs:
        photo = img.get('src')
        photos.append(photo)
    wget()


def wget():
    global  photos
    path = os.path.abspath('.') + '/picture'
    if os.path.isdir(path) is False:
        os.mkdir(path)
    for photo in photos:
        photo_name = re.findall('\/\d+\/(.*)\?auto', photo)
        if photo_name:
            Photo = os.path.join(path, photo_name[0])
            res = requests.get(photo, headers=headers)
            f = open(Photo, 'wb')
            f.write(res.content)
            f.close()
    photos = []

if __name__ == '__main__':
    urls = ["https://www.pexels.com/?page={}".format(str(i)) for i in range(1, 20)]
    pool = Pool(12)
    pool.map(get_data, urls)
