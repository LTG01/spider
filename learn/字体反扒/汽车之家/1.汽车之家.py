import requests
from lxml import etree
from fontTools.ttLib import TTFont
import pytesseract
import re

from PIL import Image, ImageFont, ImageDraw
import numpy
#========================================获取汽车之家网页信息===========================================================

def get_html(url,headers):

    response=requests.get(url,headers=headers)
    response.encoding='gb2312'
    html=response.text

    with open('替换之前.html','w',encoding='utf-8') as f:
        f.write(html)

    return html


def get_ttf(html):
    '''

    根据网页内容获取 ttf 网址，并请求数据
        <style type="text/css">
        @font-face {font-family: 'myfont';src: url('//k2.autoimg.cn/g1/M00/D0/9F/wKgHFVsUz3CAAb2-AABktvoC5wc65..eot');src: url('//k3.autoimg.cn/g1/M00/D0/9F/wKgHFVsUz3CAAb2-AABktvoC5wc65..eot?#iefix') format('embedded-opentype'),url('//k3.autoimg.cn/g1/M04/D0/9F/wKgHFVsUz3CAcskWAABj8IaKtck92..ttf') format('woff');}
    </style>
    :return:
    '''
    pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

    #提取路径
    ttf_url ="http:"+ re.findall("format\('embedded-opentype'\),url\('(.*?)'\) format\('woff'\);",html)[0]

    print(ttf_url)
    name = ttf_url.split('/')[-1]
    print(name)

    #获取内容
    ttf_cont = requests.get(ttf_url).content
    with open(name,'wb')as f:
        f.write(ttf_cont)

    font = TTFont(name)
    font.saveXML('1.xml')

    # 获取字体编码（特殊的编码）
    code_list = font.getGlyphOrder()[1:]
    print(code_list)

    """逆向部分,将特殊字体绘制到一张图片上去"""
    # 新建一张图片
    im = Image.new("RGB", (1400, 280), (255, 255, 255))
    # 绘制图片的对象
    image_draw = ImageDraw.Draw(im)
    # 绘制图片中, 显示的字体
    font = ImageFont.truetype(name, 40)

    count = 2
    # 将特殊编码等分为15分
    array_list = numpy.array_split(code_list, count)

    for i in range(len(array_list)):
        print('替换之前的', array_list[i])
        # 将js的unicode码转化为python的unicode
        new_list = [i.replace("uni", "\\u") for i in array_list[i]]
        print('替换之后的', new_list)

        # 将列表变为字符串
        text = "".join(new_list)
        print('列表变字符串', text)
        # text = text.encode('utf-8').decode('utf-8')
        # print(text)
        # encode decode
        # 把文字变成二进制
        # 将字符串进行反向编码
        text = text.encode('utf-8').decode('unicode_escape')
        print('反向编码之后的', text)
        # 将文件绘制到图片
        # 指定字体进行绘制
        image_draw.text((0, 100 * i), text, font=font, fill="#000000")

    im.save("sss.jpg")  # 可以将图片保存到本地，以便于手动打开图片查看
    im.show()

    # tessdata_dir_config = '--tessdata-dir "C:\\Program Files\\Tesseract-OCR"'
    # tessdata_dir_config = '--tessdata-dir "C:\\Program Files (x86)\\Tesseract-OCR\\tessdata"'
    # result = pytesseract.image_to_string(im, config=tessdata_dir_config)

    result = pytesseract.image_to_string(im, lang="chi_sim")
    print(result)
    # # 去除空白及换行
    result_str = result.replace(" ", "").replace("\n", "")
    # 将内容替换成网页的格式，准备去网页中进行替换
    print(code_list)
    html_code_list = [i.replace("uni", "&#x") + ";" for i in code_list]
    print(html_code_list)
    map_dict = dict(zip(html_code_list, list(result_str)))
    print(map_dict)

    with open('替换之前.html', mode='r', encoding='utf-8') as f:
        text = f.read()

    for key, value in map_dict.items():

        key = "<span style='font-family: myfont;'>"+key.lower()+"</span>"
        print(key, value)
        text = text.replace(key, value,)

    with open('替换之后.html', mode='w', encoding='utf-8') as f:
        f.write(text)


#手动确定文字和字符的编码对应关系

u_list=['uniEDED','uniED39','uniEC86','uniECD8','uniEC24','uniED65','uniEDB7','uniED03','uniED55','uniECA2',
           'uniEDE2','uniEC40','uniED81','uniECCD','uniED1F','uniEC6C','uniECBD','uniEDFE','uniED4B','uniED9C','uniECE9'
           ,'uniEC36','uniEC87','uniEDC8','uniEC26','uniED66','uniECB3','uniED05','uniEC51','uniED92','uniEDE4'
            ,'uniED30','uniED82','uniECCF','uniEC1B','uniEC6D','uniEDAE','uniECFA']
word_list=['三','七','多','的','近','上','大','是','呢','更','着','矮','八','坏','五','四','十','小','地','高','和'
           ,'远','得','九','很','低','长','右','少','了','好','六','短','一','左','二','下','不']




def read(name):
    text=''
    with open(name,'r',encoding='utf-8') as f:
        text = f.read()
    return text

def write(name,content):
    text=''
    with open(name,'w',encoding='utf-8') as f:
        f.write(content)

if __name__=="__main__":
    url = 'https://club.autohome.com.cn/bbs/thread/44f8a42ea48b2c92/87283958-1.html'

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"
    }

    html = get_html(url,headers)
    name = '替换之前.html'
    # html = read(name)
    get_ttf(html)

    pass
