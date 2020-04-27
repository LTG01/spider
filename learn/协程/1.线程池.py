
import requests
import time

def get_request(url):
    page_text = requests.get(url).text
    return len(page_text)

urls=[
        'http://127.0.0.1:5000/ltg00',
        'http://127.0.0.1:5000/ltg01',
        'http://127.0.0.1:5000/ltg02'
    ]
#同步代码
# if __name__ == '__main__':
#     time1= time.time()

#     res=[print(get_request(url)) for url in urls ]
#     print('时长：',time.time()-time1)



from multiprocessing.dummy import Pool
#异步代码

if __name__ == '__main__':
    time1 = time.time()
    pool = Pool(3)
    res = pool.map(get_request,urls)
    print(res)
    print('时长：', time.time() - time1)
    pass