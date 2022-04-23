import xlwt
import requests
from lxml import etree
import datetime


def get_data(url, head):
    """获取数据"""
    response = requests.get(url, head)
    tree = etree.HTML(response.text)
    level = list(range(1, 51))
    name = tree.xpath('/html/body/div[3]/div[4]/div/table/tbody/tr/td[2]/a/text()')
    group = tree.xpath('/html/body/div[3]/div[4]/div/table/tbody/tr/td[3]/a/text()')
    shoot_lv = tree.xpath('/html/body/div[3]/div[4]/div/table/tbody/tr/td[4]/text()')[1:]
    tiaozheng = tree.xpath('/html/body/div[3]/div[4]/div/table/tbody/tr/td[5]/text()')[1:]
    get_shoot = tree.xpath('/html/body/div[3]/div[4]/div/table/tbody/tr/td[6]/text()')[1:]
    get_three_point = tree.xpath('/html/body/div[3]/div[4]/div/table/tbody/tr/td[7]/text()')[1:]
    changci = tree.xpath('/html/body/div[3]/div[4]/div/table/tbody/tr/td[8]/text()')[1:]
    time = tree.xpath('/html/body/div[3]/div[4]/div/table/tbody/tr/td[9]/text()')[1:]
    # print(len(tiaozheng))
    # print((get_shoot))
    # print(len(get_three_point))
    # print(len(changci))
    # print(len(time))
    data = [level, name, group, shoot_lv, tiaozheng, get_shoot, get_three_point, changci, time]
    return data


def save(data_list, time):
    """保存xls文件"""
    workbook = xlwt.Workbook()
    sheet = workbook.add_sheet("NBA", cell_overwrite_ok=True)
    col = ["排名", "球员", "球队", "得分", "命中-出手", "命中率", "命中-三分", "三分命中率", "命中-罚球"]
    for a in range(9):
        sheet.write(0, a, col[a])
    for j in range(9):
        list = data_list[j]
        for i in range(50):
            sheet.write(i + 1, j, list[i])

    workbook.save(f"{time}NBA球员得分榜.xls")


def main():
    url = 'https://nba.hupu.com/stats/players/pts'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36'}
    time = datetime.date.today()
    print("正在爬取NBA数据中")

    data = get_data(url, headers)
    print("正在保存xls文件~~~")
    save(data, time)
    print("保存成功！")
    input("按任意键退出~")


if __name__ == '__main__':
    main()
