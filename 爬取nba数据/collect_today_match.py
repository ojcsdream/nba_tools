# 获取当天的比赛信息
# 获取比赛内容，数据，各个球员的得分
# url: https://nba.hupu.com/games
import requests
from lxml import etree
import xlwt
import datetime

def shoot(list, head):
    """拿到数据"""
    for url in list:
        response = requests.get(url, head)
        tree = etree.HTML(response.text)
        name = tree.xpath('/html/body/div[3]/div[4]/div[1]/div[2]/table/tbody/tr/td[1]/a/text()')[:5]
        print(name)
        part = tree.xpath('/html/body/div[3]/div[4]/div[1]/div[2]/table/tbody/tr/td[2]/text()')[:5]
        print(part)
        time = tree.xpath('/html/body/div[3]/div[4]/div[1]/div[2]/table/tbody/tr/td[3]/text()')[1:6]
        print(time)
        shoot = tree.xpath('/html/body/div[3]/div[4]/div[1]/div[2]/table/tbody/tr/td[4]/text()')[1:6]
        print(shoot)
        three_point = tree.xpath('/html/body/div[3]/div[4]/div[1]/div[2]/table/tbody/tr/td[5]/text()')[1:6]
        print(three_point)
        fa_qiu = tree.xpath('/html/body/div[3]/div[4]/div[1]/div[2]/table/tbody/tr/td[6]/text()')[1:6]
        print(fa_qiu)
        fangui = tree.xpath('/html/body/div[3]/div[4]/div[1]/div[2]/table/tbody/tr/td[11]/text()')[1:6]
        print(fangui)
        qiangduan = tree.xpath('/html/body/div[3]/div[4]/div[1]/div[2]/table/tbody/tr/td[12]/text()')[1:6]
        print(qiangduan)
        shiwu = tree.xpath('/html/body/div[3]/div[4]/div[1]/div[2]/table/tbody/tr/td[13]/text()')[1:6]
        print(shiwu)
        fenggai = tree.xpath('/html/body/div[3]/div[4]/div[1]/div[2]/table/tbody/tr/td[14]/text()')[1:6]
        print(fenggai)
        break




def get_into_url(url, headers):
    """拿到第一层网址"""
    response = requests.get(url, headers)
    # print(response.text)
    tree = etree.HTML(response.text)
    into_url_list = tree.xpath('/html/body/div[3]/div[4]/div[1]/div/div/div[2]/a[1]/@href')
    shoot(into_url_list, headers)



def main():
    url = 'https://nba.hupu.com/games'
    head = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36'
    }

    time = datetime.date.today()
    get_into_url(url, head)


if __name__ == '__main__':
    main()
