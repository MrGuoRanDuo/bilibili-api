# 保存为图片
# -*- coding:utf-8 -*-
import asyncio
import random
from typing import List
from urllib import request
import logging
import time

from PIL import Image
from pip._vendor import requests

from bilibili_api.comment import send_comment, ResourceType

from bilibili_api import user, comment, video, Credential, sync
from bilibili_api import settings
import re
import time
from urllib import request
import requests
from PIL import Image

from my.test_get_pic import SESSDATA, BILI_JCT, BUID

time_sleep = 0
LIST_TARGET_MM_UID = [16539048]
name = "一只小仙若"
List_pic: List[str] = []

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)


def pic_download_manuly():
    f = open("1016.txt", encoding='UTF-8')  # 返回一个文件对象
    line = f.readline()  # 调用文件的 readline()方法
    while line:
        print(line, end='')  # 后面跟 ',' 将忽略换行符
        # '早上好七七  BV1Mv411G7a9  http://i2.hdslb.com/bfs/archive/6aec4407b00850dd0e8b3eabde32cef473006923.jpg\n
        line = f.readline()
        name = line.split("BV")[0].split(" ")[0]
        try:
            pic_url = re.findall(r'http.*', line)[0].split('\n')[0]
        except IndexError:
            break
        BV_ID = re.findall(r'BV.*', line)[0].split(' ')[0]

        resp = request.urlopen(pic_url)
        img = Image.open(resp)
        x, y = img.size
        print(x, y)
        k_name = ""
        if 2560 > x >= 1920 or 1440 > y >= 1080:
            k_name = "1k"
        elif 4096 > x >= 2560 or 2160 > y >= 1440:
            k_name = "2k"
        elif x >= 4096 or y >= 2160:
            k_name = "4k"
        elif x >= 5120 or y >= 2880:
            k_name = "5k"
        elif x >= 6144 or y >= 3160:
            k_name = "6k"
        elif x >= 7680 or y >= 4320:
            k_name = "8k"

        r = requests.get(pic_url)
        image = r.content
        with open(k_name + "_" + str(BV_ID) + "_" + name + ".jpg", "wb") as pf:
            pf.write(image)

        time.sleep(10)
    f.close()


async def download(UID):
    credential = Credential(sessdata=SESSDATA, bili_jct=BILI_JCT, buvid3=BUID)

    u = user.User(uid=UID, credential=credential)
    global time_sleep
    time_sleep += random.uniform(3.5, 6.5)
    await asyncio.sleep(time_sleep)
    count = 1
    while 1:
        v_info = await u.get_videos(pn=count)
        v_list = v_info['list']['vlist']
        for v in v_list:
            url = v['pic']
            bvid = v['bvid']
            download_tools(_name=name, _pic_url=url, _bvid=bvid)
            await asyncio.sleep(2)
        count += 1


def download_tools(_name: str, _pic_url: str, _bvid:str):
    _resp = request.urlopen(_pic_url)
    _img = Image.open(_resp)
    _x, _y = _img.size
    print(_x, _y)
    if _x < 1920 or _y < 1080:
        return
    _k_name = ""
    if 2560 > _x >= 1920 or 1440 > _y >= 1080:
        _k_name = "1k"
    elif 4096 > _x >= 2560 or 2160 > _y >= 1440:
        _k_name = "2k"
    elif _x >= 4096 or _y >= 2160:
        _k_name = "4k"
    elif _x >= 5120 or _y >= 2880:
        _k_name = "5k"
    elif _x >= 6144 or _y >= 3160:
        _k_name = "6k"
    elif _x >= 7680 or _y >= 4320:
        _k_name = "8k"

    _r = requests.get(_pic_url)
    _image = _r.content
    with open(_k_name + "_" + str(_bvid) + "_" + _name + ".jpg", "wb") as _pf:
        _pf.write(_image)

    time.sleep(5)


if __name__ == '__main__':
    # log.info(time.ctime())
    # loop = asyncio.get_event_loop()
    # tasks = [download(UID) for UID in LIST_TARGET_MM_UID]
    # # tasks = [tools(UID) for UID in [HXD_UID, MY_UID]]
    # loop.run_until_complete(asyncio.wait(tasks))
    # loop.close()

    pic_download_manuly()
