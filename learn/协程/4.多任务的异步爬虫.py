import requests
import asyncio
import time

import aiohttp

async  def get_request(url):
    print('正在请求的URL：',url)
    # time.sleep(2)
    # res = requests.get(url).text
    async with aiohttp.ClientSession() as sess:
        async with await sess.get(url) as response:
            page_text = await response.text()
            return page_text

def task_callback(t):
    print('i ama the task_callback ',t)
    print(t.result())

urls=[
    'http://127.0.0.1:5000/ltg00',
    'http://127.0.0.1:5000/ltg01',
    'http://127.0.0.1:5000/ltg02'
]
if __name__ == '__main__':
    time1 = time.time()
    # tasks=[(asyncio.ensure_future(get_request(url))).add_done_callback(task_callback) for url in urls]
    tasks = []
    for url in urls:
        c = get_request(url)
        task = asyncio.ensure_future(c)
        task.add_done_callback(task_callback)
        tasks.append(task)


    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
    print('总时长：',time.time()-time1)




