import urllib
from urllib import request
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import requests

# user_id = 12345
# url = 'http://www.kinopoisk.ru/user/%d/votes/list/ord/date/page/2/#list' % (user_id)  # url для второй страницы
# url = 'https://vhbalancer01-a.akamaihd.net/ch/3708600a3d948c96c180c52d0e93a14b/2f0e54f420250c97a9d43fa9da1f6d2a/480/0.ts'  # url для второй страницы
# r = requests.get(url)
# with open('test.html', 'w+') as output_file:
#     output_file.write(r.text.encode('cp1251'))


# url = 'https://edge24.streamguard.cc/sec/1542497357/31303532b7ce4fe9dff24549d49161c481d461704f43e680/ivs/67/7b/6405b2e71e36.mp4/hls/tracks-3,4/segment'
#
# url = 'https://edge07.streamguard.cc/sec/1542511383/32333634f065e1f183914d13902810743037da3e1a635213/ivs/de/f6/52d1e8190573/hls/tracks-3,5/segment1.ts'
count = 10000
url = 'https://vhbalancer01-a.akamaihd.net/ch/3708600a3d948c96c180c52d0e93a14b/2f0e54f420250c97a9d43fa9da1f6d2a/480/'

for i in range(1, count):
    try:
        resp = request.urlopen(url + str(i) + '.ts?sid=sid&host=vh-20').read()

        f = open('Magik' + '.ts', 'ab')
        f.write(resp)
        f.close()
        print('complete: ', i)
    except urllib.error.HTTPError:
        print('download is broken')
        break

# resp = request.urlopen('https://pp.userapi.com/c845323/v845323267/128482/rD_cGv-Pj6w.jpg?ava=1').read()
#
# f = open('p.jpg','wb')
# f.write(resp)
# f.close()


# site= "http://en.wikipedia.org/wiki/StackOverflow"
# hdr = {'User-Agent': 'Mozilla/5.0'}
# req = Request(site,headers=hdr)
# page = urlopen(req)
# soup = BeautifulSoup(page)
# print(soup)


# driver = webdriver.Chrome()
# driver.get('https://dostfilms.net/publ/boeviki/mstiteli-voyna-beskonechnosti-2018/18-1-0-6144')
# driver.find_element_by_class_name("play-button-shadow").send_keys(Keys.ENTER)
# url = 'https://edge21.streamguard.cc/sec/1542520917/33313333b07589b51dc2428d71b3bc383ba624db1357f327/ivs/d3/c3/e0c6604d7290/hls/tracks-3,5/segment'

