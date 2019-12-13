import urllib
from urllib import request
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import requests

count = 10000
url = 'https://vhbalancer01-a.akamaihd.net/ch/8b6a336d5bcc021d895831905f00383e/25b6beb0b00db4b891cb991339fc5f2e/360/'

for i in range(1, count):
    try:
        resp = request.urlopen(url + str(i) + '.ts?sid=sid&host=vh-20').read()

        f = open('2. Растяжка на продольные шпагаты + прокачка и гибкость мышц спины.' + '.ts', 'ab')
        f.write(resp)
        f.close()
        print('complete: ', i)
    except urllib.error.HTTPError:
        print('download is broken')
        break

