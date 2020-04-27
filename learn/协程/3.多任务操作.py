import requests
import asyncio
import time

import aiohttp

async  def get_request(url):
    print('正在请求的URL：',url)
    # time.sleep(2)
    await  asyncio.sleep(2)
    print('请求结束')
    return 'nb'

def task_callback(t):
    print('i ama the task_callback ',t)
    print(t.result())

urls=[
    'www.1.com',
    'www.2.com',
    'www.3.com'

]
if __name__ == '__main__':
    time1 = time.time()
    tasks=[asyncio.ensure_future(get_request(url)) for url in urls]

    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
    print('总时长：',time.time()-time1)




