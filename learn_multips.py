import time
import requests
from multiprocessing.dummy import Pool

def calc_power2(num):
    return  num*num

def calc_pool():
    pool=Pool(3)
    origin_num=[x for x in range(10)]
    result=pool.map(calc_power2,origin_num)
    print(f'计算0-9的平方分别为：{result}')

def query(url):
    requests.get(url)

def test_single_query():
    start=time.time()
    for i in range(100):
        query('https://www.baidu.com/')
    end=time.time()
    print('单次循环100次花费时间：',(end-start))

def test_multi_query():
    pool=Pool(5)
    url_list=[]
    start=time.time()
    for i in range(100):
       url_list.append('https://www.baidu.com/')
    pool.map(query,url_list)
    end=time.time()
    print('多线程循环100次花费时间：',(end-start))

if __name__ == '__main__':
    # calc_pool()
    test_single_query()
    test_multi_query()