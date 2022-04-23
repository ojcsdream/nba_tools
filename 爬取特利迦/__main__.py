import time
import requests
from bs4 import BeautifulSoup
import re
import random
import asyncio
import aiohttp, aiofiles
import m3u8
import os



def get_data(url, head):
    time.sleep(random.randint(1, 3))  # 随机休眠，避免反爬
    response = requests.get(url , head)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'html.parser')
    flag = soup.find("div", class_="movurl")
    little_url = re.findall(r'<li><a href="(.*?)"',str(flag))
    url_list = []
    for i in little_url:
        full_url = f"http://www.yinghuacd.com/{i}"
        url_list.append(full_url)
    return url_list  # 拿到每一集的在线视频地址


def get_m3u8(url_list, head):
    """拿到每一集的m3u8文件"""
    list = []
    for i in url_list:
        response = requests.get(i, head)
        response.encoding = 'utf-8'
        m3u8_url = re.findall(r'<div data-vid="(.*?)\$mp4"', response.text)[0] # 利用正则表达式匹配m3u8地址
        list.append(m3u8_url)
    return list



def download_first_m3u8(lujing, m3u8_list):
    """下载m3u8文件"""
    clock = 0
    for i in m3u8_list:
        print(f"第{clock}个")
        response = requests.get(i).content
        with open(f"{lujing}第{clock}集.m3u8", 'wb') as f:
            f.write(response)

        clock += 1


def sovle_second_m3u8():
    """解析第二层m3u8,并拿到真实的m3u8的链接"""
    full_m3u8_list = []
    for i in range(1, 27):  # 依次打开m3u8文件
        with open(f'D:/m3u8/{i}_m3u8.txt', 'r') as f:
            for line in f:    # 如果以#号开头跳过
                if line.startswith("#"):
                    continue
                else:   # 提取子链接
                    line = line.split()[0]
                    full_m3u8 = 'https://new.iskcd.com'+line
                    full_m3u8_list.append(full_m3u8)
    return full_m3u8_list  # 返回真实的m3u8的链接列表

async def aio_download(url, name):
    """利用异步下载"""
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            async with aiofiles.open(f'D:/video/{name}.ts', 'wb') as f:
                await f.write(await response.content.read())


async def download_m3u8_main(url_list):
    """利用完整的m3u8链接，下载视频"""
    a = 1
    for i in url_list:
        task = []
        item = m3u8.load(i)
        for index, segment in enumerate(item.segments):  # 拿到m3u8里的ts文件链接
            url = segment.uri
            print(url)
            print(f"正在下载第{a}个")
            task.append(asyncio.create_task(aio_download(url, a))) # 创建协程任务

            a += 1

        await asyncio.wait(task)










if __name__ == '__main__':
    url = 'http://www.yinghuacd.com/show/5323.html'

    head = {'User-Agent' :
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36'
            }
    #
    # url_list = get_data(url, head)
    # m3u8_list = get_m3u8(url_list, head)
    # # print(m3u8_list)
    # download_first_m3u8('D:/m3u8/', m3u8_list)
    full_m3u8_list = sovle_second_m3u8()
    download_first_m3u8('E:/特利迦奥特曼/', full_m3u8_list)

    # print(full_m3u8_list)
    # asyncio.run(download_m3u8_main((full_m3u8_list)))