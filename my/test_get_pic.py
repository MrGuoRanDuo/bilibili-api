# -*- coding:utf-8 -*-
import asyncio
import random
from urllib import request
import logging
import time

import requests
from PIL import Image

from bilibili_api.exceptions import ResponseCodeException

from bilibili_api.comment import send_comment, ResourceType

from bilibili_api import user, comment, video, Credential, sync

# settings.proxy = "http://127.0.0.1:10808"

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

# 短网址转换账户授权key   https://www.ft12.com/
APP_KEY = ""

SESSDATA = ""
BILI_JCT = ""
BUID = ""

# 自己的小号
# SESSDATA2 = ""
# BILI_JCT2 = ""
# BUID2 = ""

# JSS
SESSDATA_JSS = ""
BILI_JCT_JSS = ""
BUID_JSS = ""

# BLHX1
SESSDATA_BLHX1 = ""
BILI_JCT_BLHX1 = ""
BUID_BLHX1 = ""

# Ma
SESSDATA_MA = ""
BILI_JCT_MA = ""
BUID_MA = ""

# Ba
SESSDATA_Ba = ""
BILI_JCT_Ba = ""
BUID_Ba = ""

# LFQ
SESSDATA_LFQ = ""
BILI_JCT_LFQ = ""
BUID_LFQ = ""

MY_UID = 5919684
HXD_UID = 598012701

# 100W粉以上
YAO_REN = 116683
# todo
# XM_UID = 8366990
WU_XIAO_MIAO_UID = 2223018
YA_YA_UID = 632887
XIAO_YU_YU_UID = 17437888
XIAO_XIAN_RUO_UID = 16539048
TU_ZONG_CAI_UID = 15385187
PAO_FU_MIAO_UID = 1526101
XIAO_YU_DD = 378987060
TUO_QI = 7375428
LEVEL1_LIST = [YAO_REN, WU_XIAO_MIAO_UID, YA_YA_UID, XIAO_YU_YU_UID, XIAO_XIAN_RUO_UID, TU_ZONG_CAI_UID,
               PAO_FU_MIAO_UID, XIAO_YU_DD, TUO_QI]
# 50w粉以上
KYOKYO_UID = 475250
XIAO_WU_JIANG_UID = 2691287
MEI_KE_UID = 5028996
SI_XIAO_MIAO_UID = 2009929
QING_YUAN_CYAN_UID = 11605312
KAI_MEN_LA_XIAO_CHU_UID = 5276
ZHOU_MUO_YUUKO_UID = 492393
XIAO_MI_ZHOU_UID = 10893225
XIAO_DAN_XIAO_XIAN_UID = 21648772
YANG_XIAO_XUE_UID = 23400436
YI_ZHI_XIAO_DUAN_DUAN_UID = 10139490
ZI_YAN = 35579222
A_DAI = 49676
FU_PO = 397044296
YUE_LOU = 481450341
LULU = 622863  # BV1df4y1T7Pg
XIAO_LU = 94508008  # BV12F411b7Ts
GENG_GENG = 26328593  # BV1xZ4y197ss
GUO_NONG = 900171  # BV1cq4y1m7n9
SHIYUAN = 20067185  # BV1eh411x7k4
XUE_ROU = 262888220  # BV1Db4y1i78f
MY_MY = 848008  # BV1uP4y1N7U3
YU_YUAN = 1323218982  # BV1xS4y1G7Sf
MU_MU = 533996453  # BV1644y1J7pU
LEVEL2_LIST = [KYOKYO_UID, XIAO_WU_JIANG_UID, SI_XIAO_MIAO_UID, QING_YUAN_CYAN_UID, KAI_MEN_LA_XIAO_CHU_UID,
               ZHOU_MUO_YUUKO_UID, XIAO_MI_ZHOU_UID, XIAO_DAN_XIAO_XIAN_UID, YANG_XIAO_XUE_UID,
               YI_ZHI_XIAO_DUAN_DUAN_UID, MEI_KE_UID, ZI_YAN,
               A_DAI, FU_PO, YUE_LOU, LULU, XIAO_LU, GENG_GENG, GUO_NONG, SHIYUAN, XUE_ROU, MY_MY, YU_YUAN, MU_MU]
