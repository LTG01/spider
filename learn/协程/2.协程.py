import requests
import asyncio
import time

async  def get_request(url):
    print('正在请求的URL：',url)
    time.sleep(2)
    print('请求结束')
    return 'nb'

def task_callback(t):
    print('i ama the task_callback ',t)
    print(t.result())
if __name__ == '__main__':

   c = get_request('http://www.baidu.com')
   print(c)

   task = asyncio.ensure_future(c)
   task.add_done_callback(task_callback)

   loop = asyncio.get_event_loop()
   loop.run_until_complete(task)





