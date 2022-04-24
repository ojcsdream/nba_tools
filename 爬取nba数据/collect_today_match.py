# 获取当天的比赛信息
# 获取比赛内容，数据，各个球员的得分
# url: https://nba.hupu.com/games
import requests
from lxml import etree
import xlwt
import datetime


def get_first_group(url, headers):
    """拿第一队的首发数据"""
    response = requests.get(url, headers)
    tree = etree.HTML(response.text)
    name = tree.xpath('/html/body/div[3]/div[4]/div[1]/div[2]/table/tbody/tr/td[1]/a/text()')[:5]
    # print(name)
    part = tree.xpath('/html/body/div[3]/div[4]/div[1]/div[2]/table/tbody/tr/td[2]/text()')[:5]
    # print(part)
    time = tree.xpath('/html/body/div[3]/div[4]/div[1]/div[2]/table/tbody/tr/td[3]/text()')[1:6]
    # print(time)
    shoot = tree.xpath('/html/body/div[3]/div[4]/div[1]/div[2]/table/tbody/tr/td[4]/text()')[1:6]
    # print(shoot)
    three_point = tree.xpath('/html/body/div[3]/div[4]/div[1]/div[2]/table/tbody/tr/td[5]/text()')[1:6]
    # print(three_point)
    fa_qiu = tree.xpath('/html/body/div[3]/div[4]/div[1]/div[2]/table/tbody/tr/td[6]/text()')[1:6]
    # print(fa_qiu)
    fangui = tree.xpath('/html/body/div[3]/div[4]/div[1]/div[2]/table/tbody/tr/td[11]/text()')[1:6]
    # print(fangui)
    qiangduan = tree.xpath('/html/body/div[3]/div[4]/div[1]/div[2]/table/tbody/tr/td[12]/text()')[1:6]
    # print(qiangduan)
    shiwu = tree.xpath('/html/body/div[3]/div[4]/div[1]/div[2]/table/tbody/tr/td[13]/text()')[1:6]
    # print(shiwu)
    fenggai = tree.xpath('/html/body/div[3]/div[4]/div[1]/div[2]/table/tbody/tr/td[14]/text()')[1:6]
    # print(fenggai)
    point = tree.xpath('/html/body/div[3]/div[4]/div[1]/div[2]/table/tbody/tr/td[15]/text()')[1:6]
    # 去空白
    a = []
    for i in point:
        i = i.strip("\n")
        if len(i) == 0:
            i = "/"
        a.append(i)
    point = a
    # 去空白
    # print(point)
    zheng_fu = tree.xpath('/html/body/div[3]/div[4]/div[1]/div[2]/table/tbody/tr/td[16]/text()')[1:6]
    # 去空白
    b = []
    for i in zheng_fu:
        i = i.strip("\n")
        if len(i) == 0:
            i = "/"
        b.append(i)
    zheng_fu = b
    # 去空白

    # print(zheng_fu)
    return [name, part, time, shoot, three_point, fa_qiu,
            fangui, qiangduan, shiwu, fenggai, point, zheng_fu]


def get_second_group(url, headers):
    """拿到第二支队伍的数据"""
    response = requests.get(url, headers)
    tree = etree.HTML(response.text)
    name = tree.xpath('/html/body/div[3]/div[4]/div[1]/div[3]/table/tbody/tr/td[1]/a/text()')[:5]
    # print(name)
    part = tree.xpath('/html/body/div[3]/div[4]/div[1]/div[3]/table/tbody/tr/td[2]/text()')[:5]
    # print(part)
    time = tree.xpath('/html/body/div[3]/div[4]/div[1]/div[3]/table/tbody/tr/td[3]/text()')[1:6]
    # print(time)
    shoot = tree.xpath('/html/body/div[3]/div[4]/div[1]/div[3]/table/tbody/tr/td[4]/text()')[1:6]
    # print(shoot)
    three_point = tree.xpath('/html/body/div[3]/div[4]/div[1]/div[3]/table/tbody/tr/td[5]/text()')[1:6]
    # print(three_point)
    fa_qiu = tree.xpath('/html/body/div[3]/div[4]/div[1]/div[3]/table/tbody/tr/td[6]/text()')[1:6]
    # print(fa_qiu)
    fangui = tree.xpath('/html/body/div[3]/div[4]/div[1]/div[3]/table/tbody/tr/td[11]/text()')[1:6]
    # print(fangui)
    qiangduan = tree.xpath('/html/body/div[3]/div[4]/div[1]/div[3]/table/tbody/tr/td[12]/text()')[1:6]
    # print(qiangduan)
    shiwu = tree.xpath('/html/body/div[3]/div[4]/div[1]/div[3]/table/tbody/tr/td[13]/text()')[1:6]
    # print(shiwu)
    fenggai = tree.xpath('/html/body/div[3]/div[4]/div[1]/div[3]/table/tbody/tr/td[14]/text()')[1:6]
    # print(fenggai)
    point = tree.xpath('/html/body/div[3]/div[4]/div[1]/div[3]/table/tbody/tr/td[15]/text()')[1:6]
    # 去空白
    a = []
    for i in point:
        i = i.strip("\n")
        if len(i) == 0:
            i = "/"
        a.append(i)
    point = a
    # 去空白
    # print(point)
    zheng_fu = tree.xpath('/html/body/div[3]/div[4]/div[1]/div[2]/table/tbody/tr/td[16]/text()')[1:6]
    # 去空白
    b = []
    for i in zheng_fu:
        i = i.strip("\n")
        if len(i) == 0:
            i = "/"
        b.append(i)
    zheng_fu = b
    # 去空白

    # print(zheng_fu)
    return [name, part, time, shoot, three_point, fa_qiu,
            fangui, qiangduan, shiwu, fenggai, point, zheng_fu]


def save(file_name, fist, second):
    col = ["首发	", "位置", "时间", "投篮", "3分", "罚球", "犯规", "抢断", "失误",	"封盖",	"得分",	"+/-"]
    workbook = xlwt.Workbook()
    sheet = workbook.add_sheet("NBA",cell_overwrite_ok=True)

    for i in range(12):
        sheet.write(0, i, col[i])

    workbook.save(file_name)


def shoot(list, head, time):
    """拿到数据"""
    for url in list:
        first = get_first_group(url, head)
        second = get_second_group(url, head)
        save(f"{time}比赛数据.xls", first, second)



def get_into_url(url, headers, time):
    """拿到第一层网址"""
    response = requests.get(url, headers)
    # print(response.text)
    tree = etree.HTML(response.text)
    into_url_list = tree.xpath('/html/body/div[3]/div[4]/div[1]/div/div/div[2]/a[1]/@href')
    shoot(into_url_list, headers, time)


def main():
    url = 'https://nba.hupu.com/games'
    head = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36'
    }

    time = datetime.date.today()
    get_into_url(url, head, time)



if __name__ == '__main__':
    main()