# 10w粉以上
YE_YE_ZI_UID = 25135049
SENKO_UID = 385282068
YU_BAN_MAO_MAO_UID = 17328861
KE_YING_UID = 393342019
DU_BIAN_NA_YU_YU_UID = 18701109
YOU_RUI_KE_UID = 11542325
PAO_FU_JIANG_DAZE = 6799052
TING_SHU_MU_NIAN_UID = 382894360
XIA_SU_SU_UID = 4568488
MU_MU_YOU_NAI_TANG = 18841842
MENG_KE_YU = 4745412
BU_HUI_TIAO_WU_DE_MENG_XIAO_QIAO = 625115765
HEI_SI_KE_JI = 95205743
CHU_YUAN_YUAN_YA = 97094885
QI_QI = 1851105
MENG_AI = 1600113
LA_ZI_JIANG = 9459684
XIA_SU_SU = 4568488
BAI_JIN_SAKI = 1575476
XI_HAI_AN_HONG_SHAN = 8066835
YANG = 7370915  # BV1qS4y197s8
QING_MU_WEI = 430136831  # BV1vv411r72P
QING_DOU_JIANG = 27441982  # BV1ER4y147gx
WO_WO_TOU = 5462540  # BV1mk4y127qD
TANG_XIN = 431376375  # BV1Uq4y1y74J
LAO_MO_XIAN_UID = 15252807
ZONG_ZI_SONG = 31968078
YE_MIAO_W = 8315451  # BV1YL411j7DF
QIAN_NING = 17783613  # BV1hR4y1L7Bz
JI_TU_HUI = 1845381
LEVEL3_LIST = [YE_YE_ZI_UID, SENKO_UID, YU_BAN_MAO_MAO_UID, KE_YING_UID, DU_BIAN_NA_YU_YU_UID, YOU_RUI_KE_UID,
               PAO_FU_JIANG_DAZE,
               TING_SHU_MU_NIAN_UID, XIA_SU_SU_UID, MU_MU_YOU_NAI_TANG, MENG_KE_YU, BU_HUI_TIAO_WU_DE_MENG_XIAO_QIAO,
               HEI_SI_KE_JI, CHU_YUAN_YUAN_YA,
               QI_QI, MENG_AI, LA_ZI_JIANG, XIA_SU_SU, BAI_JIN_SAKI, XI_HAI_AN_HONG_SHAN, QING_MU_WEI, YANG,
               QING_DOU_JIANG, WO_WO_TOU, TANG_XIN, LAO_MO_XIAN_UID, ZONG_ZI_SONG, YE_MIAO_W, QIAN_NING, JI_TU_HUI]
# 潜力股
# 遗憾未达标分    辨率
JIANG_QI_QI_UID = 3403527
AI_UID = 1678535
# 年更
NI_DE_TU_MEI_NEI_UID = 111522114
LEVEL1_LIST.extend(LEVEL2_LIST)
LEVEL1_LIST.extend(LEVEL3_LIST)

LIST_TARGET_MM_UID = LEVEL1_LIST

time_sleep = 0


async def download(UID):
    credential = Credential(sessdata=SESSDATA, bili_jct=BILI_JCT, buvid3=BUID)

    u = user.User(uid=UID, credential=credential)
    global time_sleep
    time_sleep += random.uniform(3.5, 6.5)
    await asyncio.sleep(time_sleep)
    count = 1
    while 1:
        v_info = await u.get_videos(pn=count)

        count += 1


