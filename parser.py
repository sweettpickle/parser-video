import urllib
import threading
from urllib import request

count = 10000

def process_1():
    url1 = 'https://vhbalancer01-a.akamaihd.net/ch/a038fbf0285b444e4a33625b5f568fef/96c78b8744a6292bd99a778bcaae4c12/480/'

    for i in range(1, count):
        try:
            resp = request.urlopen(url1 + str(i) + '.ts?sid=sid&host=vh-20').read()
            f = open('9. Растяжка на поперечный шпагат + прокачка и гибкость мышц спины.' + '.ts', 'ab')
            f.write(resp)
            f.close()
            print('complete1: ', i)
        except urllib.error.HTTPError:
            print('download1 is broken')
            break


def process_2():
    url2 = 'https://vhbalancer01-a.akamaihd.net/ch/f01e673eee9615b6efb959af547220ae/d88a557ce4e1c9a1a4e96e587780b8af/480/'

    for i in range(1, count):
        try:
            resp = request.urlopen(url2 + str(i) + '.ts?sid=sid&host=vh-20').read()
            f = open('10. Комбо-тренировка. Лазарова Аделина' + '.ts', 'ab')
            f.write(resp)
            f.close()
            print('complete2: ', i)
        except urllib.error.HTTPError:
            print('download2 is broken')
            break

# def process_1():
#     url1 = 'https://vhbalancer01-a.akamaihd.net/ch/d071bcec02ab8c93b3ce8e538614f850/743cc91c4344d43b7636bc45079af45a/360/'
#
#     for i in range(1, count):
#         try:
#             resp = request.urlopen(url1 + str(i) + '.ts?sid=sid&host=vh-20').read()
#             f = open('7. Тренировка. Краснова Мария.' + '.ts', 'ab')
#             f.write(resp)
#             f.close()
#             print('complete1: ', i)
#         except urllib.error.HTTPError:
#             print('download1 is broken')
#             break
#
#
# def process_2():
#     url2 = 'https://vhbalancer01-a.akamaihd.net/ch/d35f802e0ad6b3123fcd6f35fc28df49/54d5abc4f7e4cc81cd86657f493b153f/480/'
#
#     for i in range(1, count):
#         try:
#             resp = request.urlopen(url2 + str(i) + '.ts?sid=sid&host=vh-20').read()
#             f = open('8. Low body - круговая, силовая, функциональная тренировка, статика.' + '.ts', 'ab')
#             f.write(resp)
#             f.close()
#             print('complete2: ', i)
#         except urllib.error.HTTPError:
#             print('download2 is broken')
#             break



pr1 = threading.Thread(target=process_1, name='one')
pr2 = threading.Thread(target=process_2, name='two')

pr1.start()
pr2.start()

