




import requests
import json
import time
import pprint
import os
import pyecharts.options as opts
from pyecharts.charts import Line
import sys
# sys.setrecursionlimit(1000000)
import collections
from enum import Enum

import math
class Sort(Enum):

    SYL_1N = 'SYL_1N' # 近一年,
    SYL_2N = 'SYL_2N' # 近2年,
    SYL_3N = 'SYL_3N' # 近3年,
    SYL_3Y = 'SYL_3Y' # 近3月,
    SYL_6Y = 'SYL_6Y' # 近6月,
    SYL_JN = 'SYL_JN'# 今年来,
    SYL_Y = 'SYL_Y' # 近1月,
    SYL_Z = 'SYL_Z' # 近1周,




def getTopicFundData(tp='0118120006524473',sort=Sort.SYL_1N.value,sorttype=-1,pageindex=1,pagesize=10,**kwargs):
    '''

     :param tp:  主题编号
    :param sort:
            'SYL_1N': 近一年,
            'SYL_2N': 近2年,
            'SYL_3N': 近3年,
            'SYL_3Y': 近3月,
            'SYL_6Y': 近6月,
            'SYL_JN': 今年来,
            'SYL_Y': 近1月,
            'SYL_Z': 近1周,
    :param sorttype:
                'desc'：降序，  -1
                'aesc': 升序   1
    :param pageindex: 页码

    :param pagesize: 每页条数
    :param kwargs:
    :return:
    '''

    if not tp:
        return -1,[]
    if sorttype>0:
        sorttype = 'aesc'
    else:
         sorttype = 'desc'
    getAll = False
    if pageindex == 0:
         pageindex = 1
         pagesize  =1
         getAll = True

    params={
        'callbackname':kwargs.get('callbackname','topicFundData'),
        'sort' : sort,
        'sorttype' : sorttype,
        'pageindex' : pageindex,
        'pagesize' : pagesize,
        'tp' : tp,
        'dt' : kwargs.get('dt', '10')
    }
    url='''http://fund.eastmoney.com/api/FundTopicInterface.ashx'''
    res = requests.get(url=url,params=params)
    if res.status_code !=200:
        return -2,[]
    res1 = json.loads(res.text[18:])
    # pprint.pprint(res1)
    if not getAll:
        return 0, res1['Datas']
    #一次获取所有数据
    params['pagesize'] = res1['TotalCount']
    res = requests.get(url=url, params=params)
    if res.status_code != 200:
        return -2, []
    res1 = json.loads(res.text[18:])
    # pprint.pprint(res1)
    return 0, res1['Datas']

def getTopFundDataID():

    url = 'http://fund.eastmoney.com/api/fundtopicinterface.ashx?dt=13'

    res = requests.get(url)
    if res.status_code!=200:
        return {}
    else:
        # pprint.pprint(res.json())
        return res.json()['data']

def createHTML(items,nameType):
    month = int(time.strftime("%m", time.localtime()))
    if month >= 6:
        xaxisdata = ['近1周', '近1月', '近3月', '近6月', '今年来', '近1年', '近2年', '近3年']
    else:
        xaxisdata = ['近1周', '近1月', '近3月', '今年来', '近6月', '近1年', '近2年', '近3年']

    TTYPENAME = ''
    yaxisdata = ''
    # print('##'*100,len(items))
    for item in items:
        name = item['SHORTNAME']
        SYL_1N = item['SYL_1N']
        SYL_2N = item['SYL_2N']
        SYL_3N = item['SYL_3N']
        SYL_3Y = item['SYL_3Y']
        SYL_6Y = item['SYL_6Y']
        SYL_JN = item['SYL_JN']
        SYL_Y = item['SYL_Y']
        SYL_Z = item['SYL_Z']
        TTYPENAME = item['TTYPENAME']
        # y=[SYL_Z,SYL_Y,SYL_3Y,SYL_6Y,SYL_1N,SYL_2N,SYL_3N]
        if month >= 6:
            y = [SYL_Z, SYL_Y, SYL_3Y, SYL_6Y, SYL_JN, SYL_1N, SYL_2N, SYL_3N]
        else:
            y = [SYL_Z, SYL_Y, SYL_3Y, SYL_JN, SYL_6Y, SYL_1N, SYL_2N, SYL_3N]

        yaxisdata += '.add_yaxis("{}", {}, is_connect_nones=True)'.format(name, y)
    # print(yaxisdata)
    os.makedirs(nameType,exist_ok=True)
    try:
        cline = '''c = (Line().add_xaxis(xaxisdata){}.set_global_opts(title_opts=opts.TitleOpts(title="{}")).render("./{}/{}.html"))'''.format(
            yaxisdata, TTYPENAME,nameType, TTYPENAME)
        # print(cline)
        exec(cline)
    except Exception as e:
        print(str(e))

def sortData(data,sort):

    sortfun = lambda x: x[sort] if type(x[sort])==float else -100
    data = sorted(data, key=sortfun)

    return data



if __name__=='__main__':

    print(Sort.SYL_JN.value)
    res= getTopFundDataID()

    for key,hys in res.items():
        print(key,hys)

        # hys=res['hy']
        # for
        print(key,len(hys))
        for hy in hys:
            # t=time.time()
            err,items=getTopicFundData(tp=hy['TType'],pageindex=1,pagesize=30)
            # print(time.time()-t)

            # pprint.pprint(items)
            print(len(items),items)

            # item1 = sortData(items,Sort.SYL_Z.value)
            item2 = sortData(items, Sort.SYL_Y.value)
            item3 = sortData(items, Sort.SYL_3Y.value)
            item4 = sortData(items, Sort.SYL_6Y.value)



            createHTML(items,key)