async def tools(UID):
    credential = Credential(sessdata=SESSDATA, bili_jct=BILI_JCT, buvid3=BUID)

    u = user.User(uid=UID, credential=credential)

    global time_sleep
    time_sleep += random.uniform(3.5, 6.5)
    await asyncio.sleep(time_sleep)

    v_info = await u.get_videos()
    temp_video_num = v_info['page']['count']
    log.info(str(time.ctime()) + "|  INFO  |" + "获取初始视频信息: " + str(v_info['list']['vlist'][0]['author']) + " | " + str(
        v_info['list']['vlist'][0]['bvid']))
    # if str(v_info['list']['vlist'][0]['author']) == "BML制作指挥部":
    #     print("BML制作指挥部")
    # log.info("防止爬取过快 B站封禁"+str(UID)+" "+str(time.ctime()))
    # 防止爬取过快 B站封禁
    await asyncio.sleep(time_sleep)
    while True:
        v_info_new = await u.get_videos()

        if temp_video_num < v_info_new['page']['count']:
            # 更新用户对象
            temp_video_num = v_info_new['page']['count']
            v_info = v_info_new

            TARGET_oAID = v_info_new['list']['vlist'][0]['aid']
            BV_ID = v_info_new['list']['vlist'][0]['bvid']
            # 异步等待同步
            await asyncio.sleep(time_sleep)
            log.info(str(time.ctime()) + "|  INFO  |" + "开始视频回复 " + str(BV_ID) + "  " + str(
                v_info_new['list']['vlist'][0]['author']))
            pic_url = v_info_new['list']['vlist'][0]['pic']
            resp = request.urlopen(pic_url)
            img = Image.open(resp)
            x, y = img.size
            if x >= 1920 or y >= 1080:
                # 文件操作
                file_handle = open('../print.txt', mode='a')
                log.info(str(time.ctime()) + "|  INFO  |" + "开始保存到文件")
                file_handle.writelines(
                    str(v_info_new['list']['vlist'][0]['author']) + "  " + str(BV_ID) + "  " + pic_url + '\n')
                file_handle.close()

                # # 保存为图片
                # try:
                #     r = requests.get(pic_url)
                #     image = r.content
                #     with open(str(BV_ID)+".jpg", "wb") as f:
                #         f.write(image)
                # except Exception:
                #     pass

                comment_list = ["我又来了【侵删】(分辨率", "【侵删】封面区UP来了(分辨率", "封面区UP来了(侵删)(拿走了就点个赞吧)[吃瓜](分辨率"]
                # 短链接转换
                # url = "http://api.ft12.com/api.php?url=" + pic_url + "&apikey=18655471098@2a52746de4773e30571645d5c8f7f1b7"
                # res = ""
                # while 1:
                #     try:
                #         res = requests.get(url)
                #         break
                #     except:
                #         continue
                # + str(res.text) + '\n'
                comment_result = await send_comment(
                    text=comment_list[random.randint(0, 2)] + str(x) + "x" + str(y) + ")         \n" + '近日b站屏蔽封面链接 封面移步我的专栏' + '\n                  --随机小尾巴' + str(time.time()),
                    oid=TARGET_oAID, type_=comment.ResourceType.VIDEO,
                    credential=credential)
                log.info("|   INFO   |" + "回复状态:" + comment_result['success_toast'])
                await asyncio.sleep(time_sleep + random.randint(2, 5))
                # 刷赞相关
                await asyncio.sleep(10)
                comment_id = comment_result["rpid"]
                if comment_id == "" or comment_id is None or comment_id is False:
                    log.info("|ERROR| 评论发送失败")
                credential2 = Credential(sessdata=SESSDATA_LFQ, bili_jct=BILI_JCT_LFQ, buvid3=BUID_LFQ)
                cmt = comment.Comment(oid=TARGET_oAID, type_=comment.ResourceType.VIDEO, rpid=comment_id,
                                      credential=credential2)
                try:
                    await cmt.like()
                    log.info(str(time.ctime()) + "|  INFO  |" + "点赞成功_LFQ")
                except ResponseCodeException:
                    log.info("|ERROR| 账号未登录FX")
                # {'suc_pic': '', 'suc_toast': ''}

                await asyncio.sleep(15)
                credential_blhx = Credential(sessdata=SESSDATA_BLHX1, bili_jct=BILI_JCT_BLHX1, buvid3=BUID_BLHX1)
                cmt = comment.Comment(oid=TARGET_oAID, type_=comment.ResourceType.VIDEO, rpid=comment_id,
                                      credential=credential_blhx)
                try:
                    await cmt.like()
                    log.info(str(time.ctime()) + "|  INFO  |" + "点赞成功_BLHX1")
                except ResponseCodeException:
                    log.info("|ERROR| 账号未登录BLHX1")

                await asyncio.sleep(20)
                credential_jss = Credential(sessdata=SESSDATA_JSS, bili_jct=BILI_JCT_JSS, buvid3=BUID_JSS)
                cmt = comment.Comment(oid=TARGET_oAID, type_=comment.ResourceType.VIDEO, rpid=comment_id,
                                      credential=credential_jss)
                try:
                    await cmt.like()
                    log.info(str(time.ctime()) + "|  INFO  |" + "点赞成功_JSS")
                except ResponseCodeException:
                    log.info("|ERROR| 账号未登录jss")

                await asyncio.sleep(25)
                cmt = comment.Comment(oid=TARGET_oAID, type_=comment.ResourceType.VIDEO, rpid=comment_id,
                                      credential=credential)
                try:
                    await cmt.like()
                    log.info(str(time.ctime()) + "|  INFO  |" + "点赞成功_自己")
                except ResponseCodeException:
                    log.info("|ERROR| 账号未登录自己")

                await asyncio.sleep(30)
                credential_ma = Credential(sessdata=SESSDATA_MA, bili_jct=BILI_JCT_MA, buvid3=BUID_MA)
                cmt = comment.Comment(oid=TARGET_oAID, type_=comment.ResourceType.VIDEO, rpid=comment_id,
                                      credential=credential_ma)
                try:
                    await cmt.like()
                    log.info(str(time.ctime()) + "|  INFO  |" + "点赞成功_M")
                except ResponseCodeException:
                    log.info("|ERROR| 账号未登录MA")

                await asyncio.sleep(35)
                credential_ba = Credential(sessdata=SESSDATA_Ba, bili_jct=BILI_JCT_Ba, buvid3=BUID_Ba)
                cmt = comment.Comment(oid=TARGET_oAID, type_=comment.ResourceType.VIDEO, rpid=comment_id,
                                      credential=credential_ba)
                try:
                    await cmt.like()
                    log.info(str(time.ctime()) + "|  INFO  |" + "点赞成功_B")
                except ResponseCodeException:
                    log.info("|ERROR| 账号未登录Ba")

            else:
                log.info(str(time.ctime()) + "|  WARNING  |" + "图片分辨率不达标" + "x=" + str(x) + ",y=" + str(y))
        else:
            log.info(str(time.ctime()) + "|  INFO  |""开始下一次循环 " + str(
                v_info_new['list']['vlist'][0]['author']) + "|  " + str(v_info_new['list']['vlist'][0]['mid']))
        await asyncio.sleep(time_sleep)


if __name__ == '__main__':
    log.info(time.ctime())
    loop = asyncio.get_event_loop()
    tasks = [tools(UID) for UID in LIST_TARGET_MM_UID]
    # tasks = [tools(UID) for UID in ["5919684"]]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
