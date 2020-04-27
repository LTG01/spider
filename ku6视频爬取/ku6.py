#有点偷懒变量名用简单字母啦.............
# https://www.ku6.com/index
# <a class="video-image-warp" target="_blank" href="(.*?)">
#this.src({type: "video/mp4", src: "(.*?)"})
#src({type: "video/mp4", src: "(.*?)"})
import re  # 载入模块
import requests  # 载入模块
new_list = []
time = 0
response = requests.get('https://www.ku6.com/index')
data = response.text
print(data)
url = re.findall('<a class="video-image-warp" target="_blank" href="(.*?)">',data)
for a in url : #type:str
    if a.startswith('/v') or a.startswith('/d'):
        new_list.append(f'https://www.ku6.com{a}')
    elif a.startswith('http'):
        new_list.append(f"{a.split('垃')[0]}")

print(new_list)
for url_1 in new_list:
    response_1 = requests.get(url_1)
    data_1 = response_1.text
    video = re.findall('<source src="(.*?)" type="video/mp4">',data_1) or re.findall('type: "video/mp4", src: "(.*?)"',data_1)
    print(video)
    video_1 = video[0]
    x = video_1.split('/')[-1]
    name = f'{x}.mp4'
    video_response = requests.get(video_1)
    video_3 = video_response.content
    with open(f'D:\图片\{name}','wb') as fw:
        fw.write(video_3)
        fw.flush()
        time += 1
        print(f'已经爬取{time}个视频')